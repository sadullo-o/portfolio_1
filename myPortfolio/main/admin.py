from django.contrib import admin

from .models import Info, AboutMe, Contact, MyUsers, Blog

# Register your models here.


admin.site.register(Info)
admin.site.register(AboutMe)
admin.site.register(Contact)
admin.site.register(MyUsers)
admin.site.register(Blog)