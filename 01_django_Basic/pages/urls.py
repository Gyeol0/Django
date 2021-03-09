from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('index/', views.index, name='index'),
]

# {% url pages:index %}
# 이렇게 명시해줄 것임