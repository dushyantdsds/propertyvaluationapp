from django.shortcuts import render
from django.views import View

# Create your views here
class Index(View):
    def get(self,request,*args,**kwrgs):
        return render(request,'index.html')