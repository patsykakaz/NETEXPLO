#-*- coding: utf-8 -*-
from __future__ import unicode_literals

import random
from random import randint
secure_random = random.SystemRandom()

from django.db.models import Q
# from django.http import HttpResponse, HttpResponseRedirect
from mezzanine.pages.page_processors import processor_for
from mezzanine.blog.models import *
from MAIN.models import *

@processor_for('/')
def processor_home(request, page):
    # color_list = ["#29D6B9","#528DD9","#45BABA","#8BCABB","#F7C542","#E3708D","#65BDD6","#CC959B","#29D6B9",]
    Home = HomePage.objects.last()
    try: 
        color_list = Home.color_list
        color_list = str(color_list).strip().split(',')
        customColor = secure_random.choice(color_list)
    except: 
        customColor = '#528DD9'
    last_video = BlogPost.objects.exclude(video="").last()
    print "last blog w/video = " + str(last_video)
    # Videos = HomeVideo.objects.filter(master=Home)
    # if len(Videos) > 1:
    #     print 'VIDEO'+str(len(Videos))
    #     Home.video = secure_random.choice(Videos)
    #     customColmor = Home.video.color
    #     darken_navbar = Home.video.darken_navbar
    # else:
    Home.captions = HomeCaption.objects.filter(master=Home)
    return locals()

@processor_for(Section)
def processor_section(request, page):
    Target = Section.objects.get(pk=page.pk)
    Target_slots = Slot.objects.filter(master=Target)
    print Target_slots
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
    PressFiles_container = PressFiles.objects.last()
    customColor = target.color
    pressKit_fr = PressFiles_container.pressKit_fr
    pressKit_en = PressFiles_container.pressKit_en
    blogPosts = BlogPost.objects.all()[:12]
    M_A_logo = MediaAsset.objects.filter(type_asset='Logo')
    M_A_video  = MediaAsset.objects.filter(type_asset='Video')
    M_A_photo  = MediaAsset.objects.filter(type_asset='Photo')
    M_A_forum  = MediaAsset.objects.filter(type_asset='Forum')
    # sponsors_A = Sponsor.objects.filter(type_sponsor="A")
    # sponsors_B = Sponsor.objects.filter(type_sponsor="B")
    return locals()

@processor_for("histoire")
def processor_section(request, page):
    Target = Section.objects.get(pk=page.pk)
    customColor = Target.color
    network_all = Network.objects.all().order_by('?')
    team_all = Team.objects.all().order_by('?')
    for element in team_all:
        x = randint(1,3)
        if x == 3 and element.illustration_3:
            element.illustration = element.illustration_3
        elif x == 2 and element.illustration_2:
            element.illustration = element.illustration_2
        else: 
            element.illustration = element.illustration_1
    return locals()



