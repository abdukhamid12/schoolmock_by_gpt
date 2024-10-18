from django.contrib import admin

from .models import *

admin.site.register(School)
admin.site.register(ClassGroup)
admin.site.register(Student)
admin.site.register(Test)
admin.site.register(Question)
admin.site.register(AnswerOption)
admin.site.register(StudentAnswer)