#to generate a random admission number

import uuid

from .models import Student

import string

import random



def get_admission_number():

    while True:

        pattern = str(uuid.uuid4().int)[:7]       #convert to string and apply slicing
    
        admission_number = f"LM-{pattern}"


        if not Student.objects.filter(adm_number = admission_number).exists():

            return admission_number
        

# string.ascii_letters ---- 'a,b,c,d,AZ'

# string.digits 


def get_password():


    password = ''.join(random.choices(string.ascii_letters + string.digits,k=8))

    return password


    
