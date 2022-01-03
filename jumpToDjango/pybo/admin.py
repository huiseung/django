from django.contrib import admin
from .models import Question


class QuestAdmin(admin.ModelAdmin):
    search_fields = ['subject']


# Register your models here.
admin.site.register(Question, QuestAdmin)
