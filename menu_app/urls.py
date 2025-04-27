from django.urls import path
from menu_app.views import draw_menu

app_name = 'menu_app'

urlpatterns = [
    path('<str:menu_name>/', draw_menu, name='draw_menu'),
]