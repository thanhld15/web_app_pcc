"""Defines URL patterns for learning_logs"""

from django.urls import path

from . import views

urlpatterns = [
    # Home page
    path("", views.index, name="index"),
    path("topics/", views.topics, name="topics"),
    # Detail page for each topic
    path(r"^topics/(?P<topic_id>\d+)/$", views.topic, name="topic"),
    # Page for adding new topic
    path("new_topic/", views.new_topic, name="new_topic"),
    # Page for adding new entry
    path(r"^new_entry/(?P<topic_id>\d+)/$", views.new_entry, name='new_entry'),
    # Page for editing an entry
    path(r"^edit_entry/(?P<entry_id>\d+)/$", views.edit_entry, 
        name='edit_entry'),
    
]
