from django.shortcuts import render

from thinglist.models import *

# Create your views here.
def index(request):
  category_list = Category.objects.order_by('-name')
  context = {'lol': "aaaa", 'category_list': category_list}
  return render(request, 'blist/home.html', context)

def category(request, category_name):
  category = Category.objects.get(name=category_name)
  item_list = Item.objects.filter(category=category)
  context = {'name':category_name,'item_list': item_list}
  return render(request, 'blist/categ.html', context)

def item(request, item_name):
  item = Item.objects.get(name=item_name)
  note_list = Note.objects.filter(item=item)
  #JANKY
  #DOESNET DO SHIT RIGHT NOW CUZ NONE OF MY TEST CASES WITH SPACES CAN PASS THE category SCREEN
  item_name = item_name.replace(' ','-')
  context = {'name':item.category, 'item': item_name, 'note_list': note_list}
  return render(request, 'blist/item.html', context)

def note(request, note_id):
  note = Note.objects.get(id=note_id)
  context = {'item': note.item.name, 'note': note} # need to add in rating
  return render(request, 'blist/detail.html', context)
