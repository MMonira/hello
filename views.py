from django.shortcuts import redirect , render
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from PIL import Image
from django.contrib.auth.hashers import check_password
from django.contrib.auth import update_session_auth_hash

from Jobapp.models import *


def signuppage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        First = request.POST.get('first_name')
        Last = request.POST.get('last_name')
        Pass = request.POST.get('password')
        ConfPass = request.POST.get('confirm_password')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        blood_group = request.POST.get('blood_group')
        city = request.POST.get('city')
        country = request.POST.get('country')
        user_type = request.POST.get('user_type')
        profile_photo = request.FILES.get('profile_photo')
        if Pass == ConfPass:
            myuser = Custom_user.objects.create_user(
                username = uname,
                password = Pass,
                first_name = First,
                last_name = Last,

            )
            myuser.age = age
            myuser.gender = gender
            myuser.blood_group = blood_group
            myuser.city = city
            myuser.country = country
            myuser.user_type = user_type
            myuser.profile_photo = profile_photo

           
            if user_type == 'recruiter':
                recruitermodel.objects.create(user = myuser)
                # recruiter_basic_information.objects.create(user = myuser)
                # recruitercontact.objects.create(user = myuser)
            
            
            elif user_type == 'jobseeker':
                seekermodel.objects.create(user = myuser)
                # seeker_basic_information.objects.create(user = myuser)
                # seekercontact.objects.create(user = myuser)
                # work_experience.objects.create(user = myuser)
                # Education_qualifications.objects.create(user = myuser)


            myuser.save()
       
            messages.success(request,'You Signup Successfully')
            return redirect('signin')
        else:
            messages.error (request,'Password and Confirm Password did not Match')
    return render(request, 'signup.html')


def signinpage(request):
    if request.method == 'POST':
        uname = request.POST.get('username') 
        passw = request.POST.get('password')

        user = authenticate(username = uname, password = passw)

        if user:
            login(request, user)

            return redirect('dashboard')
        else:
            return redirect('signin')

    return render(request, 'signin.html')


@login_required
def dashboard(request):

    return render(request,'dashboard.html')


@login_required
def profile(request):
    current_user = request.user
    user_type = request.user.user_type
    if user_type == 'recruiter':
        info = recruitermodel.objects.get(user = current_user)
    else:
        info = seekermodel.objects.get(user = current_user)

    return render(request, 'profile.html',{'info':info})



@login_required
def logoutt(request):
    logout(request)
    return redirect('signin')


@login_required
def viewjob(request):
    current_user = request.user
    user_type = request.user.user_type
    if user_type == 'recruiter':
        info = jobInformationmodel.objects.filter(created_by = current_user)
    else: 
        info = jobInformationmodel.objects.all()

    return render(request,'viewjoblist.html',{'info':info})


@login_required
def applied(request):
    return render(request,'appliedjob.html')


@login_required
def addjob(request):
    if request.method == 'POST':
        title = request.POST.get('job_title')
        job_description = request.POST.get('job_description')
        job_location = request.POST.get('job_location')
        deadline = request.POST.get('deadline')
        company_logo = request.POST.get('company_logo')
        requirements = request.POST.get('requirements')
        qualifications = request.POST.get('qualifications')
        job_type = request.POST.get('job_type')
        work_place = request.POST.get('work_place')
        salary = request.POST.get('salary')
        experience = request.POST.get('experience')
        current_user = request.user

        data = jobInformationmodel(
            job_title = title,
            job_description = job_description,
            job_location = job_location,
            deadline = deadline,
            company_logo = company_logo ,
            requirements = requirements,
            qualifications = qualifications,
            job_type = job_type,
            work_place = work_place,
            salary = salary,
            experience = experience,
            created_by = current_user,
        )
        data.save()
        return redirect('viewjob')
    return render(request,'addjob.html')


@login_required
def view(request,myid):
    info = jobInformationmodel.objects.get(id = myid)
    return render(request,'newview.html',{'info':info})


def delete(request,myid):
    info = jobInformationmodel.objects.get(id = myid)
    info.delete()
    return redirect('viewjob')

def edit(request,myid):
    info = jobInformationmodel.objects.get(id = myid)
    return render(request,'editjob.html',{'info':info})


@login_required
def editprofile(request):
    return render(request,'editprofile.html')



@login_required
def updateprofile(request):
    currentUser = request.user

    if request.method == 'POST':
        uname = request.POST.get('username')
        first = request.POST.get('firstname')
        last = request.POST.get('lastname')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        blood_group = request.POST.get('blood_group')
        city = request.POST.get('city')
        country = request.POST.get('country')
        profile_photo = request.FILES.get('profile_photo')
        preprofile_photo = request.POST.get('preprofile_photo')
        user_type = request.POST.get('user_type')
        company_name = request.POST.get('company_name')
        company_location = request.POST.get('company_location')
        recruiter_name = request.POST.get('recruiter_name')
        qualifications = request.POST.get('qualifications')
        experience = request.POST.get('experience')
        skills = request.POST.get('skills')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if password == confirm_password :
            if  check_password (confirm_password, currentUser.password):
                currentUser.gender = gender
                currentUser.age = age
                currentUser.blood_group = blood_group
                currentUser.city = city
                currentUser.country = country
                currentUser.first_name = first
                currentUser.last_name = last

                if profile_photo:
                    currentUser.profile_photo = profile_photo

                else:
                    currentUser.profile_photo = preprofile_photo
                if currentUser.user_type == 'jobseeker':
                    myseeker = currentUser.seemodel
                    myseeker.qualification = qualifications
                    myseeker.experience = experience
                    myseeker.skills = skills

                    myseeker.save()

                elif currentUser.user_type == 'recruiter':
                    myrecruiter = currentUser.recmodel
                    myrecruiter.company_name = company_name
                    myrecruiter.company_location = company_location
                    myrecruiter.recruiter_name = recruiter_name
                    myrecruiter.save()

                currentUser.save()

                return redirect('profile')

        else :
            return redirect('editprofile')   



@login_required
def update(request):
    if request.method == 'POST':
        jid = request.POST.get('jid')
        title = request.POST.get('job_title')
        job_description = request.POST.get('job_description')
        job_location = request.POST.get('job_location')
        deadline = request.POST.get('deadline')
        company_logo = request.FILES.get('company_logo')
        requirements = request.POST.get('requirements')
        qualifications = request.POST.get('qualifications')
        job_type = request.POST.get('job_type')
        work_place = request.POST.get('work_place')
        precompany_logo = request.POST.get('precompany_logo')
        salary = request.POST.get('salary')
        experience = request.POST.get('experience')
        current_user = request.user

        data = jobInformationmodel(
            id = jid,
            job_title = title,
            job_description = job_description,
            job_location = job_location,
            deadline = deadline,
           
            requirements = requirements,
            qualifications = qualifications,
            job_type = job_type,
            work_place = work_place,
            salary = salary,
            experience = experience,
            created_by = current_user,
        )
        if company_logo:
            data.company_logo = company_logo
        else:
            data.company_logo = precompany_logo
        data.save()
        return redirect('viewjob')
# @login_required
# def viewjob(request):
#     return render(request,'')



@login_required
def seebasic(request):
    return render(request,'seebasic.html')
    

@login_required
def changepass(request):
    if request.method == 'POST':
        current_password = request.POST.get('current_password')
        confirm_new_password = request.POST.get('confirm_new_password')
        new_password = request.POST.get('new_password')
        if check_password(current_password,request.user.password) :
            if new_password == confirm_new_password:
                # user = Custom_user(
                #     password = new_password,
                # )
                request.user.set_password(new_password)

                request.user.save()
                update_session_auth_hash(request,request.user)

                return redirect('profile')
                
    return render(request,'changepass.html')


