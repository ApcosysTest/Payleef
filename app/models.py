from django.db import models

class Login(models.Model):
    username = models.CharField(max_length=10)
    password = models.EmailField(max_length=10) 
    
    class Meta:  
        db_table = "login"


class companysetup(models.Model):
    company_name = models.CharField(max_length=500,blank = True,null=True)
    email = models.EmailField(max_length=500,blank=True,unique=True) 
    website = models.CharField(max_length=500,blank = True,null=True)
    telephone = models.IntegerField(blank=True,null=True)
    state = models.CharField(max_length=500,blank = True,null=True)
    zip = models.IntegerField(blank = True,null=True)
    city = models.CharField(max_length=500,blank = True,null=True)
    country = models.CharField(max_length=500,blank = True,null=True)
    companylogo = models.ImageField(upload_to='images/')
    
    # basic = models.CharField(max_length=50,blank = True,null=True)
    # houseRentAllowance = models.CharField(max_length=50,blank=True,null=True) 
    # medicalAllowance = models.CharField(max_length=50,blank = True,null=True)
    # foodAllowance = models.CharField(max_length=50,blank = True,null=True)
    # conveyanceAllowance = models.CharField(max_length=50,blank = True,null=True)
    # attendance = models.CharField(max_length=50,blank = True,null=True)
    # other = models.CharField(max_length=50,blank = True,null=True)
    # annualBonus = models.CharField(max_length=50,blank = True,null=True)
    # professionalTax = models.CharField(max_length=50,blank = True,null=True)
    
    class Meta:  
        db_table = "companysetup" 
        
        
class employee(models.Model):
    emp_code = models.CharField(max_length=500)
    emp_Name = models.CharField(max_length=500)
    emp_PAN = models.CharField(max_length=500)
    Joining_date = models.CharField(max_length=500)
    mobile_no = models.IntegerField()
    salary = models.CharField(max_length=500)
    CTC = models.CharField(max_length=500) 
    designation = models.CharField(max_length=500)
    department = models.CharField(max_length=500) 
    email = models.EmailField(max_length=70,blank=True,unique=True) 
    bank_Name = models.CharField(max_length=500)
    bank_Account_No = models.CharField(max_length=500)
    IFSC = models.CharField(max_length=500)
    branch = models.CharField(max_length=500)
    
    

    class Meta:  
        db_table = "employee"