from django.contrib import admin
from django.urls import path
from Quiz.views import *
from django.conf import settings
from django.conf.urls.static import static
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', loginPage, name='login'),
    path('home/', home, name='home'),
    path('logout/', logoutPage, name='logout'),
    path('register/', registerPage, name='register'),
    path('categories/', search_categories, name='categories'),
    path('categories/<int:category_id>/quizzes', search_quizzes, name='quizzes'),
    path('quizzes/<int:quizz_id>', get_quizz, name='quizz'),
    path('quizzes/<int:quizz_id>/result', get_results, name='result')

 
]
urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)