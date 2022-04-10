from django.contrib import admin
from django.contrib import admin
from website.models import regform  
from website.models import detailform
from website.models import medical



# Register your models here.
admin.site.register(regform)
class RequestDemoAdmin(admin.ModelAdmin):
  list_display = [field.name for field in
regform._meta.get_fields()] 

admin.site.register(detailform)
class RequestDemoAdmin(admin.ModelAdmin):
  list_display = [field.name for field in
detailform._meta.get_fields()] 

admin.site.register(medical)
class RequestDemoAdmin(admin.ModelAdmin):
  list_display = [field.name for field in
medical._meta.get_fields()] 

# Register your models here.
