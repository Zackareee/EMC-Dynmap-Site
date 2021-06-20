from PIL import Image, ImageDraw
from .ImageHandling import *
from .Download import *
from .Returns import *
import numpy as np
import json

def TownOutline(TownName,Date,Mode=0,Server="Towny"): #Hachijo
  outputx, outputz, outputcolor, outputstring = [], [], [], []
  if path.isfile(F'{str(getcwd())}/DynmapArchive/JSON/{Server}/{Date}/{Date}.json'):
    with open(F'{str(getcwd())}/DynmapArchive/JSON/{Server}/{Date}/{Date}.json') as f:
      try:
        data = json.load(f)
      except:
        return "Valid Json Not Found", F"File Format Invalid. {Date}"
      for Town in TownName:
        if Mode == 0 and not(Town != None and F'{Town}__0' in data['sets']['townyPlugin.markerset']['areas']):
          return "Town Not Found", Town
        for item in data['sets']['townyPlugin.markerset']['areas']:
          if Mode == 0:

            if data['sets']['townyPlugin.markerset']['areas'][item]['label'] == Town and "Shop" not in str(item):
              outputx.append([int(x) for x in data["sets"]["townyPlugin.markerset"]["areas"][F"{item}"]["x"]])
              outputz.append([int(z) for z in data["sets"]["townyPlugin.markerset"]["areas"][F"{item}"]["z"]])
              outputcolor.append(data["sets"]["townyPlugin.markerset"]["areas"][F"{item}"]["fillcolor"])
          else:
            if data['sets']['townyPlugin.markerset']['areas'][item]['label'].startswith(Town) and "Shop" not in str(item):
              outputstring.append(data["sets"]["townyPlugin.markerset"]["areas"][F"{item}"]["label"])
    if not Mode == 0:
      return [outputstring]
    else:
      return outputx, outputz, outputcolor, Date
  else:
    return "Date Not Found", Date

def TownRender(TownX, TownZ, Width, Height, text="", FillColor=(0, 255, 255)):
  ImageRender = Image.new('RGB', (Width+17, Height+17), color='white')
  TownOutline = ImageDraw.Draw(ImageRender, 'RGBA')
  ChunkGrid = ImageDraw.Draw(ImageRender)
  Grid(ChunkGrid,Width+17,Height+17)
  for i in range(len(TownX)):
    Tuple = tuple(map(tuple, np.c_[TownX[i],TownZ[i]]))
    TownOutline.polygon(Tuple, outline=(0, 0, 255, 100), fill=(FillColor[i][0], FillColor[i][1], FillColor[i][2], 100))
    for j in range(int(len(Tuple))):
      TownOutline.line([Tuple[j-1],Tuple[j]],width=2,fill=(0, 0, 255))
  TownOutline.rectangle([(1,1),(47,15)], fill=(255,255,255), outline=None, width=1)
  TownOutline.text((4,4), F"{text}", fill=(0,0,0,128))
  return ImageRender

def TownGif(TownNames,TownDate,Server):
  Gif, GifX, GifZ, Dates = [], [], [], []
  for i in TownDate:
    vals = TownOutline(TownNames, i,Server=Server)
    if len(vals) == 4:
      TownX, TownZ, FillColor, Date = vals[0],vals[1],vals[2],vals[3]
    else:
      return vals[0], vals[1]

    GifX.append(TownX)
    GifZ.append(TownZ)
    Dates.append(Date)
  GifZ = [[[GifZ[j][i][f] - (ThreeDMinimumReturn(GifZ) - 16) for f in range(len(GifZ[j][i]))] for i in range(len(GifZ[j]))] for j in range(len(GifZ))]
  GifX = [[[GifX[j][i][f] - (ThreeDMinimumReturn(GifX) - 16) for f in range(len(GifX[j][i]))] for i in range(len(GifX[j]))] for j in range(len(GifX))]
  for i in range(len(GifX)):
    Gif.append(TownRender(GifX[i], GifZ[i], ThreeDMaximumReturn(GifX), ThreeDMaximumReturn(GifZ),Dates[i],[tuple(int(j.lstrip('#')[i:i+2], 16) for i in (0, 2, 4)) for j in FillColor]))
  return Gif



def TG(dates, town):
    Gif = TownGif(town, dates, "Towny")

    if type(Gif[0]) is str and "Not Found" in Gif[0]:
      return Gif[0], Gif[1]
    if Gif == None:
      return "Fail"
    else:
      Gif[0].save(F"{str(getcwd())}/DynmapArchive/static/TempRender.gif", save_all=True, append_images=Gif[1:], optimize=False,duration=1000, loop=0)




def TR(date,town):
    townarray = TownOutline(town,date)
    if len(townarray) != 4:
      if 'Not Found' in townarray[0]:
        return townarray[0], townarray[1]
      else:
        return json.dumps({"error": "true", "message": "Invalid Date"})

    else:
      TownX = townarray[0]
      TownZ = townarray[1]
      FillColor = townarray[2]
      TownX = [[TownX[j][i] - (MinimumReturn(TownX) - 16) for i in range(len(TownX[j]))] for j in range(len(TownX))]
      TownZ = [[TownZ[j][i] - (MinimumReturn(TownZ) - 16) for i in range(len(TownZ[j]))] for j in range(len(TownZ))]
      TownRender(TownX, TownZ, MaximumReturn(TownX), MaximumReturn(TownZ),date,FillColor=[tuple(int(j.lstrip('#')[i:i+2], 16) for i in (0, 2, 4)) for j in FillColor]).save(F"{str(getcwd())}/DynmapArchive/static/TempRender.png")



def TS(date,query):
  Towns = TownOutline(query, date, 1)
  return Towns