from django.apps import AppConfig
import os
from django.db.models import Max


def after_startup():

      from model_app.models import User

      if User.objects.count() == 0:
          user = User(username="oleg90", name="Олег",age=36)
          user.save()
#
#           msg = Message(msg="Привет, первый пост на сайте",user=user)
#           msg.save()
#           msg = Message(msg = "Второй пост, классный день",user = user)
#           msg.save()
#           msg = Message(msg ="Третий пост, все хорошо!",user = user)
#           msg.save()
#
#           user = User(username="nikita80", name="Никита", age=46)
#           user.save()
#
#           msg = Message(msg="первый пост", user=user)
#           msg.save()
#           msg = Message(msg="Второй пост, ура", user=user)
#           msg.save()
#           msg = Message(msg="Третий пост, да!", user=user)
#           msg.save()
#
#           user = User(username="vlad85", name="Никита", age=41)
#           user.save()
#
#           msg = Message(msg="первый пост)))", user=user)
#           msg.save()
#           msg = Message(msg="Второй пост)))", user=user)
#           msg.save()
#           msg = Message(msg="Третий пост)))", user=user)
#           msg.save()
#
#       for u in User.objects.all():
#           print(f"{u.username}{u.name}{u.age}")
#
#       for m in Message.objects.all():
#           print(f"{m.msg}{m.dt}")
#
#
#       oleg = User.objects.first()
#       query = Message.objects.filter(user = oleg)
#       for m in query:
#           print(f"{m.msg}{m.dt}")



#     if Person.objects.count() == 0:
#         Person.objects.create(name="John", age=23)
#         Person.objects.create(name="Tom", age=30)
#         Person.objects.create(name="Jane", age=24)
#         Person.objects.create(name="Bob", age=25)
#         Person.objects.create(name="Alice", age=40)
#         Person.objects.create(name="Charlie", age=35)
#         Person.objects.create(name="David", age=28)
#         Person.objects.create(name="Eve", age=29)
#     people = Person.objects.all()
#     print(people.query)
#
#     people = people.filter(name = "Tom")
#     print(people.query)
#
#     people = people.filter(age=30)
#     print(people.query)
#
#     for person in people:
#         print(f"id={person.id} name={person.name} age={person.age}")
#
#     print("-" * 20)
#
#     people = Person.objects.all()
#     for person in people:
#         print(f"id={person.id} name={person.name} age={person.age}")
#
#     if Person.objects.all().filter(name="Oleg").count() == 0:
#         oleg = Person(name="Oleg", age=35)
#         oleg.save()
#
#     print("-"*20)
#
#     people = Person.objects.all()
#     for person in people:
#         print(f"id={person.id} name={person.name} age={person.age}")
#
#     print("-" * 20)
#     people = people[:5]
#     for person in people:
#         print(f"id={person.id} name={person.name} age={person.age}")
#     print("-" * 20)
#     print("-" * 20)
#
#     for person in Person.objects.all().filter(age__gt=30):
#         print(f"id={person.id} name={person.name} age={person.age}")
#     print("-" * 20)
#
#     for person in Person.objects.all().filter(age__gt=30,name__icontains='a'):
#         print(f"id={person.id} name={person.name} age={person.age}")
#     print("-" * 20)
#
#     for person in Person.objects.all().filter(age__lte=30):
#         print(f"id={person.id} name={person.name} age={person.age}")
#     print("-" * 20)
#
#     for person in Person.objects.all().filter(name__in=['Tom','Bob']):
#         print(f"id={person.id} name={person.name} age={person.age}")
#     print("-" * 20)
#
#     for person in Person.objects.all().filter(age__range=(25,30)):
#         print(f"id={person.id} name={person.name} age={person.age}")
#     print("-" * 20)
#
#
#     tom = Person.objects.filter(name__iexact = 'Tom').get()
#     tom.name = 'tom'
#     tom.save()
#
#     print("-" * 20)
#     query = Person.objects.filter(name__iexact = 'Tom')
#     query = query | Person.objects.filter(name__iexact = 'Bob')
#     for person in query:
#         print(f"id={person.id} name={person.name} age={person.age}")
#     print("-" * 20)
#
# def after_startup1():
#     from model_app.models import Сar_brand
#     Сar_brand.objects.all().delete()
#
#     if Сar_brand.objects.count() == 0:
#         Сar_brand.objects.create(name='Infiniti', price=3000000)
#         Сar_brand.objects.create(name='Lada', price=750000)
#         Сar_brand.objects.create(name='Hyundai', price=1500000)
#         Сar_brand.objects.create(name='BMW', price=4000000)
#         Сar_brand.objects.create(name='UAZ', price=1500000)
#         Сar_brand.objects.create(name='Haval', price=1350000)
#         Сar_brand.objects.create(name='Kia Rio', price=850000)
#         Сar_brand.objects.create(name='Toyota RAV4', price=2450000)
#         Сar_brand.objects.create(name='Toyota Corolla ', price=4000000)
#         Сar_brand.objects.create(name='Nissan Cube ', price=250000)
#     cars = Сar_brand.objects.all()
#     for car in cars:
#         print(f"id={car.id} name={car.name} price={car.price}")
#
#     print("-" * 50)
# # увеличить цену третьей машины на 100 000
#     obj = Сar_brand.objects.all()[2]
#     obj.price += 100000
#     obj.save()
# # удалить вторую машину
#     Сar_brand.objects.all()[1].delete()
# # удалить самую дорогую машину
#     max_price = Сar_brand.objects.aggregate(Max('price'))['price__max']
#     Сar_brand.objects.filter(price = max_price)[0].delete()
#
# # поменять имя последней машины
#     ob = Сar_brand.objects.all()[7]
#     ob.name = "Sam"
#     ob.save()
#
#     cars = Сar_brand.objects.all()
#     for car in cars:
#         print(f"id={car.id} name={car.name} price={car.price}")
#
#     print("-" * 50)
# # вывести машины и стоимости с маркой toyota вне зависимости от регистра
#     query1 = Сar_brand.objects.filter(name__icontains='Toyota')
#     for car in query1:
#         print(f"id={car.id} name={car.name} age={car.price}")
#     print("-" * 20)
# # вывести машины и стоимости у которых цена больше 500000
#     for car in Сar_brand.objects.all().filter(price__gt=500000):
#         print(f"id={car.id} name={car.name} age={car.price}")
#     print("-" * 20)
# # все уникальные марки машин
#     for car in Сar_brand.objects.all().distinct():
#         print(f"id={car.id} name={car.name} age={car.price}")
#     print("-" * 20)
# # вывести машины марка начинается с Т или цена меьше 500000
#     query1 = Сar_brand.objects.filter(name__istartswith='T')
#     query2 = Сar_brand.objects.filter(price__lt=500000)
#     for car in query1 | query2:
#         print(f"id={car.id} name={car.name} age={car.price}")
#     print("-" * 20)
#



class ModelAppConfig(AppConfig):
    name = 'model_app'
    def ready(self):
        if os.environ.get('RUN_MAIN') or not os.environ.get('DJANGO_SETTINGS_MODULE'):
            after_startup()


#создать Модель,  Марка машины - Цена
#вначале удалить все что есть
#создать 10 машин

#увеличить цену третьей машины на 100 000
#удалить вторую машину
#удалить самую дорогую машину
#поменять имя последней машины


# вывести машины и стоимости с маркой toyota вне зависимости от регистра
# вывести машины и стоимости у которых цена больше 500000
# все уникальные марки машин
# вывести машины марка начинается с Т или цена меьше 500000