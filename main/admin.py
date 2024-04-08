from django.contrib import admin
from .models import Material, Section, Test, Answer


admin.site.register(Material)
admin.site.register(Section)
admin.site.register(Test)
admin.site.register(Answer)