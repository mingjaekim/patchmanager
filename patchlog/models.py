from django.db import models

class Patch(models.Model):
    author = models.CharField(max_length=100, verbose_name="작성자")
    description = models.TextField(verbose_name="수정 설명")
    patch_file = models.FileField(upload_to='patches/', verbose_name="패치 zip 파일")
    zip_name = models.CharField(max_length=50, verbose_name="최종 zip 이름")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="등록일")

    def __str__(self):
        return f"{self.author} - {self.created_at.strftime('%Y-%m-%d %H:%M')}"
