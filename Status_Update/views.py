from .forms import UserForm, EngineerForm, task, CalenderForm
from .models import Manage
from datetime import datetime
from django.urls import reverse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
now = datetime.now()


def register(request):
    registered = False
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            group = Group.objects.get(name="Engineer")
            user.groups.add(group)
            registered = True
        else:
            print('Invalid')
    else:
        user_form = UserForm()

    return render(request, 'Status_Update/register.html', context={'user_form': user_form, 'registered': registered})

# Status_Update | manage |Can view manage


def user_login(request):
    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(password=password, username=username)
        if user:
            login(request, user)
            if user.is_active and request.user.groups.filter(name="Engineer").exists():
                return HttpResponseRedirect(reverse('status:user'))
            elif user.is_active and request.user.groups.filter(name="Manager").exists():
                return HttpResponseRedirect(reverse('status:manager'))
            else:
                return HttpResponse("Unauthoried")
        else:
            return HttpResponse("ACCOUNT NOT ACTIVE")
    else:
        return render(request, 'Status_Update/login.html')


@login_required
def engineer_home(request):
    if request.method == 'POST':
        print(request.user.groups)
        weekly_task = Manage.objects.filter(
            year=now.year,
            week=now.isocalendar()[1], name_id=request.user.id)
        comment_list = request.POST.getlist('comments')
        print(comment_list)
        status_list = request.POST.getlist('status')
        print(status_list)

        for iteration, each_task in enumerate(weekly_task):
            print(iteration, each_task.id)
            obj = Manage.objects.get(id=each_task.id)
            obj.comments = comment_list[iteration]
            obj.status = status_list[iteration]
            obj.save()

        return HttpResponseRedirect(reverse('status:user'))

    else:
        weekly_task = Manage.objects.filter(
            year=now.year,
            week=now.isocalendar()[1], name_id=request.user.id)
        print(request.user.username)
        entry = []
        for each_task in weekly_task:
            print(each_task.comments)
            form = EngineerForm()
            form.fields['comments'].widget.attrs['value'] = each_task.comments
            form.fields['status'].widget.attrs['value'] = each_task.status
            entry.append((each_task.task, form))

        cont = {'entry': entry}

        return render(request, 'Status_Update/engineer.html', context=cont)


def manager_home(request):
    details = Manage.objects.filter(year=now.year,
                                    week=now.isocalendar()[1])
    if request.method == 'POST':
      #  print(request.POST.getlist('comments'))
        x = request.POST
        engineer = User.objects.get(id=int(x['name']))

        obj = Manage(date=now, year=now.year,
                     week=now.isocalendar()[1], task=x['task'], name_id=int(x['name']), engineer=engineer)
        obj.save()

        print(request.POST['name'])

        return HttpResponseRedirect(reverse('status:manager'))
    else:
        form = task()
        engineer = []
        users = User.objects.all()
        for iteration in users:
            engineer.append([iteration.id, iteration.username])
        print(engineer)
        cont = {'task': task(), 'engineer': engineer, "details": details,
                'calender': CalenderForm()}
        return render(request, 'Status_Update/manager.html', context=cont)
  #  return render(request, 'Status_Update/manager.html', context={"details": obj})


def manager_search(request):
    print(request.POST['date'])
    search_date = datetime.strptime(request.POST['date'], '%d/%m/%Y').date()
    print(search_date.year)
    print(search_date.isocalendar()[1])
    details = Manage.objects.filter(year=search_date.year,
                                    week=search_date.isocalendar()[1])
    print(details)
    cont = {'details': details, 'calender': CalenderForm()}
    return render(request, 'Status_Update/manager_search.html', context=cont)


@login_required
def each_task(request):

    if request.method == 'POST':

      #  print(request.POST.getlist('comments'))
        x = request.POST
        engineer = User.objects.get(id=int(x['name']))
        now = datetime.now()
        obj = Manage(date=now, year=now.year,
                     week=now.isocalendar()[1], task=x['task'], name_id=int(x['name']), engineer=engineer)
        obj.save()

        print(request.POST['name'])

        return HttpResponseRedirect(reverse('status:each'))
    else:
        form = task()
        engineer = []
        users = User.objects.all()
        for iteration in users:
            engineer.append([iteration.id, iteration.username])
        print(engineer)
        cont = {'task': task(), 'engineer': engineer}
        return render(request, 'Status_Update/each_task.html', context=cont)


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))


def redirect_to_login(request):
    return HttpResponseRedirect('login')
