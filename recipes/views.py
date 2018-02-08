# Create your views here.
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView, CreateView

from recipes.models import Recipe, Ingredient, Direction

visible_field_list = ['title', 'description', 'image', 'ingredients', 'directions']


class SignUp(CreateView):
    model = User
    success_url = reverse_lazy('recipe-list')
    fields = ['username', 'email', 'password']

    def form_valid(self, form):
        valid = super(SignUp, self).form_valid(form)
        username, password = form.cleaned_data.get('username'), form.cleaned_data.get('password')
        user = User.objects.get(username=username)
        user.set_password(password)
        user.save()
        new_user = authenticate(username=username, password=password)
        login(self.request, new_user)
        return valid


class RecipeCreate(CreateView):
    model = Recipe
    fields = visible_field_list


class RecipeUpdate(UpdateView):
    model = Recipe
    fields = visible_field_list
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
