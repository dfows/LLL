from django.shortcuts import render, redirect

from thinglist.models import *
import urllib2

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

def item(request, category_name, item_name):
  print 'item!',item_name
  item = Item.objects.get(name=item_name)
  note_list = Note.objects.filter(item=item)
  context = {'name':item.category, 'item': item.name, 'note_list': note_list}
  #this feels a little dirty? should i set up a blank msg or something
  if len(note_list) == 0:
    context['msg'] = "No Notes Yet"
  return render(request, 'blist/item.html', context)

def note(request, note_id):
  note = Note.objects.get(id=note_id)
  context = {'item': note.item.name, 'note': note} # need to add in rating
  return render(request, 'blist/detail.html', context)

# inputting
def addCategory(request):
  if request.method == 'POST':
    cname = request.POST['cname']  
    if cname == '':
      msg = {'error': 'error.  please enter text in the field'}
      return render(request, 'blist/addCateg.html', msg)
    else:
      c = Category(name=cname)
      c.save()
      #need to show user a message that says "category added"
      return redirect('index') 
  else:
    return render(request, 'blist/addCateg.html')

def addItem(request, category_name):
  if request.method == 'POST':
    n = request.POST['iname']
    if n == '':
      msg = {'error': 'error.  please enter text in the field'}
      return render(request, 'blist/addItem.html', msg)
    else:
      c = Category.objects.get(name=category_name)
      u = urllib2.quote(n)
      i = Item(name=n,url_name=u,category=c)
      i.save()
      return redirect('category', category_name = category_name)
  else:
    context = {'category_name':category_name}
    return render(request, 'blist/addItem.html', context)

def addNote(request, category_name, item_name):
  print category_name
  print item_name
  if request.method == 'POST':
    r = request.POST['rating']
    nn = request.POST['content']
    if r == '':
      msg = {'error': 'error.  please enter a rating'}
      return render(request, 'blist/addNote.html', msg)
    else:
      i = Item.objects.get(name=item_name);
      new_note = Note(rating=r,content=nn,item=i)
      new_note.save()
      return redirect('item', category_name, item_name)
  else:
    context = {'category_name':category_name,'item_name':item_name}
    return render(request, 'blist/addNote.html', context)  
