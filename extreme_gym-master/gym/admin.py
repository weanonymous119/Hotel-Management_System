from django.contrib import admin

from . import models

admin.site.register(models.Member)
admin.site.register(models.DietChart)
admin.site.register(models.Instructor)
admin.site.register(models.Payment)
admin.site.register(models.Equipments)
admin.site.register(models.Basic_diet)