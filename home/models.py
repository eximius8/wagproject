from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.fields import RichTextField, StreamField

from wagtail.core.blocks import RichTextBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock

from .blocks import FigCaptionBlock

from wagtail.snippets.models import register_snippet


@register_snippet
class Footer(models.Model):

    bodytext = RichTextField()

    panels = [
        FieldPanel('bodytext')
    ]

    class Meta:
        verbose_name = "Футер"
        verbose_name_plural = "Футеры"

    def __str__(self):
        return "Футер"





class NewsPage(Page):

    template = 'home/newspage.html'

    max_count = 3


class HomePage(Page):

    #subpage_types = ['home.NewsPage']
    parent_page_types = []
       
    # поля в базе данных
    subtitle = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="Подзаголовок"
    )
    rtfbody = RichTextField(
        features=['h1', 'h6', 'hr', 'bold', 'italic'],
        blank=True,
        null=True,
    )

    body = StreamField([
        ('figcaptionblock', FigCaptionBlock()),
        ('rtfblock', RichTextBlock(
            features=['h1', 'h6', 'hr', 'bold', 'italic'],
            label="Текст", 
            help_text="Введите описание")),
        ('imgblock', ImageChooserBlock(
            template="blocks/imgblock.html"
        )),
        ('youtubeblock', EmbedBlock(
            icon="success"
        ))

        ],
         block_counts={
                        'rtfblock': {'min_num': 1},
                        'imgblock': {'max_num': 1},
                    },
        blank=True)

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
