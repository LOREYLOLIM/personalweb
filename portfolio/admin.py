from django.contrib import admin
from .models import Update,About,Contact,Testimonial,Home

# Register your models here.
admin.site.register(Home)
admin.site.register(About)
admin.site.register(Contact)
admin.site.register(Testimonial)
admin.site.register(Update)
