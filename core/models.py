from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager

# Create your models here.


class Slide(models.Model):
    title = models.CharField('標題', max_length=120)
    img = models.ImageField('輪播圖片', upload_to='uploads')
    order = models.IntegerField('排序', default=0)

    class Meta:
        ordering = ('-order', 'id')
        verbose_name = '輪播圖片'
        verbose_name_plural = '輪播圖片'

    def __str__(self):
        return self.title
    


class Post(models.Model):
    title = models.CharField('標題', max_length=120, blank=True)
    location = models.CharField('地點', max_length=120, blank=True)
    camera = models.CharField('相機型號', max_length=120, blank=True)
    img = models.ImageField('圖片', upload_to='upload', blank=True)
    time = models.IntegerField('拍攝時間', default=0, blank=True)
    created = models.DateTimeField('建立時間', auto_now_add=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        '''取得目前照片的絕對位置'''
        return reverse('details', args=[self.id,])
    
    class Meta:
        ordering = ('id',)
        verbose_name = '照片內容'
        verbose_name_plural = '照片內容'


