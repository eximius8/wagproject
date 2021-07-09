
from wagtail.core.blocks import StructBlock, CharBlock
from wagtail.images.blocks import ImageChooserBlock


class FigCaptionBlock(StructBlock):

    figure = ImageChooserBlock(label="Картинка")
    caption = CharBlock()
    


    class Meta:

        icon = 'image'
        template = 'blocks/fig_caption_block.html'
        label="Картинка с подписью"