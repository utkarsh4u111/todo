from django.shortcuts import render
from .models import tasklist

# Create your views here.
def home(request):
    if request.method =="GET":
        print("i am inside get")
        return render(request,template_name="index.html")
    else:
        print("i am insisde post")
        name = request.POST["name"]
        task = request.POST["task"]
        taskd = request.POST['taskd']
        priority = request.POST['date'] 
        tasklist.object.create(taskname = task, description= taskd, priority= priority, label= "Red")
        return render(request, template_name="index.html")  

def signup(request):
    return render(request,'signup.html')
        