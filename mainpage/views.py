try:
    import cString as StringIO
except ImportError:
    import StringIO
from django.shortcuts import render
from django.http import HttpResponse
from xlsxwriter

from .forms import *

def index(request):
    stores = Store.objects.all()
    return render(request, "mainpage/index.html", locals())

def newStore(request):
    form = StoreForm(request.POST or None)
    formType = "store"
    dataSaved = False
    if request.method == "POST" and form.is_valid():
        form.save()
        form = StoreForm()
        dataSaved = True
    return render(request, "mainpage/form.html", locals())

def newProduct(request):
    form = ProdutcForm(request.POST or None)
    formType = "product"
    dataSaved = False
    if request.method == "POST" and form.is_valid():
        form.save()
        form = ProdutcForm()
        dataSaved = True
    return render(request, "mainpage/form.html", locals())

def export_xlsx(request):
