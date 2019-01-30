from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request,'homepage.html')

def count(request):
    ft = request.GET['fulltext']
    wordlist = ft.split()
    worddictionary = {}
    for word in wordlist:
        if word in worddictionary:
            worddictionary[word] += 1
        else:
            worddictionary[word] = 1
    sortedwordlist = sorted(worddictionary.items(), key=operator.itemgetter(1))
    return render(request,'count.html',{'fulltext':ft,'textlength':len(wordlist),'sortedwordlist':sortedwordlist})

def about(request):
    return render(request,'about.html')
