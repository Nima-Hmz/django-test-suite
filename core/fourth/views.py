from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse, JsonResponse
import requests
from requests.exceptions import RequestException

# Create your views here.

class loginView(View):
    def get(self, request):
        return render(request, 'fourth/login.html')
    

class DashboardView(View):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)
        
        return redirect('fourth:login')

    def get(self, request):
        user = request.user
        return HttpResponse(f"here is the dashboard page {user.username}")
    

class PostView(View):
    def get(self, request):
        try:
            response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
            response.raise_for_status()
            return JsonResponse(response.json())
        except RequestException as e:
            # log the exception

            # return a 503 service unavailable response
            return HttpResponse('service unavailable', status=503) 
        

# the hard coded way
class PostView2(View):
    def get(self, request):
        try:
            response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
            if response.status_code == 200:
                return JsonResponse(response.json())
            
            return HttpResponse("fail", status=503)
        
        except Exception:
            return HttpResponse('fail2', status=503)
        


# multiple Apis(for more professional mocking practice)
class PostView3(View):
    def get(self, request):
        result = []
        try:
            response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
            response.raise_for_status()
            result.append(response.json())
        except RequestException as e:
            # log the exception

            # return a 503 service unavailable response
            return HttpResponse('service unavailable(the first)', status=503) 
        
        try:
            response2 = requests.get('https://jsonplaceholder.typicode.com/posts/2')
            response.raise_for_status()
            result.append(response2.json())
        except RequestException as e:
            # log the exception

            # return a 503 service unavailable response
            return HttpResponse('service unavailable(the second)', status=503) 
        
        try:
            response3 = requests.get('https://jsonplaceholder.typicode.com/posts/3')
            response.raise_for_status()
            result.append(response3.json())
        except RequestException as e:
            # log the exception

            # return a 503 service unavailable response
            return HttpResponse('service unavailable(the third)', status=503) 

        return JsonResponse(result, safe=False)
