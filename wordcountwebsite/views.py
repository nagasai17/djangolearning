from django.http import HttpResponse as hp
from django.shortcuts import render

from collections import Counter
#request,home.html

def hello(request):
	return render(request,'home.html',{'hithere' : 'nagasai'})
def count(request):
	fulltext=request.GET['fulltext']
	wordssplit=fulltext.split()
	c=Counter(wordssplit)
	c1=list((c.most_common()[0]))
	
	return render(request,'count.html',{'number_of_words':len(wordssplit),'things_to_displayword' : c1[0],'things_to_displaycount' : c1[1]})
#Templates are used for typing html in httpresponse 	

def aboutme(request):
	return render(request,"aboutme.html")
