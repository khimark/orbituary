
from django.shortcuts import render
from django.db import connection

def view_obituaries(request):
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM obituaries")
            obituaries = cursor.fetchall()
            
            # Pagination
            paginator = Paginator(obituaries, 10)  # Show 10 obituaries per page
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            
            return render(request, 'view_obituaries.html', {'page_obj': page_obj})
    
    except Exception as e:
        return HttpResponse("Error retrieving obituaries: " + str(e))