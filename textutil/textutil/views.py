# i have created this file
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')
    # return HttpResponse("Hello")


def analyze(request):
    # get the text
    djtext = request.POST.get('text', 'default')
    print(djtext)
    # check checkbox value
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    charcount = request.POST.get('charcount', 'off')

    # analyze the text
    # if user wants to remove punctuation
    if removepunc == 'on':
        punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punc:
                analyzed = ''.join((analyzed, char))
        params = {'analyze_text': analyzed, 'charcount': charcount}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    # if user wants the text in uppercase
    if fullcaps == "on":
        analyzed = djtext.upper()
        params = {'analyze_text': analyzed, 'charcount': charcount}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    # \n means new line. It means that the cursor must go to the next line. \r means carriage return. It means that
    # the cursor should go back to the beginning of the line.
    if newlineremover == 'on':
        analyzed = ""
        for char in djtext:
            if char != '\n' and char != '\r':
                analyzed = ''.join((analyzed, char))
        params = {'analyze_text': analyzed, 'charcount': charcount}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    # if user wants character count
    if charcount == 'on':
        analyzed = djtext
        params = {'analyze_text': analyzed,
                  'charcount': charcount,
                  'char_count': len(analyzed)}
        # return render(request, 'analyze.html', params)

    # if nothing has selected
    if removepunc != "on" and fullcaps != "on" and newlineremover != "on" and charcount != "on":
        return HttpResponse("Nothing has selected. Error")

    return render(request, 'analyze.html', params)


def about(request):
    return render(request, 'about.html')
