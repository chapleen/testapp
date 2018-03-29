from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^new-store', views.newStore),
    url(r'^new-product', views.newProduct),
    url(r'^export-xlsx', views.index),
    url(r'^edit-in-excel', views.index)
]