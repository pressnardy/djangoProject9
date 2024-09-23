import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoProject9.settings')
import django
django.setup()

from clients.forms import ClientForm
from clients.models import Client

# name = "cassim"
# reno = 34856
# pno = 5647
# sd = '29/09/2024'
# ed = '29/10/2024'
# rn = '29/09/2025'
# amount = 100.0000
#
# client = ClientForm(name, reno, pno, sd, ed, rn, amount)
# client.save()

print(Client.objects.all())


