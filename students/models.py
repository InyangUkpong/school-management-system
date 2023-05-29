from django.db import models

# Create your models here.
class StudentClassInfo(models.Model):
    class_name = models.CharField(max_length=20)
    class_short_form = models.CharField(max_length=10)

    def __str__(self):
        return self.class_name


class StudentSectionInfo(models.Model):
    section_name = models.CharField(max_length=20)

    def __str__(self):
        return self.section_name


class StudentShiftInfo(models.Model):
    shift_name = models.CharField(max_length=100)

    def __str__(self):
        return self.shift_name


class StudentInfo(models.Model):
    academic_year = models.CharField(max_length=100)
    admission_date = models.DateField()
    admission_id = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender_choice = (
        ("male", "Male"),
        ("Female", "Female"),
    )
    
    class_type_choice =(
        ("software", "Software Engineering"),
        ("data analytics", "Data Analytics"),
        ("aws cloud", "AWS Cloud Practitioner"),
    )
    
    section_type_choice= (
        ("cohort 5", "Cohort 5"),
        ("cohort 6", "Cohort 6"),
        ("cohort 7", "Cohort 7"),
        ("cohort 8", "Cohort 8"),
        ("cohort 9", "Cohort 9"),
    )
    gender = models.CharField(choices=gender_choice, max_length=10)
    class_type = models.CharField(choices=class_type_choice, max_length=30)
    section_type = models.CharField(choices=section_type_choice, max_length=30)
    shift_type = models.ForeignKey(StudentShiftInfo, on_delete=models.CASCADE)
    student_img = models.ImageField(upload_to='photos/%Y/%m/%d/')
    fathers_name = models.CharField(max_length=100, null=True, blank=True)
    fathers_img = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    fathers_nid = models.IntegerField(unique=True, null=True, blank=True)
    fathers_number = models.IntegerField(unique=True, null=True, blank=True)
    mothers_name = models.CharField(max_length=100, null=True, blank=True)
    mothers_img = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    mothers_nid = models.IntegerField(unique=True, null=True, blank=True)
    mothers_number = models.IntegerField(null=True, blank=True)

    class Meta:
        unique_together = ["admission_id", "class_type"]

    def __str__(self):
        return self.name


class AttendanceManager(models.Manager):
    def create_attendance(self, student_class, student_id):
        student_obj = StudentInfo.objects.get(
            class_type__class_short_form=student_class,
            admission_id=student_id
        )
        attendance_obj = Attendance.objects.create(student=student_obj, status=1)
        return attendance_obj


class Attendance(models.Model):
    student = models.ForeignKey(StudentInfo, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    status = models.IntegerField(default=0)

    objects = AttendanceManager()

    class Meta:
        unique_together = ['student', 'date']

    def __str__(self):
        return self.student.admission_id

        # # for integer field
        # return str(self.student.mothers_nid)
