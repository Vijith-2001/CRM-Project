from django.shortcuts import render,redirect,get_object_or_404

# Create your views here.

from django.views.generic import View

from .utility import get_admission_number,get_password

from.models import Student

from .forms import StudentRegisterForm

from django.db.models import Q

from authentication.models import Profile

from authentication.permissions import permission_roles


from django.db import transaction

from django.contrib.auth.decorators import login_required

from django.utils.decorators import method_decorator







class GetStudentObject:                 #to avoid repetition

    def get_student(self,request,uuid):

        try:

            student = Student.objects.get(uuid=uuid)

            return student

        except:

            return render(request,'errorpages/error-404.html')




    #dispatch decides whether to go to get or post

# @method_decorator(permission_roles(roles=['Admin','Sales']),name='dispatch')

class DashboardView(View):

    def get(self,request,*args,**kwargs):

        return render(request,'students/dashboard.html')
    

    

# @method_decorator(permission_roles(roles=['Admin','Sales','Trainer','Academic Counsellor']),name='dispatch')

class StudentsListView(View):

    def get(self,request,*args,**kwargs):

        query = request.GET.get('query')

        students = Student.objects.filter(active_status = True)

        if query:

            students = Student.objects.filter(Q(active_status = True)&(Q(first_name__icontains=query)|
                                                                       Q(last_name__icontains=query)|
                                                                       Q(email__exact=query)|
                                                                       Q(contact_num__icontains=query)|
                                                                       Q(house_name__icontains=query)|
                                                                       Q(post_office__icontains=query)|
                                                                       Q(district__icontains=query)|
                                                                       Q(pincode__icontains=query)|
                                                                       Q(adm_number__icontains=query)|
                                                                       Q(course__code__icontains=query)|
                                                                       Q(batch__name__icontains=query)|
                                                                       Q(trainer__first_name__icontains=query)))


        # students = Student.objects.all()


        data = {'students':students,'query':query}      

        return render(request,'students/students.html',context=data)
    

    

# @method_decorator(permission_roles(roles=['Admin','Sales']),name='dispatch')

class FormsView(View):

    def get(self,request,*args,**kwargs):

        form = StudentRegisterForm()


        data = {'form':form}

        return render(request,'students/forms.html',context=data)
    
    
    def post(self,request,*args,**kwargs):

        form = StudentRegisterForm(request.POST,request.FILES)


        if form.is_valid():

            with transaction.atomic():

                student = form.save(commit=False)


                student.adm_number = get_admission_number()

                student.join_date = '2025-02-05'



                username = student.email

                password = get_password()

                print(password)

                profile = Profile.objects.create_user(username=username,password=password,role='Student')

                student.profile = profile



                student.save()

            return redirect('students')  #reference name
        
        else:

            data = {'form':form} 

            return render(request,'students/forms.html',context=data)



@method_decorator(permission_roles(roles=['Admin','Sales','Trainer','Academic Counsellor']),name='dispatch')

class StudentDetailView(View):

    def get(self,request,*args,**kwargs):

        uuid = kwargs.get('uuid')

        student = GetStudentObject().get_student(request,uuid)



        data = {'student':student}



        return render(request,'students/student-detail.html',context=data)
    




# class Error404View(View):

#     def get(self,request,*args,**kwargs):

#         return render(request,'students/error-404.html')
    


#student delete view

@method_decorator(permission_roles(roles=['Admin','Sales']),name='dispatch')

class StudentDeleteView(View):

    def get(self,request,*args,**kwargs):


        uuid = kwargs.get('uuid')

        student = GetStudentObject().get_student(request,uuid)
        

        # student.delete()

        student.active_status = False    #soft-delete

        student.save()




        return redirect('students')
    

@method_decorator(permission_roles(roles=['Admin','Sales']),name='dispatch')

class StudentUpdateView(View):

    def get(self,request,*args,**kwargs):

        uuid = kwargs.get('uuid')

        student = GetStudentObject().get_student(request,uuid)

        form = StudentRegisterForm(instance=student)    #for edit, add instance

        data = {'form':form}



        return render(request,'students/student-update.html',context=data)
    


    def post(self,request,*args,**kwargs):

        uuid = kwargs.get('uuid')

        student = GetStudentObject().get_student(request,uuid)

        form = StudentRegisterForm(request.POST,request.FILES,instance=student)  #always add instance when updating/editing

        if form.is_valid():

            form.save()

            return redirect('students')
        
        else:

            data = {'form':form}

            return render(request,'students/student-update.html',context=data)












        

        




    
    




