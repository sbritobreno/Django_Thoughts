from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic, View
from django.utils import timezone
# from ThoughtsApp.models import Choice, Question


class IndexView(generic.ListView):
    template_name = 'ThoughtsApp/index.html'

    def get_queryset(self):
        """Return the last five published questions."""
        return ''


class MyThoughtsView(generic.TemplateView):
    template_name = 'ThoughtsApp/myThoughts.html'

    def get_queryset(self):
        """Return the last five published questions."""
        return ''
