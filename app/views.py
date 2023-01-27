from django.shortcuts import render , redirect
from .models import companysetup , Login , employee 
from .forms import companySetupForm , LoginForm , employeeForm 
from django.http import HttpResponse



# Create your views here.
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)  
        username = request.POST['username']
        password = request.POST['password']
         
        try:
            salary = Login.objects.get(username = username,password=password)
            request.session['username'] = username
        except Login.DoesNotExist:
            salary = None


        if salary is not None:
            return redirect('/homepage')                                           
        else:
  
            return render(request,"login.html")

    return render(request,"login.html")

def homepage(request):
    return render(request,'homepage.html')

def companySetup(request):
    if request.method == "POST": 
        form = companySetupForm(request.POST,request.FILES)
        
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/companyInformation')
                # return HttpResponse("done")
            except:  
                print(form.errors)
                pass  
    else:  
        
        form = companySetupForm()  
    return render(request,'companySetup.html',{'form':form})

def companyInformation(request):
    if request.method == 'GET':
            company = companysetup.objects.get()
            print(company)
            # if request.method == "POST":  
            #     form = companySetupForm(request.POST,instance=company)  
            #     if form.is_valid():
            #         try:  
            #             form.save()  
            #             return redirect('/addEmployee')  
                        
            #         except:  
            #             pass  

            # else:
            #     form = companySetupForm()  
        
   
            return render(request,'companyInformation.html',{'company':company})        
    return render(request,"companyInformation.html")

def addEmployee(request):
    if request.method == "POST": 
        form = employeeForm(request.POST)
        
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/searchEmployee')
                # return HttpResponse("done")
            except:  
                print(form.errors)
                pass  
    else:  
        
        form = employeeForm()   
    return render(request,'addEmployee.html',{'form':form})

def searchEmployee(request):
    if request.method == 'POST':
            form = employeeForm(request.POST)  
            emp_code = request.POST['emp_code']
            
            try:
                emp = employee.objects.get(emp_code=emp_code) 
                request.session['emp_code'] = emp_code
                    
            except employee.DoesNotExist:
                emp = None
                             
            if emp is not None:
                return redirect('/employeeDetails')                                           
            else:
                return render(request, 'searchEmployee.html')

    return render(request,"searchEmployee.html")

def employeeDetails(request):
    emp_code = request.POST['emp_code']
    emp = employee.objects.filter(emp_code=emp_code)
    return render(request, 'searchEmployee.html',{'employee' : emp})

def employeeInformation(request, id):  
    emp = employee.objects.get(id=id)  
    return render(request,'employeeInformation.html', {'employee':emp})  

def update(request, id):  
    emp = employee.objects.get(id=id)  
    form = employeeForm(request.POST, instance = emp)  
    if form.is_valid():  
        form.save()  
        return redirect("/searchEmployee")  
    return render(request, 'employeeInformation.html', {'employee': emp})    


 

def salary(request):
    return render(request,'salary.html')

def salaryReport(request):
    return render(request,'salaryReport.html')

def payslipDistribution(request):
    return render(request,'payslipDistribution.html')