import requests
from os import path, makedirs, getcwd
from datetime import datetime

def MarkerDownload(Server):
    print(F"{str(getcwd())}/JSON/{str(Server)}/{str(datetime.today().strftime('%-d.%-m.%y'))}/{str(datetime.today().strftime('%-d.%-m.%y'))}.json")
    Headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    if not path.exists(F"{str(getcwd())}/JSON/{str(Server)}/{str(datetime.today().strftime('%-d.%-m.%y'))}/{str(datetime.today().strftime('%-d.%-m.%y'))}.json"):
        if Server == "Towny":
            DownloadedFile = requests.get('https://earthmc.net/map/tiles/_markers_/marker_earth.json', headers=Headers)
        if '502: Bad gateway' in DownloadedFile:
            print("502: Bad gateway")
            MarkerDownload(Server)
        else:
            makedirs(F"{str(getcwd())}/JSON/{str(Server)}/{str(datetime.today().strftime('%-d.%-m.%y'))}/")
            open(F"{str(getcwd())}/JSON/{str(Server)}/{str(datetime.today().strftime('%-d.%-m.%y'))}/{str(datetime.today().strftime('%-d.%-m.%y'))}.json", 'wb').write(DownloadedFile.content)
            print("File Downloaded")
        return True
    else:
        return False