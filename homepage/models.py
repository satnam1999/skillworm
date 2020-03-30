from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=100, unique=True)
    category_info = models.TextField()

    def __str__(self):
        return self.category_name


class Skill(models.Model):
    skill_name = models.CharField(max_length=100, unique=True)
    skill_url = models.SlugField(max_length=100, null=True, blank=True)
    img = models.ImageField(upload_to='pictures')
    skill_info = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.skill_name
