from django.urls import path    
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    # path('login/',views.login_user,name='login'),
    path('logout/',views.logout_user,name='logout'),
    path('signUp/',views.register_user,name='signUp'),
    path('add_record/',views.add_record,name='add_record'),
    path('edit_record/<int:pk>',views.edit_record,name='edit_record'),
    path('delete_record/<int:pk>',views.delete_record,name='delete_record'),
]
