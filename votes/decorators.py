from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func

def official_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_official | request.user.is_superuser:
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponse('You are not authorised to view this page.')
    return wrapper_func

# def allowed_users(allowed_roles=[]):
#     def decorator(view_func):
#         def wrapper_func(request, *args, **kwargs):
#             group = None
#             if request.user.groups.filter(name__in=allowed_roles).exists():
#                 return view_func(request, *args, **kwargs)
#             else:
#                 return HttpResponse('You are not authorised to view this page.')
#         return wrapper_func
#     return decorator