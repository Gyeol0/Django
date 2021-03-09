from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('DTL/', views.DTL, name='DTL'),
    path('question/', views.question, name='question'),
    path('answer/', views.answer, name='answer'),
    path('lotto/', views.lotto, name='lotto'),
    path('dinner/<str:menu>/<int:people>/', views.dinner, name='dinner'),
]

# {% url pages:index %}
# 이렇게 명시해줄 것임