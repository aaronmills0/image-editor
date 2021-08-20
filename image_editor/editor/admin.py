from django.contrib import admin
from .models import Image, Feedback

# Register your models here.
admin.site.register(Image)

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'body', 'created_on')
    list_filter = ('created_on',)
    search_fields = ('name', 'email', 'body')
admin.site.register(Feedback, FeedbackAdmin)
