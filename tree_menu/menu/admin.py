from django.contrib import admin
from menu.models import Menu, Subject


@admin.register(Subject)
class MenuSubjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent')
    list_filter = ('menu',)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}
