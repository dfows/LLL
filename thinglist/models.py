from django.db import models

# Create your models here.
class Category(models.Model):
  # category
  name = models.CharField(max_length="20",primary_key=True)
  def __unicode__(self):
    return self.name

class Item(models.Model):
  # an item
  name = models.CharField(max_length="100",primary_key=True)
  category = models.ForeignKey(Category)
  def __unicode__(self):
    return self.name
  def __str__(self):
    return self.name

class Note(models.Model):
  # these are feelings u had about some item
  id = models.AutoField(primary_key=True)
  date = models.DateTimeField(auto_now=True)
  content = models.TextField(blank=True)
  item = models.ForeignKey(Item)
  def __unicode__(self):
    return self.date.__str__()+" : "+self.item.__str__()

