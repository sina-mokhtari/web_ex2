from django.contrib import admin

# Register your models here.
from .models import  Skill, Education, EducationalRecord, WorkPlace, WorkExperience, Storage, AcademicAchievement, EditRequest
from users.models import myUser
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'fullName', 'age', 'birthDate', 'gender')  # Columns to display in the admin list view
    list_filter = ('age', 'birthDate', 'gender')  # Filters to use in the admin list view
    search_fields = ('fullName',)  # Fields to search in the admin list view


class WorkExperienceAdmin(admin.ModelAdmin):
    list_display = ('fromDate', 'toDate', 'workplace')
    list_filter = ('fromDate', 'toDate')

class EducationalRecordAdmin(admin.ModelAdmin):
    list_display = ('fromDate', 'toDate', 'education')
    list_filter = ('fromDate', 'toDate')

admin.site.register(myUser, UserAdmin)
admin.site.register(Skill)
admin.site.register(Education)
admin.site.register(EducationalRecord)
admin.site.register(WorkPlace)
admin.site.register(WorkExperience, WorkExperienceAdmin)
admin.site.register(Storage)
admin.site.register(AcademicAchievement)
admin.site.register(EditRequest)