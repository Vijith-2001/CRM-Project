
#to write decorators


from django.shortcuts import redirect,render




def permission_roles(roles):    #to recieve role

    def decorator(fn):     #to recieve function (decorator always recieve function)

        def wrapper(request,*args,**kwargs):

            if request.user.is_authenticated and request.user.role in roles:     #check if user is logged in and role is present

                return fn(request,*args,**kwargs)
            
            else:

                return render(request,'errorpages/error-403.html')
        
        return wrapper
    
    return decorator