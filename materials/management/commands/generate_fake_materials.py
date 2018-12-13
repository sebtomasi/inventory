import datetime

from django.core.management.base import BaseCommand, CommandError
import random
from materials.models import Category, Hardware


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        ordinateur, create = Category.objects.get_or_create(name="ordinateur")
        tablette, create = Category.objects.get_or_create(name="tablette")
        imprimante, create = Category.objects.get_or_create(name="imprimante")
        serveur, create = Category.objects.get_or_create(name="serveur")
        borne, create = Category.objects.get_or_create(name="borne")
        category_list = [ordinateur, tablette, imprimante, serveur, borne]



        for i in range(100):
            month = random.randint(1,12)
            day = random.randint(1,28)
            hour = random.randint(8,18)
            year = random.randint(2007,2019)
            new_buy_date = datetime.datetime(year, month, day, hour)
            new_category = random.choice(category_list)
            new_price = random.randint(100,2000)
            Hardware.objects.create(category=new_category, buy_date=new_buy_date, price=new_price)

        print("100 new hardwares created")
