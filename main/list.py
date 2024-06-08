# list.py

from django.shortcuts import render
from django.http import HttpResponse

# import pdfkit

# def person_list(request):
#     persons = Person.objects.all()

#     if request.method == 'POST':
#         person_id = request.POST.get('person_id')
#         person = Person.objects.get(pk=person_id)

#         html = f"<h1>{person.name}</h1><p>Yaş: {person.age}</p><p>Şəhər: {person.city}</p>"

#         pdf = pdfkit.from_string(html, False)

#         response = HttpResponse(pdf, content_type='application/pdf')
#         response['Content-Disposition'] = f'attachment; filename="{person.name}.pdf"'
#         return response

#     return render(request, 'person_list.html', {'persons': persons})
