from django.shortcuts import render

from thinglist.models import *
# Create your views here.
def index(request):
  category_list = Category.objects.order_by('-name')
  print category_list
  context = {'lol': "aaaa", 'category_list': category_list}
  return render(request, 'blist/home.html', context)

def category(request, category_name):
  category = Category.objects.get(name=category_name)
  item_list = Item.objects.get(category=category)
  context = {'name':category,'item_list': item_list}
  return render(request, 'blist/categ.html', context)

def item(request, item_name):
  item = Item.objects.get(name=item_name)
  notes_list = Note.objects.get(item=item)
  context = {'name':item, 'note_list': note_list}
  return render(request, 'blist/item.html', context)

def note(request, note_id):
  note = Note.objects.get(id=note_id) #i may need to use an id here
  context = {'item': note.item, 'note': note} # need to add in rating
  return render(request, 'blist/detail.html', context)
