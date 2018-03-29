from django.shortcuts import render
from django.http import HttpResponse
from xlsxwriter import Workbook
import io

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
    output = io.BytesIO()
    workbook = Workbook(output, {'in_memory': True})
    stores_worksheet = workbook.add_worksheet('stores')
    products_worksheet = workbook.add_worksheet('products')


    stores_worksheet.write('A1', 'Name')
    stores_worksheet.write('B1', 'Address')
    for i, store in enumerate(Store.objects.all()):
        stores_worksheet.write(i+1, 0, store.name)
        stores_worksheet.write(i+1, 1, store.address)

    products_worksheet.write('A1', 'Name')
    products_worksheet.write('B1', 'Weight')
    products_worksheet.write('C1', 'Brand')
    products_worksheet.write('D1', 'Price')
    products_worksheet.write('E1', 'Expiration Date')
    dateFormat = workbook.add_format({'num_format': 'dd/mm/yy'})

    for i, product in enumerate(Product.objects.all()):
        products_worksheet.write(i+1, 0, product.name)
        products_worksheet.write(i+1, 1, product.weight)
        products_worksheet.write(i+1, 2, product.brand)
        products_worksheet.write(i+1, 3, product.price)
        products_worksheet.write(i+1, 4, product.expirationDate, dateFormat)

    workbook.close()
    output.seek(0)
    response = HttpResponse(output.read(), content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    response['Content-Disposition'] = "attachment; filename=testapp.xlsx"
    return response
