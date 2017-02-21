#-*- coding: utf-8 -*-
from __future__ import unicode_literals

import random
secure_random = random.SystemRandom()

from django.db.models import Q
# from django.http import HttpResponse, HttpResponseRedirect
from mezzanine.pages.page_processors import processor_for
from MAIN.models import *

@processor_for('/')
def processor_home(request, page):
    Home = HomePage.objects.last()
    customColor = Home.color
    Videos = HomeVideo.objects.filter(master=Home)
    if len(Videos) > 1:
        print 'VIDEO'+str(len(Videos))
        Home.video = secure_random.choice(Videos)
        customColor = Home.video.color
        darken_navbar = Home.video.darken_navbar
    else:
        Home.captions = HomeCaption.objects.filter(master=Home)
    return locals()

@processor_for(Section)
def processor_section(request, page):
    Section = Section.objects.get(pk=page.pk)
    Section.slots = Slot.objects.filter(master=Section)
    return locals()




