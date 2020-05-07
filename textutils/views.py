#I have created this file
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html')


def aboutus(request):
    return render(request, 'aboutus.html')


def aboutpage(request):
    a = request.POST.get('text' , 'default')
    remove_punc = request.POST.get('punc','off')
    capital = request.POST.get('fullcaps','off')
    nlr = request.POST.get('newlineremover','off')
    esr = request.POST.get('extraspaceremover','off')

    if remove_punc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in a:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {"purpose": "Remove punctuations",
                "analyzed_text": analyzed}
        a = analyzed

    if capital == "on":
        analyzed = ""
        for char in a:
            analyzed = analyzed + char.upper()
        params = {"purpose": "Changed into capital",
                  "analyzed_text": analyzed}
        a = analyzed

    if esr == "on":
        analyzed = ""
        for index, char in enumerate(a):
            if not (a[index] == " " and a[index + 1] == " "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        a = analyzed

    if nlr == "on":
        analyzed = ""
        for char in a:
            if char!="\n" and char!="\r":
                analyzed = analyzed + char
        params = {"purpose": "New line removed",
                  "analyzed_text": analyzed}



    if remove_punc != "on" and capital != "on" and nlr != "on" and esr != "on":
        return HttpResponse("<h1>Please select any operation!!!</h1>")


    return render(request, 'analyze.html', params)
