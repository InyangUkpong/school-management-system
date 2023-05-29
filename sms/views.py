from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from students.models import StudentInfo

@login_required
def index(request):
    all_students = StudentInfo.objects.all()
    total_students = 0
    for _ in all_students:
        total_students+=1
    males = []
    females = []
    for student in all_students:
        if student.gender.lower() == "male":
            males.append(student.gender)
        else:
            females.append(student.gender)
            
    print((int(len(females))/total_students) * 100)
            
    context = {
        "total": total_students,
        "males_perc": (int(len(males))/total_students) * 100,
        "females_perc": (int(len(females))/total_students) * 100,
        "username": request.user.username
    }
    
    
    return render(request, "home.html", context=context)



