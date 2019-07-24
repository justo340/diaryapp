from entries import views
from django.urls import path
from entries.views import EntryListView

urlpatterns = [
    path('', EntryListView.as_view(), name='home'),
    path('add/', views.add, name='add'),
    # hear  the name  is what is executed
    # when the link is used in the templates
]
