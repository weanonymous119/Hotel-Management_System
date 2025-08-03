from django.urls import path
from gym import views

urlpatterns = [
    path("index/",views.index,name = 'index'),
    path("show_member/",views.show_member,name = "show_member"),
    path("show_member/<gender>",views.show_member_female,name="show_member_female"),
    path("equipment/",views.equipments,name="equipments"),
    path("equipments_show/",views.equipments_show,name="equipment_show"),
    path("show_classes/", views.show_classes, name="show_classes"),
    path("about/", views.about, name="about"),
    path("add_user/",views.user,name = "add_user"),
    path("basic_diet/",views.basic_diet,name = "basic_diet"),
    path("welcome/",views.welcome)

]


