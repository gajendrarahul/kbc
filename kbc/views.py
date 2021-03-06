from django.shortcuts import render,HttpResponse,redirect
from django.views.generic import TemplateView
from Account.models import Account
from teacher.models import TeacherDetails
from django.contrib.auth.hashers import make_password
from django.contrib.auth import logout,login,authenticate
from django.contrib.auth.decorators import login_required


def Homepage(request):
    if request.user.is_authenticated:
        if request.user.is_teacher:
            return redirect('teacherhomepage')
        elif request.user.is_admin:
            return redirect('adminhomepage')
        else:
            return HttpResponse('<center><h2 style = "margin-top:20%">You are not authorized <br> please contact the administrator </h2></center>')
        return render(request,'dashboard.html')
    else:
        return render(request,'dashboard.html')

# admin home page 
@login_required(login_url='signin')
def AdminHome(request):
    teacher_details=TeacherDetails.objects.filter()[::1]
    return render(request,'admin/adminhomepage.html',{'teacher_details':teacher_details})
# admin teacher home  page

@login_required(login_url='signin')
def Adminteacher(request):
    teacher_details=TeacherDetails.objects.filter()[::1]
    return render(request,'admin/adminteacher.html',{'teacher_details':teacher_details})

# Everyone login code  here 
def Signin(request):
    if request.method=="GET":
        return render(request,'login.html')
    else:
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            if request.user.is_teacher:
                return redirect('teacherhomepage')
            elif request.user.is_admin:
                return redirect('adminhomepage')
            else:
                return HttpResponse('<center><h2 style = "margin-top:20%">You are not authorized <br> please contact the administrator </h2></center>')
        else:
            return HttpResponse('<center><h2 style = "margin-top:20%">opps!!! you donot have account here <br> please contact the administrator </h2> <a href="dashboard.html">Home</a></center>')
# add teacher details and teacher account  view 
def TeacherUserSignup(request):
    if request.method=="GET":
        return render(request,'admin/adminhomepage.html')
    else:
        name = request.POST['Tname']
        sub = request.POST['subject']
        sdate = request.POST['sdate']
        edate = request.POST['edate']
        salary =request.POST['salary']
        contact = request.POST['contact']
        address = request.POST['address']
        email = request.POST['email']
        p1 = request.POST['password1']
        p2 = request.POST['password2']
        if p1==p2:
            user = Account(email=email,password=make_password(p1),is_teacher=True)
            user.save()
            print(user.id)
            teacher = TeacherDetails(name=name,email=user.email,subject=sub,started_date=sdate,end_date=edate,salary=salary,contact=contact,address=address,user_id=user.id)
            teacher.save()
            return  redirect('adminteacher')
# teacher account delete
def Delete(request, id):
    a = TeacherDetails.objects.get(id=id)
    user = Account.objects.get(id=a.user_id)
    user.delete()
    return redirect('adminteacher')

def Editteacher(request,id):
    context = {
        'teacher':TeacherDetails.objects.get(id=id),
        'teacher_details':TeacherDetails.objects.filter()
    } 
    return render(request,'admin/editteacher.html', context)
def Signout(request):
    logout(request)
    return redirect('signin') 