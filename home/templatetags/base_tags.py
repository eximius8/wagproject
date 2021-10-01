from home.models import Footer

from django import template

from wagtail.core.models import Site 

register = template.Library()


@register.inclusion_tag('home/tags/footer.html', takes_context=True)
def footer_tag(context):

    return {
        'request': context['request'],
        'footer': Footer.objects.first()
    }


@register.simple_tag(takes_context=True)
def get_site_root(context):
    # This returns a core.Page. The main menu needs to have the site.root_page
    # defined else will return an object attribute error ('str' object has no
    # attribute 'get_children')
    return Site.find_for_request(context['request']).root_page


@register.inclusion_tag('tags/top_menu.html', takes_context=True)
def top_menu(context, parent):
    menuitems = parent.get_children().live().in_menu()
    
    return {        
        'menuitems': menuitems,
        # required by the pageurl tag that we want to use within this template
        'request': context['request'],
    }