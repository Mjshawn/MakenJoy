from django.contrib import admin
from .models import Member, Comment



class CustomAdmin(admin.ModelAdmin):
    list_display = ['author','title', 'contents', 'select']
    actions = ['change']

    def change(self, request, queryset):
        updated_select = queryset.update(select='django')

admin.site.register(Member, CustomAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ['message']
admin.site.register(Comment)