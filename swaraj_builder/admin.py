from django.contrib import admin
from swaraj_builder.models import Project,Quest,Record
# Register your models here.

class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('id','title','address','city','created_date')
    list_display_links = ('id', 'title')
admin.site.register(Project,ProjectsAdmin)

class QuestAdmin(admin.ModelAdmin):
    list_display = ('id','first_name','phone','subject','message','enquiry_date')
    list_display_links = ('id','first_name')
admin.site.register(Quest,QuestAdmin)

class RecordAdmin(admin.ModelAdmin):
    list_display = ('id','projects_completed','happy_clients','total_tasks')
    list_display_links = ('id','projects_completed')
admin.site.register(Record,RecordAdmin)

