from django.contrib import admin
from ordered_model.admin import OrderedModelAdmin

from pypro.modules.models.model_module import Module
from pypro.modules.models.model_lecture import Lecture


class ModuleAdmin(OrderedModelAdmin):
    list_display = ('title', 'audience', 'move_up_down_links')
    prepopulated_fields = {'slug': ('title', )}


class LectureAdmin(OrderedModelAdmin):
    list_display = ('title', 'module', 'order', 'move_up_down_links')
    list_filter = ('module', )
    ordering = ('module', 'order')
    prepopulated_fields = {'slug': ('title', )}


admin.site.register(Module, ModuleAdmin)
admin.site.register(Lecture, LectureAdmin)
