from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from mytodoapp.models import ToDo


class ToDoListView(generic.ListView):
    model = ToDo


class ToDoDetailView(generic.DetailView):
    model = ToDo


class ToDoCreateView(generic.CreateView):
    model = ToDo
    fields = ["name", "description"]


class ToDoDeleteView(generic.DeleteView):
    model = ToDo
    success_url = reverse_lazy("todo-list")


class ToDoUpdateView(generic.UpdateView):
    model = ToDo
    fields = ["status"]
    template_name_suffix = "_update_form"
