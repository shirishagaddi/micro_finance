from django import template
from micro_admin.models import *
register = template.Library()


@register.filter
def get_count(pk):
    group = Groups.objects.get(id=pk)
    count = group.clients.all().count()
    return count


@register.filter
def get_centers_count(pk):
	center = Centers.objects.get(id=pk)
	count = center.groups.all().count()
	return count

