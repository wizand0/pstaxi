from django import template
from django.template import defaultfilters

register = template.Library()


@register.filter
def pstaxidate(date):
    return defaultfilters.date(date, "d.m.Y г.")
