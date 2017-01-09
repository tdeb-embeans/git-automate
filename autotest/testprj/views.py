from django.shortcuts import render
from django.http import HttpResponse
from .models import TestCase

def index(request):
    test_cases_date_time_wise_list = TestCase.objects.all()
    countPassCases = (TestCase.objects.filter(result = 'pass')).__len__()
    print ("TD:countPassCases", countPassCases)
    countFailCases = (TestCase.objects.filter(result = 'fail')).__len__()
 
    countNECases = (TestCase.objects.filter(result = 'NE')).__len__()

    countTotalCases = countPassCases + countFailCases + countNECases
    context = {'countPassCases': countPassCases,
	       'countFailCases':countFailCases,
		'countNECases':countNECases,
		'countTotalCases':countTotalCases}
    

    return render(request, 'testprj/index.html', context)# Create your views here.





