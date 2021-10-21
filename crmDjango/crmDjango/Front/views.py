from django.http import HttpResponse
from django.http.response import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from datetime import datetime
from crmDjango.Back.controller import Controller
from crmDjango.Front.templates.userForm import UserForm
from django.core.exceptions import ValidationError

class views:
    
    usersList = Controller.getUsers()
    needSort=False
    c=''

    def index(request):
        return render(request, 'index.html',context={})

    def users(request):
        charList=Controller.getCharUsersList()

        if request.method == 'POST':
            form = UserForm(request.POST)

            if request.POST.get('removeBtn'):
                Controller.removeUser(request.POST.get('firstnameRMV'),request.POST.get('lastnameRMV'))
                views.usersList = Controller.getUsers()
            
            if request.is_ajax():
                form = UserForm(request.POST)
                if form.is_valid() and not Controller.isUser(form.cleaned_data['firstname'], form.cleaned_data['lastname']):
                    Controller.addUser(form.cleaned_data['firstname'], form.cleaned_data['lastname'], form.cleaned_data['email'], form.cleaned_data['address'], form.cleaned_data['phone'])
                    views.usersList = Controller.getUsers()
                    return JsonResponse({"success": "success"},status=200)
                else:
                    errors = form.errors.as_json()
                    return JsonResponse({"errors": errors}, status=400) 

        else:
            if request.is_ajax():
                views.c=request.GET.get('char')
                if not views.c=='':
                    views.needSort = True
                    #views.usersList = Controller.sortByChar(c) #Controller.getUsers()
                    return JsonResponse({"success": "success"},status=200)
                else:
                    return JsonResponse({"errors": "errors"}, status=400) 
            
        form = UserForm()
        if views.needSort:
            views.usersList = Controller.sortByChar(views.c)
        for w in range(len(views.usersList)):
            print("lastname2:",views.usersList[w].getLastName())
        return render(request, 'users.html',context={"usersList":views.usersList,'form':form,'controller':Controller,'charList':charList})