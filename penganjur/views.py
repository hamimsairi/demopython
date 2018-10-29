from django.shortcuts import render

# Create your views here.

#Penganjur HOME
def home(request):
	return render(request,'penganjur/home.html')