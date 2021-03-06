#-*- coding: utf-8 -*-

from copy import deepcopy
from django.contrib import admin
from mezzanine.pages.models import RichTextPage
from mezzanine.pages.admin import PageAdmin
from mezzanine.blog.admin import BlogPostAdmin
from mezzanine.blog.models import BlogPost
from .models import *

HomePage_fieldsets = deepcopy(PageAdmin.fieldsets)
HomePage_fieldsets[0][1]["fields"].insert(-1, "baseline")
HomePage_fieldsets[0][1]["fields"].insert(-1, "sub_title")
HomePage_fieldsets[0][1]["fields"].insert(-1, "color_list")
HomePage_fieldsets[0][1]["fields"].insert(-1, "color_caption")
HomePage_fieldsets[0][1]["fields"].insert(-1, "color_caption_text")
HomePage_fieldsets[0][1]["fields"].insert(-1, "slider_timer")
HomePage_fieldsets[0][1]["fields"].insert(-1, "caption")
class HomeCaptionInline(admin.TabularInline):
    model = HomeCaption
    extra = 5
class HomeVideoInline(admin.TabularInline):
    model = HomeVideo
    extra = 5
class HomePageAdmin(PageAdmin):
    fieldsets = HomePage_fieldsets
    inlines = (HomeCaptionInline,HomeVideoInline)

Section_fieldsets = deepcopy(PageAdmin.fieldsets)
Section_fieldsets[0][1]["fields"].insert(-1, "illustration")
Section_fieldsets[0][1]["fields"].insert(-1, "color")
Section_fieldsets[0][1]["fields"].insert(-1, "caption_color")
Section_fieldsets[0][1]["fields"].insert(-1, "text_color")
Section_fieldsets[0][1]["fields"].insert(-1, "sub_title")
Section_fieldsets[0][1]["fields"].insert(-1, "caption")
class SectionAdmin(PageAdmin):
        fieldsets = Section_fieldsets

Slot_fieldsets = deepcopy(PageAdmin.fieldsets)
Slot_fieldsets[0][1]["fields"].insert(-1, "master")
Slot_fieldsets[0][1]["fields"].insert(-1, "illustration")
Slot_fieldsets[0][1]["fields"].insert(-1, "color")
Slot_fieldsets[0][1]["fields"].insert(-1, "text_color")
Slot_fieldsets[0][1]["fields"].insert(-1, "pull_image_left")
Slot_fieldsets[0][1]["fields"].insert(-1, "caption")
class SlotAdmin(PageAdmin):
        fieldsets = Slot_fieldsets

Team_fieldsets = deepcopy(PageAdmin.fieldsets)
Team_fieldsets[0][1]["fields"].insert(-1, "prenom")
Team_fieldsets[0][1]["fields"].insert(-1, "fonction")
Team_fieldsets[0][1]["fields"].insert(-1, "email")
Team_fieldsets[0][1]["fields"].insert(-1, "illustration_1")
Team_fieldsets[0][1]["fields"].insert(-1, "illustration_2")
Team_fieldsets[0][1]["fields"].insert(-1, "illustration_3")
class TeamAdmin(PageAdmin):
        fieldsets = Team_fieldsets

Network_fieldsets = deepcopy(PageAdmin.fieldsets)
Network_fieldsets[0][1]["fields"].insert(-1, "prenom")
Network_fieldsets[0][1]["fields"].insert(-1, "poste")
Network_fieldsets[0][1]["fields"].insert(-1, "university")
Network_fieldsets[0][1]["fields"].insert(-1, "ville")
Network_fieldsets[0][1]["fields"].insert(-1, "pays")
class NetworkAdmin(PageAdmin):
        fieldsets = Network_fieldsets

Sponsor_fieldsets = deepcopy(PageAdmin.fieldsets)
Sponsor_fieldsets[0][1]["fields"].insert(-1, "logo")
Sponsor_fieldsets[0][1]["fields"].insert(-1, "type_sponsor")
Sponsor_fieldsets[0][1]["fields"].insert(-1, "lien")
class SponsorAdmin(PageAdmin):
        fieldsets = Sponsor_fieldsets


Press_fieldsets = deepcopy(PageAdmin.fieldsets)
Press_fieldsets[0][1]["fields"].insert(-1, "caption_color")
Press_fieldsets[0][1]["fields"].insert(-1, "color")
Press_fieldsets[0][1]["fields"].insert(-1, "pressKit_fr")
Press_fieldsets[0][1]["fields"].insert(-1, "pressKit_en")
class MediaAssetInline(admin.TabularInline):
    model = MediaAsset
    extra = 12
class PressFilesAdmin(PageAdmin):
        fieldsets = Press_fieldsets
        inlines = (MediaAssetInline,)



admin.site.register(HomePage, HomePageAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(Slot, SlotAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Network, NetworkAdmin)
admin.site.register(Sponsor, SponsorAdmin)
admin.site.register(PressFiles, PressFilesAdmin)



# BLOG ADMIN (model modified through settings)

blog_fieldsets = deepcopy(BlogPostAdmin.fieldsets)
blog_fieldsets[0][1]["fields"].insert(-2, "video")

class MyBlogPostAdmin(BlogPostAdmin):
    fieldsets = blog_fieldsets

admin.site.unregister(BlogPost)
admin.site.register(BlogPost, MyBlogPostAdmin)



