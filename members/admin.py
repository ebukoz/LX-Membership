from django.contrib import admin
from .models import Member, Car

# Register your models here.
class MemberAdmin(admin.ModelAdmin):
    list_display = ("id","firstname", "lastname", "joined_date")

admin.site.register(Member, MemberAdmin)

class CarsAdmin(admin.ModelAdmin):
    list_display = ("name","mileage","manufacturer","year")

admin.site.register(Car, CarsAdmin)