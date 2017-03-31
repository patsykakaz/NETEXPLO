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
    baseline =models.CharField(null=False, blank=True, max_length=255, verbose_name='Baseline (sur le carousel)')
    sub_title = models.CharField(null=False, blank=True, max_length=255, verbose_name='Sous-titre de la section')
    color = ColorField(default='#528DD9', help_text='Couleur identifiante de la page')
    color_caption = ColorField(default='#E8ECED', help_text='couleur de fond du paragraphe de la home')
    color_caption_text = ColorField(default='#333', help_text='couleur du texte du paragraphe de la home')
    slider_timer = models.IntegerField(default=3000, help_text='intervalle, en ms, du sliders')
    caption = RichTextField()

    class Meta:
        verbose_name='HOMEPAGE'
        # ordering = ['title']

    def save(self, *args, **kwargs):
        self.in_menus = []
        super(HomePage, self).save(*args, **kwargs)

class HomeVideo(models.Model):
    master = models.ForeignKey("HomePage")
    title = models.CharField(max_length=255, null=False,blank=False)
    # file = models.FileField(upload_to='uploads/videos', blank=False)
    file = FileField(upload_to=upload_to("MAIN.HomeVideoCaption.video", "video"), max_length=255, null=False,blank=False)
    illustration_alt = FileField(verbose_name=_("illustration_alt"),
        upload_to=upload_to("MAIN.HomeVideoCaption.illustration_alt", "illustration_alt"), max_length=255, null=False,blank=False)
    darken_navbar = models.BooleanField(null=False,blank=False, default=False, verbose_name='Assombrir navbar',help_text='Ajouter un fond sombre à la navbar pour qu\'elle ressorte correctement lorsque le fond de la video est clair')

class HomeCaption(models.Model):
    master = models.ForeignKey("HomePage")
    title = models.CharField(max_length=255, null=False, blank=False)
    image = FileField(verbose_name=_("Image"),
        upload_to=upload_to("MAIN.HomeVideoCaption.illustration", "SLIDER HOME"),
        format="Image", max_length=255)
    lien = models.URLField(null=False, blank=True)

class Section(Page,RichText):
    illustration = FileField(verbose_name=_("illustrationSection"),
        upload_to=upload_to("MAIN.HomeVideoCaption.illustration", "Section"),
        format="Image", max_length=255, null=False, blank=False)
    color = ColorField(default='#528DD9', help_text='couleur des éléments static de la page (navbar, footer)')
    caption_color = ColorField(default='#E8ECED', help_text='Couleur de fond du paragraphe introductif de la section')
    text_color = ColorField(default='#333', help_text='couleur du texte dans le paragraphe')
    sub_title = models.CharField(null=False, blank=True, max_length=255, verbose_name='Sous-titre de la section')
    caption = RichTextField()

    class Meta:
        verbose_name='SECTION'
        # ordering = ['title']

    def save(self, *args, **kwargs):
        self.in_menus = []
        super(Section, self).save(*args, **kwargs)

class Slot(Page,RichText):
    master = models.ForeignKey("Section")
    illustration = FileField(verbose_name=_("illustrationSlot"),
        upload_to=upload_to("MAIN.HomeVideoCaption.illustration", "Slot"),
        format="Image", max_length=255, null=False, blank=True)
    color = ColorField(default='#FFFFFF', verbose_name='couleur du fond du slot')
    text_color = ColorField(default='#333', verbose_name='couleur du texte placé dans le slot')
    pull_image_left = models.BooleanField(default=True, verbose_name='Placer l\'image à gauche', help_text='Décochez pour placer l\'image à droite')
    caption = RichTextField()

    class Meta:
        verbose_name='SLOT'
        # ordering = ['title']

    def save(self, *args, **kwargs):
        self.in_menus = []
        if not self.parent:
            try: 
                self.parent = Page.objects.get(pk=self.master.pk)
            except: 
                pass
        super(Slot, self).save(*args, **kwargs)


class Team(Page):
    prenom = models.CharField(max_length=255,null=False,blank=False)
    fonction = models.CharField(max_length=255,null=False,blank=False)
    email = models.EmailField(null=False,blank=True)
    illustration_1 = FileField(verbose_name=_("illustrationTeam"),
        upload_to=upload_to("MAIN.HomeVideoCaption.illustration", "Team"),
        format="Image", max_length=255, null=False, blank=True)
    illustration_2 = FileField(verbose_name=_("illustrationTeam"),
        upload_to=upload_to("MAIN.HomeVideoCaption.illustration", "Team"),
        format="Image", max_length=255, null=False, blank=True)
    illustration_3 = FileField(verbose_name=_("illustrationTeam"),
        upload_to=upload_to("MAIN.HomeVideoCaption.illustration", "Team"),
        format="Image", max_length=255, null=False, blank=True)

    class Meta:
        verbose_name='TEAM MEMBER'
        # ordering = ['title']

    def save(self, *args, **kwargs):
        self.in_menus = []
        if not self.parent:
            try: 
                self.parent = Page.objects.get(title="TEAM")
            except: 
                pass
        super(Team, self).save(*args, **kwargs)

class Network(Page):
    prenom = models.CharField(max_length=255,null=False,blank=False)
    poste = models.CharField(max_length=255,null=False,blank=False)
    university = models.CharField(max_length=255,null=False,blank=False)
    ville = models.CharField(max_length=255,null=False,blank=False)
    pays = models.CharField(max_length=255,null=False,blank=False)

    class Meta:
        verbose_name='NETWORK MEMBER'
        # ordering = ['title']

    def save(self, *args, **kwargs):
        self.in_menus = []
        if not self.parent:
            try: 
                self.parent = Page.objects.get(title='NETWORK')
            except: 
                pass
        super(Network, self).save(*args, **kwargs)

class Sponsor(Page):
    logo = FileField(verbose_name=_("Logo"),
        upload_to=upload_to("MAIN.Sponsor.logo", "logo"),
        format="Image", max_length=255, null=False, blank=False)
    type_choices = (
        ("A",'Partenaire'),
        ("B",'Entreprise adherente'),
    )
    type_sponsor = models.CharField(max_length=200, 
                    choices=type_choices, null=False, blank=False, verbose_name='Type de partenaire')
    lien = models.URLField(null=False, blank=True)

    class Meta:
        verbose_name='PARTENAIRE'
        # ordering = ['title']

    def save(self, *args, **kwargs):
        self.in_menus = []
        if not self.parent:
            try: 
                self.parent = Page.objects.get(title='SPONSORS')
            except: 
                pass
        super(Sponsor, self).save(*args, **kwargs)


class PressFiles(Page):
    caption_color = ColorField(default='#edf1f2', help_text='Couleur de fond du slot MEDIA ASSETS')
    color = ColorField(default='#333', help_text='couleur du texte du slot MEDIA ASSETS')

    def save(self, *args, **kwargs):
        self.in_menus = []
        super(PressFiles, self).save(*args, **kwargs)

class MediaAsset(models.Model):
    type_choices = (
        ("Logo",'Logo'),
        ("Video",'Video'),
        ("Photo",'Photo'),
        ("Forum",'Forum'),
    )
    type_asset = models.CharField(max_length=200, 
                    choices=type_choices, null=False, blank=False, verbose_name='Type de fichier')
    master = models.ForeignKey("PressFiles")
    title = models.CharField(max_length=255, null=False, blank=False)
    file = models.FileField(upload_to='press/', null=False, blank=False)
    image_file = FileField(verbose_name=_("image representation"),
        upload_to=upload_to("MAIN.MediaAsset.image_file", "image_file"),
        format="Image", max_length=255, null=False, blank=True)







