from django.shortcuts import render
from django.http import HttpResponse
from .models import TestCase

def index(request):
    test_cases_date_time_wise_list = TestCase.objects.all()
    context = {'test_cases_date_time_wise_list':test_cases_date_time_wise_list}
    return render(request, 'testprj/index.html', context)# Create your views here.


