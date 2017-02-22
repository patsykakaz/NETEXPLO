#-*- coding: utf-8 -*-
from __future__ import unicode_literals

from modeltranslation.translator import translator, TranslationOptions
from .models import *


class TranslatedHomePage(TranslationOptions):
    fields = ('sub_title','caption')

class TranslatedSection(TranslationOptions):
    fields = ('caption','sub_title')

class TranslatedSlot(TranslationOptions):
    fields = ('caption',)

class TranslatedTeam(TranslationOptions):
    fields = ('fonction',)

class TranslatedNetwork(TranslationOptions):
    fields = ('poste','university','ville','pays')



translator.register(HomePage, TranslatedHomePage)
translator.register(Section, TranslatedSection)
translator.register(Slot, TranslatedSlot)
translator.register(Team, TranslatedTeam)
translator.register(Network, TranslatedNetwork)
translator.register(Sponsor)
translator.register(PressFiles)




