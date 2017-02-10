#-*- coding: utf-8 -*-
from __future__ import unicode_literals

import random
secure_random = random.SystemRandom()
# from django.http import HttpResponse, HttpResponseRedirect
from mezzanine.pages.page_processors import processor_for
from MAIN.models import *

@processor_for('/')
def processor_home(request, page):
    Home = HomePage.objects.last()
    if len(HomeVideo.objects.filter(master=Home)):
        Home.video = HomeVideo.objects.filter(master=Home)
        Home.video = secure_random.choice(Home.video)
        if Home.video.darken_navbar: 
            darken_navbar = True
    else:
        Home.captions = HomeCaption.objects.filter(master=Home)
    return locals()




