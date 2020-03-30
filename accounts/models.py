from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

# Create your models here.
class UserType(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    teacher = models.BooleanField(default=False)
    student = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

class UserData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default="")
    address = models.TextField()
    phone_number = models.CharField(max_length=10, validators=[RegexValidator(r'^\d[0123456789]{9}$')])
    city_ch = (
        ('Mumbai','Mumbai'),
        ('Delhi','Delhi'),
        ('Banglore','Banglore'),
    )
    city = models.CharField(max_length= 25 ,choices=city_ch, default='none')
    pincode = models.CharField(max_length=6, default="",validators=[RegexValidator(r'^\d[0123456789]{5}$')])
    id_proof = models.ImageField(upload_to='images/',default="")
    show_id = models.IntegerField(unique=True, null=False,default=1)
    decr = models.TextField(default='')


    def __str_(self):
        return self.user.username

class TutorCourse(models.Model):
    user = models.ForeignKey(User, related_name='tutorcor', on_delete=models.CASCADE)
    course = models.CharField(max_length=50)

class course(models.Model):
    student = models.ManyToManyField(User, blank= True, related_name='enrolled_students')
    tutor = models.ManyToManyField(User,  blank= True, related_name='Course_Tutors')
    cr_id = models.ManyToManyField(TutorCourse,  blank= True,related_name='Course')

class Review(models.Model):
   user = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE)
   review = models.TextField()
   rating = models.CharField(max_length=1)

class ReviewInline(admin.StackedInline):
    model = Review

class UserAdmin(admin.ModelAdmin):
    inlines = [
        ReviewInline,
    ]


    