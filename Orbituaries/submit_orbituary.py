
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.db import connection

def submit_obituary(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        dob = request.POST.get('dob')
        dod = request.POST.get('dod')
        content = request.POST.get('content')
        author = request.POST.get('author')

        try:
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO obituaries (name, dob, dod, content, author) VALUES (%s, %s, %s, %s, %s)", 
                               (name, dob, dod, content, author))
                connection.commit()
                
                return HttpResponse("Obituary submitted successfully!")
        
        except Exception as e:
            return HttpResponse("Error submitting obituary: " + str(e))
    
    else:
        return HttpResponse("Invalid request method")