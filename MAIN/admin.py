#-*- coding: utf-8 -*-

from copy import deepcopy
from django.contrib import admin
from mezzanine.pages.admin import PageAdmin
from mezzanine.pages.models import RichTextPage
from .models import *

HomePage_fieldsets = deepcopy(PageAdmin.fieldsets)
HomePage_fieldsets[0][1]["fields"].insert(-1, "caption")
class HomeCaptionInline(admin.TabularInline):
    model = HomeCaption
    extra = 4
class HomeVideoInline(admin.TabularInline):
    model = HomeVideo
    extra = 4
class HomePageAdmin(PageAdmin):
        inlines = (HomeCaptionInline,HomeVideoInline)
        fieldsets = HomePage_fieldsets

Section_fieldsets = deepcopy(PageAdmin.fieldsets)
Section_fieldsets[0][1]["fields"].insert(-1, "illustration")
Section_fieldsets[0][1]["fields"].insert(-1, "color")
Section_fieldsets[0][1]["fields"].insert(-1, "caption")
class SectionAdmin(PageAdmin):
        fieldsets = Section_fieldsets

Slot_fieldsets = deepcopy(PageAdmin.fieldsets)
Slot_fieldsets[0][1]["fields"].insert(-1, "master")
Slot_fieldsets[0][1]["fields"].insert(-1, "illustration")
Slot_fieldsets[0][1]["fields"].insert(-1, "color")
Slot_fieldsets[0][1]["fields"].insert(-1, "caption")
class SlotAdmin(PageAdmin):
        fieldsets = Slot_fieldsets


admin.site.register(HomePage, HomePageAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(Slot, SlotAdmin)

