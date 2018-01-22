from django.contrib import admin

# Register your models here.
from recipes.models import Recipe, Direction, Ingredient


@admin.register(Ingredient)
class IngredientsAdmin(admin.ModelAdmin):
    list_display = ('name',)
    fields = ('name',)


@admin.register(Direction)
class DirectionAdmin(admin.ModelAdmin):
    list_display = ('step',)
    fields = ('step',)


class IngredientsInline(admin.TabularInline):
    model = Recipe.ingredients.through
    extra = 1


class DirectionsInline(admin.TabularInline):
    model = Recipe.directions.through
    extra = 1


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    fields = ('title', 'created_by', 'image', 'description',)
    list_display = ('title', 'created_by', 'created_at')
    exclude = ('created_at',)
    inlines = [
        IngredientsInline,
        DirectionsInline,
    ]
