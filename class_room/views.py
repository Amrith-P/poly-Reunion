from django.shortcuts import render, redirect
from class_room.models import *
from django.db import IntegrityError
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


def list_benches(request):
    bench11 = Bench11.objects.all()
    bench12 = Bench12.objects.all()
    bench13 = Bench13.objects.all()
    bench14 = Bench14.objects.all()
    bench15 = Bench15.objects.all()
    bench21 = Bench21.objects.all()
    bench22 = Bench22.objects.all()
    bench23 = Bench23.objects.all()
    bench24 = Bench24.objects.all()
    bench25 = Bench25.objects.all()
    bench26 = Bench26.objects.all()
    bench31 = Bench31.objects.all()
    bench32 = Bench32.objects.all()
    bench33 = Bench33.objects.all()
    bench34 = Bench34.objects.all()
    bench35 = Bench35.objects.all()
    bench41 = Bench41.objects.all()
    bench42 = Bench42.objects.all()
    bench43 = Bench43.objects.all()
    bench44 = Bench44.objects.all()
    bench45 = Bench45.objects.all()
    


    context = {
        'bench11': bench11,
        'bench12': bench12,
        'bench13': bench13,
        'bench14': bench14,
        'bench15': bench15,
        'bench21': bench21,
        'bench22': bench22,
        'bench23': bench23,
        'bench24': bench24,
        'bench25': bench25,
        'bench26': bench26,
        'bench31': bench31,
        'bench32': bench32,
        'bench33': bench33,
        'bench34': bench34,
        'bench35': bench35,
        'bench41': bench41,
        'bench42': bench42,
        'bench43': bench43,
        'bench44': bench44,
        'bench45': bench45,



    }
    return render(request, 'index.html', context)


def edit_bench11(request, bench_id):
    bench11 = Bench11.objects.get(id=bench_id)

    if request.method == 'POST':
        student_name = request.POST.get('student_name')
        student_image = request.FILES.get('student_image')
        bench11.student_name = student_name
        bench11.student_image = student_image
        try:
            bench11.save()
            messages.success(request, f" '{bench11.student_name}' Details Added Successfully")
            return redirect('/')
        except IntegrityError:
            messages.error(request, f" '{bench11.student_name}' Field")
            return redirect('edit_bench11', bench_id=bench_id)
    context = {
        'bench11': bench11,
    }
    return render(request, 'edit_bench11.html', context)

def edit_bench12(request, bench_id):
    bench12 = Bench12.objects.get(id=bench_id)

    if request.method == 'POST':
        student_name = request.POST.get('student_name')
        student_image = request.FILES.get('student_image')
        bench12.student_name = student_name
        bench12.student_image = student_image
        try:
            bench12.save()
            messages.success(request, f" '{bench12.student_name}' Details Added Successfully")
            return redirect('/')
        except IntegrityError:
            messages.error(request, f" '{bench12.student_name}' Field")
            return redirect('edit_bench12', bench_id=bench_id)
    context = {
        'bench12': bench12,
    }
    return render(request, 'edit_bench12.html', context)    

def edit_bench13(request, bench_id):
    bench13 = Bench13.objects.get(id=bench_id)

    if request.method == 'POST':
        student_name = request.POST.get('student_name')
        student_image = request.FILES.get('student_image')
        bench13.student_name = student_name
        bench13.student_image = student_image
        try:
            bench13.save()
            messages.success(request, f" '{bench13.student_name}' Details Added Successfully")
            return redirect('/')
        except IntegrityError:
            messages.error(request, f" '{bench13.student_name}' Field")
            return redirect('edit_bench13', bench_id=bench_id)
    context = {
        'bench13': bench13,
    }
    return render(request, 'edit_bench13.html', context)

def edit_bench14(request, bench_id):
    bench14 = Bench14.objects.get(id=bench_id)

    if request.method == 'POST':
        student_name = request.POST.get('student_name')
        student_image = request.FILES.get('student_image')
        bench14.student_name = student_name
        bench14.student_image = student_image
        try:
            bench14.save()
            messages.success(request, f" '{bench14.student_name}' Details Added Successfully")
            return redirect('/')
        except IntegrityError:
            messages.error(request, f" '{bench14.student_name}' Field")
            return redirect('edit_bench14', bench_id=bench_id)
    context = {
        'bench14': bench14,
    }
    return render(request, 'edit_bench14.html', context)

def edit_bench15(request, bench_id):
    bench15 = Bench15.objects.get(id=bench_id)

    if request.method == 'POST':
        student_name = request.POST.get('student_name')
        student_image = request.FILES.get('student_image')
        bench15.student_name = student_name
        bench15.student_image = student_image
        try:
            bench15.save()
            messages.success(request, f" '{bench15.student_name}' Details Added Successfully")
            return redirect('/')
        except IntegrityError:
            messages.error(request, f" '{bench15.student_name}' Field")
            return redirect('edit_bench15', bench_id=bench_id)
    context = {
        'bench15': bench15,
    }
    return render(request, 'edit_bench15.html', context) 

def edit_bench21(request, bench_id):
    bench21 = Bench21.objects.get(id=bench_id)

    if request.method == 'POST':
        student_name = request.POST.get('student_name')
        student_image = request.FILES.get('student_image')
        bench21.student_name = student_name
        bench21.student_image = student_image
        try:
            bench21.save()
            messages.success(request, f" '{bench21.student_name}' Details Added Successfully")
            return redirect('/')
        except IntegrityError:
            messages.error(request, f" '{bench21.student_name}' Field")
            return redirect('edit_bench21', bench_id=bench_id)
    context = {
        'bench21': bench21,
    }
    return render(request, 'edit_bench21.html', context)  

def edit_bench22(request, bench_id):
    bench22 = Bench22.objects.get(id=bench_id)

    if request.method == 'POST':
        student_name = request.POST.get('student_name')
        student_image = request.FILES.get('student_image')
        bench22.student_name = student_name
        bench22.student_image = student_image
        try:
            bench22.save()
            messages.success(request, f" '{bench22.student_name}' Details Added Successfully")
            return redirect('/')
        except IntegrityError:
            messages.error(request, f" '{bench22.student_name}' Field")
            return redirect('edit_bench22', bench_id=bench_id)
    context = {
        'bench22': bench22,
    }
    return render(request, 'edit_bench22.html', context)      

def edit_bench23(request, bench_id):
    bench23 = Bench23.objects.get(id=bench_id)

    if request.method == 'POST':
        student_name = request.POST.get('student_name')
        student_image = request.FILES.get('student_image')
        bench23.student_name = student_name
        bench23.student_image = student_image
        try:
            bench23.save()
            messages.success(request, f" '{bench23.student_name}' Details Added Successfully")
            return redirect('/')
        except IntegrityError:
            messages.error(request, f" '{bench23.student_name}' Field")
            return redirect('edit_bench23', bench_id=bench_id)
    context = {
        'bench23': bench23,
    }
    return render(request, 'edit_bench23.html', context) 

def edit_bench24(request, bench_id):
    bench24 = Bench24.objects.get(id=bench_id)

    if request.method == 'POST':
        student_name = request.POST.get('student_name')
        student_image = request.FILES.get('student_image')
        bench24.student_name = student_name
        bench24.student_image = student_image
        try:
            bench24.save()
            messages.success(request, f" '{bench24.student_name}' Details Added Successfully")
            return redirect('/')
        except IntegrityError:
            messages.error(request, f" '{bench24.student_name}' Field")
            return redirect('edit_bench24', bench_id=bench_id)
    context = {
        'bench24': bench24,
    }
    return render(request, 'edit_bench24.html', context)      

def edit_bench25(request, bench_id):
    bench25 = Bench25.objects.get(id=bench_id)

    if request.method == 'POST':
        student_name = request.POST.get('student_name')
        student_image = request.FILES.get('student_image')
        bench25.student_name = student_name
        bench25.student_image = student_image
        try:
            bench25.save()
            messages.success(request, f" '{bench25.student_name}' Details Added Successfully")
            return redirect('/')
        except IntegrityError:
            messages.error(request, f" '{bench25.student_name}' Field")
            return redirect('edit_bench25', bench_id=bench_id)
    context = {
        'bench25': bench25,
    }
    return render(request, 'edit_bench25.html', context)  

def edit_bench26(request, bench_id):
    bench26 = Bench26.objects.get(id=bench_id)

    if request.method == 'POST':
        student_name = request.POST.get('student_name')
        student_image = request.FILES.get('student_image')
        bench26.student_name = student_name
        bench26.student_image = student_image
        try:
            bench26.save()
            messages.success(request, f" '{bench26.student_name}' Details Added Successfully")
            return redirect('/')
        except IntegrityError:
            messages.error(request, f" '{bench26.student_name}' Field")
            return redirect('edit_bench26', bench_id=bench_id)
    context = {
        'bench26': bench26,
    }
    return render(request, 'edit_bench26.html', context)        














def edit_bench31(request, bench_id):
    bench31 = Bench31.objects.get(id=bench_id)

    if request.method == 'POST':
        student_name = request.POST.get('student_name')
        student_image = request.FILES.get('student_image')
        bench31.student_name = student_name
        bench31.student_image = student_image
        try:
            bench31.save()
            messages.success(request, f" '{bench31.student_name}' Details Added Successfully")
            return redirect('/')
        except IntegrityError:
            messages.error(request, f" '{bench31.student_name}' Field")
            return redirect('edit_bench31', bench_id=bench_id)
    context = {
        'bench31': bench31,
    }
    return render(request, 'edit_bench31.html', context)

def edit_bench32(request, bench_id):
    bench32 = Bench32.objects.get(id=bench_id)

    if request.method == 'POST':
        student_name = request.POST.get('student_name')
        student_image = request.FILES.get('student_image')
        bench32.student_name = student_name
        bench32.student_image = student_image
        try:
            bench32.save()
            messages.success(request, f" '{bench32.student_name}' Details Added Successfully")
            return redirect('/')
        except IntegrityError:
            messages.error(request, f" '{bench32.student_name}' Field")
            return redirect('edit_bench32', bench_id=bench_id)
    context = {
        'bench32': bench32,
    }
    return render(request, 'edit_bench32.html', context)    

def edit_bench33(request, bench_id):
    bench33 = Bench33.objects.get(id=bench_id)

    if request.method == 'POST':
        student_name = request.POST.get('student_name')
        student_image = request.FILES.get('student_image')
        bench33.student_name = student_name
        bench33.student_image = student_image
        try:
            bench33.save()
            messages.success(request, f" '{bench33.student_name}' Details Added Successfully")
            return redirect('/')
        except IntegrityError:
            messages.error(request, f" '{bench33.student_name}' Field")
            return redirect('edit_bench33', bench_id=bench_id)
    context = {
        'bench33': bench33,
    }
    return render(request, 'edit_bench33.html', context)

def edit_bench34(request, bench_id):
    bench34 = Bench34.objects.get(id=bench_id)

    if request.method == 'POST':
        student_name = request.POST.get('student_name')
        student_image = request.FILES.get('student_image')
        bench34.student_name = student_name
        bench34.student_image = student_image
        try:
            bench34.save()
            messages.success(request, f" '{bench34.student_name}' Details Added Successfully")
            return redirect('/')
        except IntegrityError:
            messages.error(request, f" '{bench34.student_name}' Field")
            return redirect('edit_bench34', bench_id=bench_id)
    context = {
        'bench34': bench34,
    }
    return render(request, 'edit_bench34.html', context)

def edit_bench35(request, bench_id):
    bench35 = Bench35.objects.get(id=bench_id)

    if request.method == 'POST':
        student_name = request.POST.get('student_name')
        student_image = request.FILES.get('student_image')
        bench35.student_name = student_name
        bench35.student_image = student_image
        try:
            bench35.save()
            messages.success(request, f" '{bench35.student_name}' Details Added Successfully")
            return redirect('/')
        except IntegrityError:
            messages.error(request, f" '{bench35.student_name}' Field")
            return redirect('edit_bench35', bench_id=bench_id)
    context = {
        'bench35': bench35,
    }
    return render(request, 'edit_bench35.html', context) 

def edit_bench41(request, bench_id):
    bench41 = Bench41.objects.get(id=bench_id)

    if request.method == 'POST':
        student_name = request.POST.get('student_name')
        student_image = request.FILES.get('student_image')
        bench41.student_name = student_name
        bench41.student_image = student_image
        try:
            bench41.save()
            messages.success(request, f" '{bench41.student_name}' Details Added Successfully")
            return redirect('/')
        except IntegrityError:
            messages.error(request, f" '{bench41.student_name}' Field")
            return redirect('edit_bench41', bench_id=bench_id)
    context = {
        'bench41': bench41,
    }
    return render(request, 'edit_bench41.html', context)  

def edit_bench42(request, bench_id):
    bench42 = Bench42.objects.get(id=bench_id)

    if request.method == 'POST':
        student_name = request.POST.get('student_name')
        student_image = request.FILES.get('student_image')
        bench42.student_name = student_name
        bench42.student_image = student_image
        try:
            bench42.save()
            messages.success(request, f" '{bench42.student_name}' Details Added Successfully")
            return redirect('/')
        except IntegrityError:
            messages.error(request, f" '{bench42.student_name}' Field")
            return redirect('edit_bench42', bench_id=bench_id)
    context = {
        'bench42': bench42,
    }
    return render(request, 'edit_bench42.html', context)      

def edit_bench43(request, bench_id):
    bench43 = Bench43.objects.get(id=bench_id)

    if request.method == 'POST':
        student_name = request.POST.get('student_name')
        student_image = request.FILES.get('student_image')
        bench43.student_name = student_name
        bench43.student_image = student_image
        try:
            bench43.save()
            messages.success(request, f" '{bench43.student_name}' Details Added Successfully")
            return redirect('/')
        except IntegrityError:
            messages.error(request, f" '{bench43.student_name}' Field")
            return redirect('edit_bench43', bench_id=bench_id)
    context = {
        'bench43': bench43,
    }
    return render(request, 'edit_bench23.html', context) 

def edit_bench44(request, bench_id):
    bench44 = Bench44.objects.get(id=bench_id)

    if request.method == 'POST':
        student_name = request.POST.get('student_name')
        student_image = request.FILES.get('student_image')
        bench44.student_name = student_name
        bench44.student_image = student_image
        try:
            bench44.save()
            messages.success(request, f" '{bench44.student_name}' Details Added Successfully")
            return redirect('/')
        except IntegrityError:
            messages.error(request, f" '{bench44.student_name}' Field")
            return redirect('edit_bench44', bench_id=bench_id)
    context = {
        'bench44': bench44,
    }
    return render(request, 'edit_bench44.html', context)      

def edit_bench45(request, bench_id):
    bench45 = Bench45.objects.get(id=bench_id)

    if request.method == 'POST':
        student_name = request.POST.get('student_name')
        student_image = request.FILES.get('student_image')
        bench45.student_name = student_name
        bench45.student_image = student_image
        try:
            bench45.save()
            messages.success(request, f" '{bench45.student_name}' Details Added Successfully")
            return redirect('/')
        except IntegrityError:
            messages.error(request, f" '{bench45.student_name}' Field")
            return redirect('edit_bench45', bench_id=bench_id)
    context = {
        'bench45': bench45,
    }
    return render(request, 'edit_bench45.html', context)        