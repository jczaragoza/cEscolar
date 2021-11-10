from django.urls import path
from core.erp.views.category.views import *

app_name = 'erp'

urlpatterns = [
    path('category/list/', CategoriaListView.as_view(), name='category_list'),
]
