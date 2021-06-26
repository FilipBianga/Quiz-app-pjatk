from django.contrib import admin
from .models import *
 
# Tutaj powinny znaleźć się modele, które będą widoczne w panelu admin
admin.site.register(Matematyka)
admin.site.register(Fizyka)
admin.site.register(Historia)
admin.site.register(Informatyka)
