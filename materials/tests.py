from django.contrib.auth.models import Permission
from django.core.management import call_command
from django.test import TestCase, Client
from datetime import datetime
from accounts.models import User
from materials.models import Hardware


class MaterialTestCase(TestCase):
    def setUp(self):
        call_command("generate_fake_materials")
        self.john = User.objects.create(username="JohnDoe",first_name="John",last_name="Doe", email="john.doe@fabdev.fr")
        self.john.set_password("123456")
        self.john.save()


    def test_generate_fake_materials(self):
        self.assertEqual(Hardware.objects.all().count(), 100)


    def test_check_permission_hardware_list(self):
        c = Client()
        c.login(username='JohnDoe', password='123456')
        response = c.get("?start_date=2017-01-01&end_date=2017-02-01")
        self.assertEqual(response.status_code, 403)

    def test_filter_buy_date(self):

        view_hardware_permission = Permission.objects.get(codename="view_hardware")

        self.john.user_permissions.add(view_hardware_permission)

        c = Client()
        c.login(username='JohnDoe', password='123456')
        response = c.get("?start_date=2017-01-01&end_date=2017-10-01")

        for hardware in response.context["object_list"]:
            self.assertGreaterEqual(hardware.buy_date,datetime.strptime("2017-01-01","%Y-%m-%d"))
            self.assertLessEqual(hardware.buy_date,datetime.strptime("2017-10-01","%Y-%m-%d"))