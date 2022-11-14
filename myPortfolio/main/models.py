from django.db import models

# Create your models here.
class Info(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Xabar'
        verbose_name_plural = 'Xabarlar'



class AboutMe(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField()
    mansab = models.CharField(max_length=250)
    malumot = models.TextField()
    type = models.CharField(max_length=100, default='about')
    state = models.IntegerField(max_length=10, default=1)
    # contact_id = models.IntegerField(max_length=10, default=None)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'xodim'
        verbose_name_plural = 'Xodimlar'


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=250)
    subject = models.CharField(max_length=250)
    message = models.TextField()

    def __str__(self):
        return self.name


class MyUsers(models.Model):
    username = models.CharField('Username', max_length=100)
    password = models.CharField('Password', max_length=100)
    phone_number = models.CharField('Phone Number', max_length=100, default='')
    full_name = models.CharField('Full Name', max_length=100, default='')
    image = models.ImageField(default='blank-profile-picture-973460_1280.jpg')
    about = models.CharField(max_length=250, default='')
    facebook = models.CharField(max_length=250, default='')
    twitter = models.CharField(max_length=250, default='')
    instagram = models.CharField(max_length=250, default='')


    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'My Users'

class Blog(models.Model):
    title = models.CharField(max_length=100)
    blog = models.TextField()
    username = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
