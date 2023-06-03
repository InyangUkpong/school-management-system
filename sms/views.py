from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from students.models import StudentInfo, Attendance
from teachers.models import TeacherInfo
from django.contrib.auth.models import User

@login_required
def dashboard(request):
    all_students = StudentInfo.objects.all()
    all_teachers = TeacherInfo.objects.all()
    all_attendance = Attendance.objects.all()
    section_type_arr = []
    #attendance_count_arr = []
    
    for attendance in all_attendance:
        attendance_count = attendance.status
        section_type = attendance.student.section_type
        #attendance_count_arr.append(int(attendance_count))
        section_type_arr.append(section_type)
        
    attendance_count_dict = {item:section_type_arr.count(item) for item in section_type_arr}
    attendance_count_arr = [count for count in attendance_count_dict.values()]
    section_type_arr = [section_type for section_type in attendance_count_dict.keys()]
    
    total_students = 0
    total_teachers = 0

    logged_in_user= request.user
    
    try:
        teacher_pic = TeacherInfo.objects.filter(user=logged_in_user).first().teacher_img.url
    except (TeacherInfo.DoesNotExist, AttributeError):
        teacher_pic="https://ih1.redbubble.net/image.1380092762.9137/st,small,507x507-pad,600x600,f8f8f8.jpg"
        
    for _ in all_students:
        total_students+=1
    for _ in all_teachers:
        total_teachers+=1
        
    males = []
    females = []
    male_teachers = []
    female_teachers = []
    
    for student in all_students:
        if student.gender.lower() == "male":
            males.append(student.gender)
        else:
            females.append(student.gender)
            
    for teacher in all_teachers:
        if teacher.gender.lower() == "male":
            male_teachers.append(teacher.gender)
        else:
            female_teachers.append(teacher.gender)
        
    
    try:
        male_teachers_perc = (int(len(male_teachers))/total_teachers) * 100
    except ZeroDivisionError:
        male_teachers_perc = 0
        
    try:
        female_teachers_perc = (int(len(female_teachers))/total_teachers) * 100
    except ZeroDivisionError:
        female_teachers_perc = 0
            
    context = {
        "total": total_students,
        "males_perc": (int(len(males))/total_students) * 100,
        "females_perc": (int(len(females))/total_students) * 100,
        "male_teachers_perc": male_teachers_perc,
        "female_teachers_perc": female_teachers_perc,
        "username": request.user.username,
        "teacher_pic": teacher_pic,
        "attendance_count_arr": attendance_count_arr,
        "section_type_arr": section_type_arr
    }

   
    return render(request, "pages/dashboard.html", context=context)



