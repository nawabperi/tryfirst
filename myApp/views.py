from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Students

# Create your views here.
def entry(request):
    student_details=get_object_or_404(Students)
    return render(request, 'myApp/stuEntry.html', {'student_details': student_details})





