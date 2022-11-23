from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from ThoughtsApp.models import Thoughts


class IndexView(generic.ListView):
    template_name = 'ThoughtsApp/index.html'
    context_object_name = 'thoughts_list'

    # Returns all thoughts from the database ordering by date(Newest)
    def get_queryset(self):
        return Thoughts.objects.all().order_by('-pub_date')


class MyThoughtsView(generic.ListView):
    model = Thoughts
    template_name = 'ThoughtsApp/myThoughts.html'
    context_object_name = 'thoughts_list'

    # Returns all thoughts from the database ordering by date(Newest)
    # Reads data from database (CRUD):Read
    def get_queryset(self):
        return Thoughts.objects.all().order_by('-pub_date')


class AddThoughtView(generic.TemplateView):
    model = Thoughts
    template_name = 'ThoughtsApp/AddThought.html'


class EditThoughtView(generic.DetailView):
    model = Thoughts
    template_name = 'ThoughtsApp/EditThought.html'


# Add new thought to the database
# Create data in the database (CRUD):Create
def add(request):
    # Gets user and phrase from request
    userid = request.user
    phrase = request.POST['your_thought']
    pub_date = timezone.now()

    if not phrase or phrase.isspace():
        return render(request, 'ThoughtsApp/addThought.html',
                      {'error_message': "Phrase cannot be empty"})

    # Add thought to the database
    thought = Thoughts(user=userid, thought_text=phrase, pub_date=pub_date)
    thought.save()

    return HttpResponseRedirect(reverse('ThoughtsApp:mythoughts'))


# Edit a thought in the database
# Edit data in the database (CRUD):Update
def edit(request, thought_id):
    # Gets phrase from the post request
    phrase = request.POST['edit_thought']

    if not phrase or phrase.isspace():
        return HttpResponseRedirect(reverse('ThoughtsApp:mythoughts'))

    # Gets thought to be updated and update it
    thought = Thoughts.objects.get(pk=thought_id)
    thought.thought_text = phrase
    thought.save()

    return HttpResponseRedirect(reverse('ThoughtsApp:mythoughts'))


# Remove a thought from the database
# Remove data from the database (CRUD):Delete
def remove(request, thought_id):
    # Gets thought by id and delete it
    thought = Thoughts.objects.get(pk=thought_id)
    thought.delete()
    return HttpResponseRedirect(reverse('ThoughtsApp:mythoughts'))
