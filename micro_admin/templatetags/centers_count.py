from django import template
from  micro_admin.models import *
register = template.Library()

@register.filter
def get_count(value):
       return range(value)