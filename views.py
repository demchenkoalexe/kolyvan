from django.shortcuts import render #для вывода информации

# Create your views here.
def show(request):
   return render(request, 'kolMag/index.html')

def showListProducts(request):
   context = {
      'products': 'Большая колыванская ваза',
      'description': 'Большая колыванская ваза (иногда называемая в популярных источниках «царицей ваз») из зелёно-волнистой яшмы — произведение камнерезного искусства, экспонирующееся в государственном Эрмитаже. Вес каменного изделия составляет 19 тонн. Высота вазы с пьедесталом — 2,57 м, большой диаметр составляет 5,04 м, а малый — 3,22 м. Это самая большая ваза в мире.',
      'image1': 'kolMag/image/bd/stoneproduct/Revnev-Jaspis-Vase_St._Petersburg_Eremitage.JPG'
   }
   return render(request, 'kolMag/listProducts.html', context)

def admin(request):
   return render(request, 'kolMag/admin.html')