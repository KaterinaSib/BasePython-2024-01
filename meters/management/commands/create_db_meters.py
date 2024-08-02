from django.core.management.base import BaseCommand
from addresses.models import Address
from meters.models import Category, Meter, MeterData
from users.models import MyUser


class Command(BaseCommand):

    def handle(self, *args, **options):
        user_admin = MyUser.objects.create(
            username="user_admin",
            email="user_admin@mail.com",
            password="admin12345!",
            is_superuser=True,
        )
        address_1 = Address.objects.create(
            street="Мира",
            num_house=2,
            num_room=15,
            user=user_admin,
        )

        address_2 = Address.objects.create(
            street="Ленина",
            num_house=20,
            num_room=5,
            user=user_admin,
        )

        user_bob = MyUser.objects.create_superuser(
            username="Bob",
            email="bob@mail.com",
            password="bob12345!",
        )

        address_bob = Address.objects.create(
            street="Осенняя",
            num_house=2,
            num_room=20,
            user=user_bob,
        )

        gvs = Category.objects.create(
            name="ГВС",
        )

        hvs = Category.objects.create(
            name="ХВС",
        )

        electric = Category.objects.create(
            name="Эл/эн",
        )

        meter_1 = Meter.objects.create(
            address=address_1,
            category=gvs,
            type="Тайпит",
            serial_num=45678,
        )

        data_meter_1 = MeterData.objects.create(
            meter=meter_1,
            data=65,
        )

        meter_2 = Meter.objects.create(
            address=address_2,
            category=hvs,
            type="Тайпит",
            serial_num=54321,
        )

        data_meter_2 = MeterData.objects.create(
            meter=meter_2,
            data=123,
        )

        meter_bob_electric = Meter.objects.create(
            address=address_bob,
            category=electric,
            type="ЭнергоМера",
            serial_num=13542,
        )

        data_meter_bob_electric = MeterData.objects.create(
            meter=meter_bob_electric,
            data=12,
        )

        meter_bob_hvs = Meter.objects.create(
            address=address_bob,
            category=hvs,
            type="Бетар",
            serial_num=65432,
        )

        data_meter_bob_hvs = MeterData.objects.create(
            meter=meter_bob_hvs,
            data=15,
        )
