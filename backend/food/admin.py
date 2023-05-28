from django.contrib import admin
from .models import Recipe


class RecipeAdmin(admin.ModelAdmin):
    # Перечисляем поля, которые должны отображаться в админке
    list_display = ('name')
    # Добавляем интерфейс для поиска по имени
    search_fields = ('name',)
    # Добавляем возможность фильтрации по имени
    list_filter = ('name',)


admin.site.register(Recipe, RecipeAdmin)
