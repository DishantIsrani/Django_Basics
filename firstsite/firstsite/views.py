from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
    

def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'Off')
    FullCaps = request.POST.get('FullCaps', 'Off')
    newlineremover = request.POST.get('newlineremover', 'Off')

    if removepunc == "on":
        punctuations = '''!()-{}[];:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose':'Remove punctutation', 'analyzed_text':analyzed}
        djtext = analyzed

    
    if(FullCaps == 'on'):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose':'Changed to uppercase', 'analyzed_text':analyzed}
        djtext = analyzed


    if(newlineremover=='on'):
        analyzed = ""
        for char in djtext:
            if char !="\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose':'New line removed', 'analyzed_text':analyzed}


    if(removepunc != 'on' and newlineremover!= 'on' and FullCaps=='on'):
        return HttpResponse("Please select the correct operation and try again")

    return render(request, 'analyze.html', params)