from django.urls import path
from core.erp.views.category.views import *
from core.erp.views.dashboard.views import *
from core.erp.views.cursos.views import *

app_name = 'erp'

urlpatterns = [
    path('category/list/', CategoriaListView.as_view(), name='category_list'),
    path('category/add/', CategoriaCreateView.as_view(), name='category_create'),
    path('category/edit/<int:pk>/', CategoriaUpdateView.as_view(), name='category_update'),
    path('category/delete/<int:pk>/', CategoriaDeleteView.as_view(), name='category_delete'),
    path('category/form/', CategoriaFormView.as_view(), name='category_form'),
    # Cursos
    path('curso/list/', CursoListView.as_view(), name='curso_list'),
    path('curso/add/', CursoCreateView.as_view(), name='curso_create'),
    path('curso/update/<int:pk>/', CursoUpdateView.as_view(), name='curso_update'),
    path('curso/delete/<int:pk>/', CursoDeleteView.as_view(), name='curso_delete'),
    #Home
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
]
