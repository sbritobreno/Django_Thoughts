from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from ThoughtsApp.models import Thoughts


class IndexView(generic.ListView):
    template_name = 'ThoughtsApp/index.html'
    context_object_name = 'thoughts_list'

    def get_queryset(self):
        return Thoughts.objects.all().order_by('-pub_date')


class MyThoughtsView(generic.ListView):
    model = Thoughts
    template_name = 'ThoughtsApp/myThoughts.html'
    context_object_name = 'thoughts_list'

    def get_queryset(self):
        return Thoughts.objects.all().order_by('-pub_date')


class AddThoughtView(generic.TemplateView):
    model = Thoughts
    template_name = 'ThoughtsApp/AddThought.html'


class EditThoughtView(generic.DetailView):
    model = Thoughts
    template_name = 'ThoughtsApp/EditThought.html'


def add(request):
    userid = request.user
    phrase = request.POST['your_thought']
    pub_date = timezone.now()

    if not phrase or phrase.isspace():
        return render(request, 'ThoughtsApp/addThought.html',
                      {'error_message': "Phrase cannot be empty"})

    thought = Thoughts(user=userid, thought_text=phrase, pub_date=pub_date)
    thought.save()

    return HttpResponseRedirect(reverse('ThoughtsApp:mythoughts'))


def edit(response, thought_id):
    return HttpResponseRedirect(reverse('ThoughtsApp:mythoughts'))


def remove(response, thought_id):
    return HttpResponseRedirect(reverse('ThoughtsApp:mythoughts'))