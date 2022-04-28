from flask import Blueprint, render_template, flash
from datetime import timedelta
from .Dependancies.render import TR, TG, TS
from .forms import TownMapForm, SearchForm, NationMapForm
from os import getcwd
import base64
import time
import cProfile
import pstats

mainbp = Blueprint('main', __name__)

import os

if os.name == 'nt':
    s = "#"
else:
    s = "-"

@mainbp.after_request
def add_header(response):
    response.cache_control.no_store = True
    return response


@mainbp.route('/', methods=['GET', 'POST'])
def index():
    forms = TownMapForm()
    queryForm = SearchForm()
    nforms = NationMapForm()

    encoded_string = Towns = None
    if forms.addrow.data:
        forms.town.append_entry()

    if forms.delrow.data:
        if len(forms.town.data) > 1:
            forms.town.pop_entry()


    if queryForm.qsubmit.data == True :
        Towns = TS(queryForm.date.data.strftime(F"%{s}d.%{s}m.%{s}y"), [queryForm.query.data])
        print(Towns)
    if forms.submit.data == True :
        datelimit = 32 # KEEP AT 32
        towns = []
        for i in forms.town.data:
            towns.append(i["town"])

        date = forms.date.data
        if forms.datetwo.data:
            datelist = []
            for i in range((forms.datetwo.data - date).days + 1):
                day = date + timedelta(days=i)
                datelist.append(day.strftime(F"%{s}d.%{s}m.%{s}y"))

            if len(datelist) < datelimit and len(datelist) > 0:
                start = time.perf_counter()
                temp = TG(datelist, towns)

                elapsed = time.perf_counter() - start
                print(f'done in {elapsed:.2f}s')
                if temp != None and ("Not Found" in temp[0]):
                    flash(F'{temp[0]}; {temp[1]}', "error")
                elif temp == False:
                        flash(F'File size too large', "error")
                else:
                    with open(F"{str(getcwd())}/DynmapArchive/static/TempRender.gif", "rb") as image_file:
                        encoded_string = base64.b64encode(image_file.read())

            else:
                flash('Start Date and End Date must be within 31 days.', "error")

        else:

            temp = TR(date.strftime(F"%{s}d.%{s}m.%{s}y"), towns)
            if temp != None and ("Not Found" in temp[0]):
                flash(F'{temp[0]} {temp[1]}', "error")
            else:
                with open(F"{str(getcwd())}/DynmapArchive/static/TempRender.png", "rb") as image_file:
                    encoded_string = base64.b64encode(image_file.read())


    if encoded_string != None: return render_template('index.html', heading='Top Listings', form=forms, qform=queryForm, nform=nforms,image=encoded_string.decode("utf-8"))
    if Towns != None: return render_template('index.html', form=forms, qform=queryForm, nform=nforms,text=Towns)
    return render_template('index.html', qform=queryForm, form=forms, nform=nforms)