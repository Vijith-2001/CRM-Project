from django.db import models

import uuid

# Create your models here.




#for giving slug(combination of symbols,numbers etc)


class BaseClass(models.Model):

    uuid = models.SlugField(unique=True,default=uuid.uuid4)

    active_status = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)   #auto_now updates everytime


    class Meta:

        abstract = True





# class CourseChoices(models.TextChoices):    #for choice/options

#     # variable = databasevalue, representation

#     PY_DJANGO = 'PY-DJANGO','PY-DJANGO'

#     MEARN = 'MEARN','MEARN'

#     DATA_SCIENCE = 'DATA SCIENCE','DATA SCIENCE'

#     SOFTWARE_TESTING = 'SOFTWARE TESTING','SOFTWARE TESTING'



class DistrictChoices(models.TextChoices):   

    TRIVANDRUM = 'TRIVANDRUM','TRIVANDRUM'

    KOLLAM = 'KOLLAM','KOLLAM'

    PATHANAMTHITTA = 'PATHANAMTHITTA','PATHANAMTHITTA'

    ALAPPUZHA = 'ALAPPUZHA','ALAPPUZHA'

    KOTTAYAM = 'KOTTAYAM','KOTTAYAM'

    IDUKKI = 'IDUKKI','IDUKKI'

    ERNAKULAM = 'ERNAKULAM','ERNAKULAM'

    THRISSUR = 'THRISSUR','THRISSUR'

    PALAKKAD = 'PALAKKAD','PALAKKAD'

    MALAPPURAM = 'MALAPPURAM','MALAPPURAM'

    KOZHIKODE = 'KOZHIKODE','KOZHIKODE'

    WAYANAD = 'WAYANAD','WAYANAD'

    KANNUR = 'KANNUR','KANNUR'

    KASARGOD = 'KASARGOD','KASARGOD'


# class BatchChoices(models.TextChoices):

#     PY_NOV_2024 = 'PY_NOV_2024','PY_NOV_2024'

#     PY_JAN_2025 = 'PY_JAN_2025','PY_JAN_2025'

#     DS_JAN_2025 = 'DS_JAN_2025','DS_JAN_2025'

#     ST_JAN_2025 = 'ST_JAN_2025','ST_JAN_2025'

#     MEARN_NOV_2024 = 'MEARN_NOV_2024','MEARN_NOV_2024'

#     MEARN_JAN_2025 = 'MEARN_JAN_2025','MEARN_JAN_2025'


# class TrainerChoices(models.TextChoices):


#     JOHN_DOE = 'JOHN_DOE','JOHN_DOE'

#     JAMES = 'JAMES','JAMES'

#     PETER = 'PETER','PETER'

#     ALEX = 'ALEX','ALEX'








class Student(BaseClass):        #this is the table name


    ''' personal details fields'''

    profile = models.OneToOneField('authentication.Profile',on_delete=models.CASCADE)





    first_name = models.CharField(max_length=50)

    last_name = models.CharField(max_length=50)

    photo = models.ImageField(upload_to = 'students')

    email = models.EmailField(unique=True)

    contact_num = models.CharField(max_length=50)

    house_name = models.CharField(max_length=50)

    post_office = models.CharField(max_length=50)

    district = models.CharField(max_length=50, choices=DistrictChoices.choices)

    pincode = models.CharField(max_length=6)

    
 
    '''course details fields'''



    adm_number = models.CharField(max_length=50)

    # course = models.CharField(max_length=50, choices=CourseChoices.choices)   #default=CourseChoices.PY_DJANGO

    course = models.ForeignKey('courses.Courses',null=True,on_delete=models.SET_NULL)

    # batch = models.CharField(max_length=50,choices=BatchChoices.choices)

    batch = models.ForeignKey('batches.Batches',null=True,on_delete=models.SET_NULL)

    # batch_date = models.DateField()

    join_date = models.DateField(auto_now_add=True)

    # trainer_name = models.CharField(max_length=50,choices=TrainerChoices.choices)

    trainer = models.ForeignKey('trainers.Trainers',null=True,on_delete=models.SET_NULL)





  #using magic method- string representation


    def __str__(self):

        return f"{self.first_name} {self.last_name} "     #for showing student names on adding files
    

    class Meta:

        verbose_name = 'Students'

        verbose_name_plural = 'Students'

        ordering = ['-id']     #for ordering the added students  (also -id for reverse ordering)




