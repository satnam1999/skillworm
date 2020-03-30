from django.contrib import admin
from .models import UserType
from .models import UserData
from .models import TutorCourse
from .models import course
from .models import UserType
from .models import Review


# Register your models here.
admin.site.register(UserType)
admin.site.register(UserData)
admin.site.register(TutorCourse)
admin.site.register(course)
admin.site.register(Review)

