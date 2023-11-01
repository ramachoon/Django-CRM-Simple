from django.urls import path
from website.views import home,customer_record,delete_record,add_record,update_record


app_name = "website"

urlpatterns = [
    path('home/', home, name="home"),
    path('record/<int:pk>',customer_record, name="customer"),
    path('delete_record/<int:pk>',delete_record, name="delete_record"),
    path('add_record/',add_record,name="add_record"),
    path('update_record/<int:pk>',update_record,name="update_record")
]