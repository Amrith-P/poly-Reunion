from django.urls import path
from . import views
from class_room.views import *

app_name = 'class_room'

urlpatterns = [ 
    path('', list_benches, name='index'),
    path('edit_bench11/<int:bench_id>/', views.edit_bench11, name='edit_bench11'),
    path('edit_bench12/<int:bench_id>/', views.edit_bench12, name='edit_bench12'),
    path('edit_bench13/<int:bench_id>/', views.edit_bench13, name='edit_bench13'),
    path('edit_bench14/<int:bench_id>/', views.edit_bench14, name='edit_bench14'),
    path('edit_bench15/<int:bench_id>/', views.edit_bench15, name='edit_bench15'),
    path('edit_bench21/<int:bench_id>/', views.edit_bench21, name='edit_bench21'),
    path('edit_bench22/<int:bench_id>/', views.edit_bench22, name='edit_bench22'),
    path('edit_bench23/<int:bench_id>/', views.edit_bench23, name='edit_bench23'),
    path('edit_bench24/<int:bench_id>/', views.edit_bench24, name='edit_bench24'),
    path('edit_bench25/<int:bench_id>/', views.edit_bench25, name='edit_bench25'),
    path('edit_bench26/<int:bench_id>/', views.edit_bench26, name='edit_bench26'),
    path('edit_bench31/<int:bench_id>/', views.edit_bench31, name='edit_bench31'),
    path('edit_bench32/<int:bench_id>/', views.edit_bench32, name='edit_bench32'),
    path('edit_bench33/<int:bench_id>/', views.edit_bench33, name='edit_bench33'),
    path('edit_bench34/<int:bench_id>/', views.edit_bench34, name='edit_bench34'),
    path('edit_bench35/<int:bench_id>/', views.edit_bench35, name='edit_bench35'),
    path('edit_bench41/<int:bench_id>/', views.edit_bench41, name='edit_bench41'),
    path('edit_bench42/<int:bench_id>/', views.edit_bench42, name='edit_bench42'),
    path('edit_bench43/<int:bench_id>/', views.edit_bench43, name='edit_bench43'),
    path('edit_bench44/<int:bench_id>/', views.edit_bench44, name='edit_bench44'),
    path('edit_bench45/<int:bench_id>/', views.edit_bench45, name='edit_bench45'),

    
    
]