# Create your views here.
from django import forms
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView, CreateView

from recipes.models import Recipe, Ingredient, Direction

visible_field_list = ['title', 'description', 'image', 'ingredients', 'directions']


class RecipeCreate(CreateView):
    model = Recipe
    fields = visible_field_list


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = visible_field_list

    def __init__(self, request, *args, **kwargs):
        self.request = request
        super(RecipeForm, self).__init__(*args, **kwargs)


class RecipeUpdate(UpdateView):
    model = Recipe
    form_class = RecipeForm
    template_name_suffix = '_update_form'

    def get_form_kwargs(self):
        kwargs = super(RecipeUpdate, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def get_context_data(self, **kwargs):
        context = super(RecipeUpdate, self).get_context_data(**kwargs)
        context['ingredients'] = Ingredient.objects.all()
        context['directions'] = Direction.objects.all()
        return context


class RecipeDelete(DeleteView):
    model = Recipe
    success_url = reverse_lazy('recipe-list')
