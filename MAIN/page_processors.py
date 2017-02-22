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
    Target = Section.objects.get(pk=page.pk)
    Target.slots = Slot.objects.filter(master=Target)
    customColor = Target.color
    return locals()

@processor_for("sponsors")
def processor_section(request, page):
    target = Section.objects.get(pk=page.pk)
    customColor = target.color
    sponsors_A = Sponsor.objects.filter(type_sponsor="A")
    sponsors_B = Sponsor.objects.filter(type_sponsor="B")
    return locals()

@processor_for("presse")
def processor_section(request, page):
    target = Section.objects.get(pk=page.pk)
    customColor = target.color
    # sponsors_A = Sponsor.objects.filter(type_sponsor="A")
    # sponsors_B = Sponsor.objects.filter(type_sponsor="B")
    return locals()




