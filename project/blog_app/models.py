from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    author = models.CharField(max_length=100)
    date = models.DateField()
    image = models.ImageField(upload_to='blog/images/')
    
    def __str__(self):
        return self.title
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    
    def __str__(self):
        return self.name
class Comment(models.Model):
    post = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    date = models.DateField(auto_now_add=True)
    active = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['date']
    
    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)    