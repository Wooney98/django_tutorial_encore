from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Article(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    contents = models.TextField()
    url = models.URLField()
    email = models.EmailField()
    cdate = models.DateTimeField(auto_now_add = True)# data가 create되는 시스템상의 시점
    mdate = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name_plural = "아티클 작성하기"
        ordering = ('-mdate',)
    def __str__(self):
        return f"{self.title} -- {self.name} -- {self.cdate}"
    def get_absolute_url(self): 
        return reverse('community:view_detail', args=(self.id,))
        # reverse()함수를 통해 모델의 개별 데이터 url을 문자열로 반환
