from django.contrib import admin
from .models import Class, ClassMember

class ClassMemberInline(admin.StackedInline):
    model = ClassMember

class ClassAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'created_date')
    inlines = [ClassMemberInline]

admin.site.register(Class, ClassAdmin)
admin.site.register(ClassMember)
