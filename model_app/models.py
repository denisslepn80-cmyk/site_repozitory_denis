from django.db import models
from django import forms
from django.forms import ModelForm



class Category (models.Model):

    name = models.CharField(max_length=50, verbose_name="Название категории")
    def __str__(self):
        return self.name
class SourceType (models.Model):

    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
class Source (models.Model):

    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    sourceType = models.ForeignKey(SourceType, on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.name

class Type (models.Model):

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Product (models.Model):

    name = models.CharField(max_length=50, blank=True)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    quantity = models.FloatField()
    price = models.FloatField()
    def __str__(self):
        return str(self.type) +" "+str(self.name)

class ProductSource (models.Model):


    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    source = models.ForeignKey(Source,on_delete=models.CASCADE)






class User (models.Model):

    username = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    age = models.IntegerField()



class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class ProductSourceForm(ModelForm):
    class Meta:
        model = ProductSource
        fields = '__all__'


    # def __str__(self):
    #     return self.name

# class Message(models.Model):
#     msg = models.TextField(max_length=200)
#     dt = models.DateTimeField(auto_now_add=True)
#     user = models.ForeignKey(User,on_delete=models.CASCADE)
#
# class MessageForm(ModelForm):
#     class Meta:
#         model = Message
#         fields = ["msg"]

# class UserForm(ModelForm):
#     class Meta:
#         model = User
#         fields = __all__

# class Сar_brand(models.Model):
#     name = models.CharField(max_length=20)
#     price = models.IntegerField()