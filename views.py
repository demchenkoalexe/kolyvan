from django.shortcuts import render #для вывода информации
from django.db import connection
from django.views.decorators.csrf import csrf_exempt

from .models import *

#ФУНКЦИИ ОБРАЩЕНИЯ К БАЗЕ
#получить конкретное изделие завода
def get_details(id):
	return StoneProduct.objects.raw("select * from stone_product where stone_product.id = %s" % id)

#получить автора изделия
def get_author(id):
	return AuthorProduct.objects.raw("select * from author_product where author_product.id = %s" % id)

#получить id автора изделия
def get_author_name(name):
	return AuthorProduct.objects.raw("select * from author_product where author_product.name='%s'" % name)

#получить камень из которого изготовлено изделие
def get_stone(id):
	return ListStone.objects.raw("select * from list_stone where list_stone.id =%s" % id)

#получить id преобладающего материала
def get_stone_name(name):
	return AuthorProduct.objects.raw("select * from list_stone where list_stone.name='%s'" % name)

#обновление товара
def update_product(id, name, author_id, size_length, size_height, stone_id, possible_price, description, image_file, full_description):
	with connection.cursor() as c:
		c.execute("update stone_product set name='%s', id_author_id='%s', size_length='%s', size_height='%s', id_list_materials_id='%s', possible_price='%s', description='%s', image='%s', full_description='%s' where id=%s" % (name, author_id, size_length, size_height, stone_id, possible_price, description, image_file, full_description, id))

#добавление нового товара
def create_product(name, author_id, size_length, size_height, stone_id, possible_price, description, image_file, full_description):
	with connection.cursor() as c:
		c.execute("insert into stone_product (name, id_author_id, size_length, size_height, id_list_materials_id, possible_price, description, image, full_description) values ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (name, author_id, size_length, size_height, stone_id, possible_price, description, image_file, full_description))





# Create your views here.
def show(request):
	return render(request, 'kolMag/index.html')

def showListProducts(request):
	stoneProduct = StoneProduct.objects.all()
	return render(request, 'kolMag/listProductsView.html', locals())

def admin(request):
	stoneProduct = StoneProduct.objects.all()
	i = 0
	return render(request, 'kolMag/adminView.html', locals())

@csrf_exempt
def product(request): 
	oneProduct = get_details(request.POST['view'])[0]
	author = get_author(request.POST['author'])[0]
	stone = get_stone(request.POST['stone'])[0]
	return render(request, 'kolMag/productView.html', locals())

@csrf_exempt
def editAdmin(request):
	oneProduct = get_details(request.POST['edit'])[0]
	authors = AuthorProduct.objects.all()
	stones = ListStone.objects.all()
	return render(request, 'kolMag/adminEditView.html', locals())

#Сохранение отредактированного продукта
@csrf_exempt
def saveEdit(request):
	authorId = get_author_name(request.POST['inputNameAuthor'])[0]
	stoneId = get_stone_name(request.POST['inputStone'])[0]
	update_product(request.POST['id'], request.POST['inputName'], authorId.id, request.POST['inputLength'], request.POST['inputHeight'], 
		stoneId.id, request.POST['inputPrice'], request.POST['inputDescription'], request.POST['inputFile'], request.POST['inputFullDescription'])

	stoneProduct = StoneProduct.objects.all()
	return render(request, 'kolMag/adminView.html', locals())

def addProduct(request):
	authors = AuthorProduct.objects.all()
	stones = ListStone.objects.all()
	return render(request, 'kolMag/addProductView.html', locals())

#Сохранение добавленого продукта
@csrf_exempt
def saveAdd(request):
	authorId = get_author_name(request.POST['inputNameAuthor'])[0]
	stoneId = get_stone_name(request.POST['inputStone'])[0]
	create_product(request.POST['inputName'], authorId.id, request.POST['inputLength'], request.POST['inputHeight'], 
		stoneId.id, request.POST['inputPrice'], request.POST['inputDescription'], request.POST['inputFile'], request.POST['inputFullDescription'])

	stoneProduct = StoneProduct.objects.all()
	return render(request, 'kolMag/adminView.html', locals())

#Удаление продукта
@csrf_exempt
def delete(request):
	with connection.cursor() as c:
		c.execute("delete from stone_product where id=%s" % (request.GET['id']))

	stoneProduct = StoneProduct.objects.all()
	return render(request, 'kolMag/adminView.html', locals())