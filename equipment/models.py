from django.db import models
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField

from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel
from modelcluster.fields import ParentalKey


class EquipmentOperator(models.Model):
    """Оператор оборудования."""

    name = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField()

    equipment = ParentalKey(
        'equipment.EquipemntPage',
        on_delete=models.CASCADE,
        related_name='operators'
        )


class EquipemntPage(Page):
    """Старница с информацией о единице оборудования."""
    
    description = RichTextField(
        blank=True, 
        null=True,
        features=['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 
                'hr', 'bold', 'italic', 'ol', 'ul', 'link' ],
        )
    
    content_panels = Page.content_panels + [
        FieldPanel('description'),
        MultiFieldPanel([
            InlinePanel('operators', label="оператора")],
            heading="Операторы",
            )
    ]
    
    subpage_types = []
    parent_page_types = ['equipment.EquipmentIndexPage']
    
    class Meta:
        verbose_name = "Оборудование"
        verbose_name_plural = "Оборудование"


class EquipmentIndexPage(Page):
    """Страница для выведения списка оборудования."""

    max_count = 1

    subpage_types = ['equipment.EquipemntPage']
    parent_page_types = ['home.HomePage']
