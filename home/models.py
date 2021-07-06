from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.fields import RichTextField, StreamField

from wagtail.core.blocks import RichTextBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock


class HomePage(Page):
    
    # поля в базе данных
    subtitle = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="Подзаголовок"
    )
    rtfbody = RichTextField(
        blank=True,
        null=True,
    )

    body = StreamField([
        ('rtfblock', RichTextBlock()),
        ('imgblock', ImageChooserBlock()),
        ('youtubeblock', EmbedBlock())

    ],blank=True)

    bg_image = models.ForeignKey(
        'wagtailimages.Image',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    # поля для ввода данных в интерефейсе администратора

    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        FieldPanel('rtfbody'),
        ImageChooserPanel('bg_image'),
        StreamFieldPanel('body')     
    ]

    # promote_panels = []
    # settings_panels = []
