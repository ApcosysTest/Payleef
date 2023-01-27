from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def login(request):
    return render(request,'login.html')

def homepage(request):
    return render(request,'homepage.html')

def companySetup(request):
    return render(request,'companySetup.html')

def companyInformation(request):
    return render(request,'companyInformation.html')

def addEmployee(request):
    return render(request,'addEmployee.html')

def employeeInformation(request):
    return render(request,'employeeInformation.html')

def salary(request):
    return render(request,'salary.html')

def salaryReport(request):
    return render(request,'salaryReport.html')

def payslipDistribution(request):
    return render(request,'payslipDistribution.html')