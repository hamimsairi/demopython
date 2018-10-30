from django.shortcuts import render
from .models import Aktiviti 
from .forms import AktivitiForm

# Create your views here.

#Penganjur HOME######################################################################################
def home(request):
	listaktiviti = Aktiviti.objects.all()
	print(request.GET['aktivitiid'])
	#Print Data from Table
	for v in listaktiviti:
		print(v.tajuk,v.tempat,v.penceramah)

	return render(request,'penganjur/home.html')

# Tambah Penganjur######################################################################################
def add_penganjur(request):

	#add data stp kali request
	akt= Aktiviti(tajuk='Tajuk Baru', tempat='Tak Kesah', penceramah='Paon', hadpeserta=55)
	akt.save()

	return render(request,'penganjur/home.html')

#delete penganjur######################################################################################
def delete_penganjur(request,pk):

	#dptkan id aktivity n cari rekod
	aktvt = get_object_or_404(Aktiviti,pk)

	#confirm delete
	aktvt.delete()
	return render(request,'penganjur/home.html')	

# Update Penganjur######################################################################################
def update_penganjur(request,pk):

	#add data stp kali request
	akt=get_object_or_404(Aktiviti,pk)
	akt= Aktiviti(tajuk='Tajuk Baru', tempat='Tak Kesah', penceramah='Paon', hadpeserta=55)
	akt.save()

	return render(request,'penganjur/home.html')	

# Add Penganjur######################################################################################	
def penganjur_new(request):
	if request.method == "POST":
		pass
	else:
		form = AktivitiForm()
	return render(request,'penganjur/penganjur_add.html',{'form':form})	