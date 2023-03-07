from django.contrib import admin
from .models import Slide, Post

# Register your models here.



@admin.register(Slide)
class SlideAdmin(admin.ModelAdmin):
    '''首頁輪播圖管理後台'''
    list_display = ('title', 'order')
    link_fields = ('link')
    list_editable = ('order',)
    ordering = ('-order', 'id')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
     '''照片內容後台管理'''
     list_display = ('title', 'location', )
     ordering = ('-created',)
