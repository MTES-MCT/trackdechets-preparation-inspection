from django import template

register = template.Library()


@register.filter
def number(nb):
    """Format a given number with thousands separators (spaces)"""
    if not nb:
        return ""
    return str(nb).replace(" ", "&nbsp;")
