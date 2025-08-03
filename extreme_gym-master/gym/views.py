from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Member,Payment,DietChart,Instructor,Equipments,Basic_diet
from .forms import User_form

def index (request):
    return render(request,"gym/home.html")

def show_member(request):

    return render(request,"gym/mem.html")
def show_member_female(request,gender):
    if(gender=="female"):
        members = Member.objects.raw("Select * from gym_member where gender='female'")
    elif gender=="male":
        members = Member.objects.raw("Select * from gym_member where gender='male'")
    elif gender == "instructor":
        members = Instructor.objects.raw("Select * from gym_instructor")
    context_dict = {"all_members":members}

    return render(request,"gym/mem.html",context = context_dict)

def equipments(request):

    return render(request,"gym/faci.html")
def welcome(request):
    return render(request,"gym/welcome.html")
def equipments_show(request):
    equipment = Equipments.objects.raw("Select * from gym_equipments")
    context_dict = {"equipments":equipment}

    return render(request,"gym/faci.html", context = context_dict)


def  basic_diet(request):
    basic_diet =  Basic_diet.objects.raw("Select * from gym_basic_diet")
    context_dict = {"basic_diet": basic_diet}

    return render(request,"gym/faci.html", context = context_dict)

def show_classes(request):

    return render(request,"gym/classes.html")

def about(request):

    return render(request,"gym/about.html")

def user(request):

    print(request.POST)
    if request.method=="POST":
        form = User_form(request.POST)
        if form.is_valid():
            member = Member()
            member.first_name = form.cleaned_data["first_name"]
            member.last_name = form.cleaned_data["last_name"]
            member.gender = form.cleaned_data["gender"]
            member.age  = form.cleaned_data["age"]
            member.joining_date = form.cleaned_data["joining_date"]
            member.contact_number = form.cleaned_data["contact_number"]
            print(member.contact_number)
            member.save()
            return HttpResponseRedirect("/gym/welcome")
    else:
        form=User_form()
    return render(request,"gym/from.html",{"form":form})