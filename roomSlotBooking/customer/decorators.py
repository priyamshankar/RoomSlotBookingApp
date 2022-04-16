from django. http import HttpResponse
from django.shortcuts import redirect
from requests import request

def unauthenticated_user(view_fnc):
    def wrapper_fnc(request, *args,**kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_fnc(request,*args,**kwargs)
            

    return wrapper_fnc

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args,**kwargs):

            group =None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_func(request,*args,**kwargs)
            else:
                return HttpResponse('you are not authorised to view this page')
        return wrapper_func
    return decorator