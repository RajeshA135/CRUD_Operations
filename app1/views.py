from django.shortcuts import render, redirect, get_object_or_404
from .models import StudentData

def index(request):
    if request.method == 'POST':
        StudentData.objects.create(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            phone=request.POST['phone'],
            address=request.POST['address']
        )
        return redirect('index')

    data = StudentData.objects.all()
    return render(request, 'index.html', {'data': data})

def edit(request, id):
    student = get_object_or_404(StudentData, pk=id)
    if request.method == 'POST':
        student.first_name = request.POST['first_name']
        student.last_name = request.POST['last_name']
        student.phone = request.POST['phone']
        student.address = request.POST['address']
        student.save()
        return redirect('index')

    return render(request, 'edit.html', {'student': student})

def delete(request, id):
    student = get_object_or_404(StudentData, pk=id)
    student.delete()
    return redirect('index')
