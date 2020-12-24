from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    data = {
        "name": "Faisal",
        "city" : "Karachi"
    }
    return render(request , "index.html" , data)

def contact(request):
    return render(request , "contact.html")

def about(request):
    text_dj = request.GET.get("text")
    print(text_dj)
    remove_punc = request.GET.get("removepunc" , "Not Checked")
    uppercase = request.GET.get("uppercase" , "Not Checked")
    charcount = request.GET.get("charcount" , "Not Checked")

    print(remove_punc)

    analyzed_text = ""


    if remove_punc == "on":
        punctuation_list = ". , ? ! ;"
        for char in text_dj:
            if char not in punctuation_list:
                analyzed_text = analyzed_text + char
        punc_text = {
        "purpose": "Remove Punctuation",   
        "text": analyzed_text
    } 

        return render(request , "about.html" , punc_text)
    elif uppercase == "on":
        for char in text_dj:
            analyzed_text = analyzed_text + char.upper()
        punc_text ={
        "purpose": "Uppercase",   
        "text": analyzed_text
    } 

        return render(request , "about.html" , punc_text)
    elif charcount == "on":
        count = 0
        for char in text_dj:
            count = count + 1
        
        punc_text ={
        "purpose": "Charactor Count",   
        "text": count
        }

        return render(request , "about.html" , punc_text)



    else:
        return HttpResponse("Error! Please Check the checkbox")


    



    

def items(request):
    return render(request , "items.html")

def office(request):
    return render(request , "office.html")