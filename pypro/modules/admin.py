from django.contrib import admin
from ordered_model.admin import OrderedModelAdmin

from pypro.modules.models import Module


class ModuleAdmin(OrderedModelAdmin):
    list_display = ('title', 'audience', 'move_up_down_links')
    prepopulated_fields = {'slug': ('title', )}


admin.site.register(Module, ModuleAdmin)
