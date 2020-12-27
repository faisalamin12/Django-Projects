from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request , "home.html")


def calculate(request):
     num1_input = request.GET.get("num1")
     op = request.GET.get("operator")
     num2_input = request.GET.get("num2")


     if op == "+":
         result = int(num1_input) + int(num2_input)

         data = {
             "Result": result
         }

         return render(request , "home.html",data)
    
    
     elif op == "-":
        result = int(num1_input) - int(num2_input)

        data = {
             "Result": result
         }

        return render(request , "home.html",data)
        

     elif op == "*":
        result = int(num1_input) * int(num2_input)

        data = {
             "Result": result
         }

        return render(request , "home.html",data)
   
   
     elif op == "/":
        result = int(num1_input) / int(num2_input)

        data = {
             "Result": result
         }

        return render(request , "home.html",data)
        






     


