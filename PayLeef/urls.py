"""PayLeef URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   path('',views.login),
   path('homepage',views.homepage),
   path('companySetup',views.companySetup),
   path('companyInformation',views.companyInformation),
   path('addEmployee',views.addEmployee),
   path('searchEmployee',views.searchEmployee),
   path('employeeDetails', views.employeeDetails),  
   path('employeeInformation/<int:id>', views.employeeInformation),  
   path('update/<int:id>', views.update),  
#    path('disable_emp/<str:emp_code>/<int:id>',views.disable_emp),
   path('deactive_emp/<str:emp_code>/<int:id>',views.deactive_emp),
   path('active_emp/<str:emp_code>/<int:id>',views.active_emp),
   path('salary',views.salary),
#    path('salaryDetails',views.salaryDetails),
   path('salaryReport',views.salaryReport),
   path('payslip',views.payslip),
   path('payslipDistribution',views.payslipDistribution),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
