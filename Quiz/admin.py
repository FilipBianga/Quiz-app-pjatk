from django.contrib import admin
from .models import *

# Tutaj powinny znaleźć się modele, które będą widoczne w panelu admin
admin.site.register(Quizz)
admin.site.register(Category)
admin.site.register(Answer)
admin.site.register(Question)