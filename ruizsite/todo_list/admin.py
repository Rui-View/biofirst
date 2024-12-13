# from django.contrib import admin
# from .models import Todo

# # Register your models here.
# admin.site.register(Todo)

from django.contrib import admin
from .models import Todo

@admin.action(description='Mark selected Todos as Completed')
def mark_completed(modeladmin, request, queryset):
    queryset.update(description='Completed')  # 将 description 更新为 "Completed"

class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'deadline')  # 显示字段
    actions = [mark_completed]  # 注册自定义操作

admin.site.register(Todo, TodoAdmin)
