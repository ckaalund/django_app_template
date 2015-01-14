from django.contrib import admin
from apps.my_model.models import MyModel


@admin.register(MyModel)
class MyModelAdmin(admin.ModelAdmin):
    # list_display = ('name',)
    # search_fields = ('name',)
    # ordering = ('-created',)
