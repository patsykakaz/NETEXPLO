#-*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import ugettext, ugettext_lazy as _

from settings import MEDIA_ROOT
from mezzanine.pages.models import Page
from mezzanine.core.models import RichText
from mezzanine.core.fields import RichTextField, FileField
from mezzanine.utils.models import upload_to

from colorfield.fields import ColorField


# HOMEPAGE
    # Carousel (inlines)
    # Videos (inlines)
    
# SECTION
    # illustration
    # caption
    # Dark/white
# SPACE
    # background    
    # shadow ? 
    # illustration
    # left/right
    # title
    # caption

# MEMBRE RESEAU INTERNATIONAL
# EMPLOYEE
# PARTENAIRES
# PRESSBOOK
# ASSETS

class HomePage(Page, RichText):
    caption = RichTextField()
class HomeVideo(models.Model):
    master = models.ForeignKey("HomePage")
    title = models.CharField(max_length=255, blank=True, null=False)
    # file = models.FileField(upload_to='uploads/videos', blank=False)
    file = FileField(upload_to=upload_to("MAIN.HomeVideoCaption.video", "video"), max_length=255, null=False, blank=True)
    illustration_alt = FileField(verbose_name=_("illustration_alt"),
        upload_to=upload_to("MAIN.HomeVideoCaption.illustration_alt", "illustration_alt"), max_length=255, null=False, blank=True)
    color = ColorField(null=False, blank=True, default="rgb(114,196,231)")
    darken_navbar = models.BooleanField(default=False, verbose_name='Assombrir navbar',help_text='Ajouter un fond sombre à la navbar pour qu\'elle ressorte correctement lorsque le fond de la video est clair')
class HomeCaption(models.Model):
    master = models.ForeignKey("HomePage")
    title = models.CharField(max_length=255, blank=True, null=True, editable=False)
    illustration = FileField(verbose_name=_("illustration"),
        upload_to=upload_to("MAIN.HomeVideoCaption.illustration", "illustration"),
        format="Image", max_length=255, null=True, blank=True)
    color = ColorField(null=False, blank=True, default="72C4E7")

class Section(Page,RichText):
    illustration = FileField(verbose_name=_("illustrationSection"),
        upload_to=upload_to("MAIN.HomeVideoCaption.illustration", "Section"),
        format="Image", max_length=255, null=False, blank=True)
    color = ColorField(null=False, blank=True, default="72C4E7")
    caption = RichTextField()

class Slot(Page,RichText):
    master = models.ForeignKey("Section")
    illustration = FileField(verbose_name=_("illustrationSlot"),
        upload_to=upload_to("MAIN.HomeVideoCaption.illustration", "Slot"),
        format="Image", max_length=255, null=False, blank=True)
    color = ColorField(null=False, blank=True, default="72C4E7", verbose_name='background color')
    caption = RichTextField()

class Team(Page):
    prenom = models.CharField(max_length=255,null=False,blank=False)
    fonction = models.CharField(max_length=255,null=False,blank=False)
    email = models.EmailField(null=False,blank=False)
    illustration = FileField(verbose_name=_("illustrationTeam"),
        upload_to=upload_to("MAIN.HomeVideoCaption.illustration", "Team"),
        format="Image", max_length=255, null=False, blank=True)

class Network(Page):
    prenom = models.CharField(max_length=255,null=False,blank=False)
    poste = models.CharField(max_length=255,null=False,blank=False)
    university = models.CharField(max_length=255,null=False,blank=False)
    ville = models.CharField(max_length=255,null=False,blank=False)
    pays = models.CharField(max_length=255,null=False,blank=False)








