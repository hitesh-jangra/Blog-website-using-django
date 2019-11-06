from django.contrib import admin
from .models import Question,Answer,Blog
from django.db import models

# Register your models here.

admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Blog)