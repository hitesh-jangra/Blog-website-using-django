from django.urls import path
from . import views
urlpatterns= [
   path('',views.home,name='home'),
   path('askquestion/',views.ask_question,name='askquestion'),
   path('<int:id>',views.view_question,name='view_question'),
   path('blogs/',views.blog,name='blogs'),
   path('visitblog/<int:id>/',views.visitblog,name='visitblog'),
]