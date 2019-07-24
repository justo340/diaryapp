from django.shortcuts import render, redirect
from entries.models import Entry
from entries.forms import EntryForm
from django.views.generic import ListView


class EntryListView(ListView):
    model = Entry
    context_object_name = 'entries'
    ordering = ['-date_posted']
    template_name = 'entries/index.html'


def add(request):
    if request.method == 'POST':
        # checks if the  method is a post request -is posting something
        form = EntryForm(request.POST)
        if form.is_valid():
            form.save()   # only works if you used EntryForm
            return redirect('home')
            # the name that was given to the  url of index
    else:
        form = EntryForm()   # checks  if the method is a get method
    context = {'form': form}
    return render(request, 'entries/add.html', context)
