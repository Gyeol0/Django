from django.db import models

# Create your models here.

class Article(models.Model):
    # 필드
    # PK(id)는 알아서 작성해줌
    title = models.CharField(max_length = 10) # char 데이터 타입, 길이 제한 지정, 길이 제한이 있을 때에는 char
    content = models.TextField() # 텍스트 데이터 타입, 길이 제한 없음, 글자 수가 많을 때
    created_at = models.DateTimeField(auto_now_add=True) # 작성 되었을 때(add)
    updated_at = models.DateTimeField(auto_now=True) # 수정 되었을 때, 저장될 때마다
