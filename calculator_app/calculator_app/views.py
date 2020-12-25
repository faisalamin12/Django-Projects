from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request , "home.html")


def calculate(request):
     num1_input = request.GET.get("num1")
     op = request.GET.get("operator")
     num2_input = request.GET.get("num2")
     result = num1_input + num2_input

     inputs = {
        "num1": num1_input,
        "num2": num2_input,
        "operator": op,
        "Result":result
    }

     return render(request , "home.html", inputs)


