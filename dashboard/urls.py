from django.urls import path
from . import views
urlpatterns =[
    path('',views.notes, name='dashboard'),
    path('add-note',views.add_note, name='add-note'),
    path('note/<int:pk>/',views.edit_note,name='note'),
    path('move-to-trash/<int:pk>/',views.move_to_trash,name='move-to-trash'),
    path('delete-note/<int:pk>/',views.delete_note,name='delete-note'),
    path('trash/',views.notes_trash,name='trash'),
    path('restore-note/<int:pk>/',views.restore_note,name='restore-note')
]
