from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import RichTextField


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

    # поля для ввода данных в интерефейсе администратора

    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        FieldPanel('rtfbody'),
    ]

    # promote_panels = []
    # settings_panels = []
