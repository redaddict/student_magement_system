from django.shortcuts import render,redirect
from django.core.exceptions import MultipleObjectsReturned
from student.models import Details

# Create your views here.
def home(request):
    return render(request,'student/home.html')
def record(request):
    data=Details.objects.all()
    context={
        'data':data
    }
    return render(request,'student/record.html',context)
def registration(request):
    if request.method=='POST':
        st_id = request.POST.get('st_id')
        name = request.POST.get('name')
        mob = request.POST.get('mbl')
        city = request.POST.get('city')
        clg = request.POST.get('college')
        degree = request.POST.get('degree')
        year = request.POST.get('year')
        course = request.POST.get('course')
        data=Details(stu_id=st_id,name=name,mob=mob,city=city,college=clg,degree=degree,year=year,course=course)
        data.save()
    return render(request,'student/registration.html')

def update(request,id):
    # data=Details.objects.filter(stu_id=id)
    try:
        # Attempt to retrieve the first object with the given stu_id
        data = Details.objects.filter(stu_id=id).first()
    except MultipleObjectsReturned:
        # Handle the case where multiple objects are returned
        # Here, you may choose to log the error, handle it differently, or simply ignore it
        # For simplicity, we'll handle it by getting the first object from the queryset
        data = Details.objects.filter(stu_id=id).order_by('id').first()
    context={
        'data':data
    }
    if request.method=='POST':
        st_id = request.POST.get('st_id')
        name = request.POST.get('name')
        mob = request.POST.get('mbl')
        city = request.POST.get('city')
        clg = request.POST.get('college')
        degree = request.POST.get('degree')
        year = request.POST.get('year')
        course = request.POST.get('course')
        

        data.stu_id=st_id
        data.name=name
        data.mob=mob
        data.city=city
        data.college=clg
        data.degree=degree
        data.year=year
        data.course=course
        data.save()
    return render(request,'student/update.html',context)

def delete(request,id):
    # data=Details.objects.get(stu_id=id)
    try:
        # Attempt to retrieve the first object with the given stu_id
        data = Details.objects.filter(stu_id=id).first()
    except MultipleObjectsReturned:
        # Handle the case where multiple objects are returned
        # Here, you may choose to log the error, handle it differently, or simply ignore it
        # For simplicity, we'll handle it by getting the first object from the queryset
        data = Details.objects.filter(stu_id=id).order_by('id').first()
    data.delete()
    return redirect('/record/')

def about(request):
    return render(request,'student/about.html')

def python(request):
    return render(request,'student/python.html')
def java(request):
    return render(request,'student/java.html')
def aws(request):
    return render(request,'student/aws.html')


