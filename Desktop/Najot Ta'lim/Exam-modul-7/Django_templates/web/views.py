import requests
from django.views import View, generic
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

class Get_info_api:
    @staticmethod
    def get_student():
        url = 'http://127.0.0.1:8000/api/student/'
        # data = {
        #     'username': username1,
        #     'password': password
        # }
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return 'failed'
    
    @staticmethod
    def get_course():
        url = 'http://127.0.0.1:8000/api/course/'
        # data = {
        #     'username': username1,
        #     'password': password
        # }
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return 'failed'
    
    @staticmethod
    def get_course_detail(id):
        url = f"http://127.0.0.1:8000/api/course/{id}"
        # data = {
        #     'username': username1,
        #     'password': password
        # }
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return 'failed'
            
    @staticmethod
    def post_student(first_name, last_name, email, phone_number, username, password):
        url = 'http://127.0.0.1:8000/api/student/'
        data = {
            "first_name": first_name,
            "last_name": last_name,
            "email":email,
            "phone_number":phone_number,
            "username": username,
            "password": password
        }
        response = requests.post(url, data=data)
        if response.status_code == 201:
            return response.json()
        else:
            return 'failed'    
    @staticmethod
    def post_message(first_name, last_name, email, phone_number, username, message):
        url = 'http://127.0.0.1:8000/api/message/'
        data = {
            "first_name": first_name,
            "last_name": last_name,
            "email":email,
            "phone_number":phone_number,
            "username": username,
            "message": message
        }
        response = requests.post(url, data=data)
        if response.status_code == 201:
            return response.json()
        else:
            return 'failed'    
    
    
    
class Index_View(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')

class Login_View(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'login.html')
    
    def post(self, request, *args, **kwargs):
        username1 = request.POST['username']
        password = request.POST['password']
        value = {'username':username1, 'password':password}
        user, created = User.objects.get_or_create(username=username1)
        print('pppppppppppppppppppppp', username1, password)
        if (username1 and password):
            print('aaaaaaaaaaaaaaaaaaaaaaaaaaaa', Get_info_api.get_student())
            for username_from_api1 in Get_info_api.get_student():
                print('aaaaaaaaaaaaaaaaaaaaaaaaaaaa', username_from_api1['username'], username_from_api1['password'])
                if str(username1) == username_from_api1['username']:
                    print('ttttttttttttttttttttttttttttttttttttttt')
                    if str(password) == username_from_api1['password']:
                        status = request.session.get('status')
                        request.session['status'] = 'st'
                        # request.user.save()
                        login(request, user)
                        return redirect('index')
                    else:
                        return render(request, 'login.html', context={'message':'password', 'value':value})
                else:
                    continue
            return render(request, 'login.html', context={'message':'nfound', 'value':value})
        return render(request, 'login.html', context={'message':'found_first', 'value':value})
    
class Register_View(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'register.html')
    
    def post(self, request, *args, **kwargs):
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        username = request.POST['username']
        password = request.POST['password']
        user, created = User.objects.get_or_create(username=username)
        try:
            if not phone_number.isdigit():
                phone_number = phone_number
        except:
            print('Error integer')
        value = {'first_name':first_name, 'last_name':last_name, 'email':email, 'phone_number':phone_number, 'username':username, 'password':password}
        if (first_name and last_name and email and phone_number and username and password):
            for username_from_api1 in Get_info_api.get_student():
                print('aaaaaaaaaaaaaaaaaaaaaaaaaaaa', username_from_api1['username'], username_from_api1['password'])
                if phone_number != username_from_api1['phone_number']:
                    print('aaaaaaaaaaaaaaaaaaaaaaaaaaaa', username_from_api1['username'], username_from_api1['password'])
                    if username != username_from_api1['username']:
                        if Get_info_api.post_student(first_name=first_name, last_name=last_name, email=email, phone_number=phone_number, username=username, password=password) != 'failed':
                            status = request.session.get('status')
                            request.session['status'] = 'st'
                            login(request, user)
                            return redirect('login')
                    #     return render(request, 'register.html', context={'value':value, 'message':'server'})
                    # return render(request, 'register.html', context={'value':value, 'message':'username'})
            return render(request, 'register.html', context={'value':value, 'message':'error'})
        return render(request, 'register.html', context={'value':value, 'message':'tuldir'})

class Log_OutView(View):
    def get(self, request):
        logout(request)
        return redirect('index')
    
class Team_View(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'team.html')
    
class Testimonial_View(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'testimonial.html')
    
class Service_View(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'service.html')
    
class Offer_View(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'offer.html')
    
class Feature_View(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'feature.html')
    
class FAQ_View(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'FAQ.html')
    
class Contact_View(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'contact.html')
    
    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            phone_number = request.POST['phone_number']
            username = request.POST['username']
            message = request.POST['message']
            value = {'first_name':first_name, 'last_name':last_name, 'email':email, 'phone_number':phone_number, 'username':username, 'message':message}
            if (first_name and last_name and email and phone_number and username and message):
                for username_from_api1 in Get_info_api.get_student():
                    print('aaaaaaaaaaaaaaaaaaaaaaaaaaaa', username_from_api1['username'], username_from_api1['password'])
                    if phone_number == username_from_api1['phone_number']:
                        print('aaaaaaaaaaaaaaaaaaaaaaaaaaaa', username_from_api1['username'], username_from_api1['password'])
                        if username == username_from_api1['username']:
                            if Get_info_api.post_message(first_name=first_name, last_name=last_name, email=email, phone_number=phone_number, username=username, message=message) != 'failed':
                                return redirect('index')
                            # return render(request, 'contact.html', context={'value':value, 'message':'server'})
                        # return render(request, 'contact.html', context={'value':value, 'message':'username'})
                        # return render(request, 'contact.html', context={'value':value, 'message':'phone'})
                return render(request, 'contact.html', context={'value':value, 'message':'error'})
            return render(request, 'contact.html', context={'value':value, 'message':'tuldir'})
        else:
            message = request.POST['message']
            if message:
                for username_from_api1 in Get_info_api.get_student():
                    print('aaaaaaaaaaaaaaaaaaaaaaaaaaaa', username_from_api1['username'], username_from_api1['password'], request.user.username)
                    if request.user.username == username_from_api1['username']:
                        if Get_info_api.post_message(first_name=username_from_api1['first_name'], last_name=username_from_api1['last_name'], email=username_from_api1['email'], phone_number=username_from_api1['phone_number'], username=username_from_api1['username'], message=message) != 'failed':
                                return redirect('index')
                        
                        
class Blog_View(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'blog.html')
    
class Base_View(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'base.html')
    
class Course_View(View):
    def get(self, request, *args, **kwargs):
        if Get_info_api.get_course() != 'failed':
            courses = Get_info_api.get_course()
            return render(request, 'course.html', context={'courses':courses})
    
class CourseView(View):
    def get(self, request, id):
        course = Get_info_api.get_course_detail(id)
        return render(request, 'course_detail.html', context={'course':course})
    
class Error_View(View):
    def get(self, request, *args, **kwargs):
        return render(request, '404.html')