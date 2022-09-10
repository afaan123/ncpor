from tkinter import CASCADE
from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from tinymce.models import HTMLField
from django.contrib.auth.models import User



class test1(models.Model):
    name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class test2(models.Model):
    name = models.CharField(max_length=255,null=True)
    designation = models.CharField(max_length=255,null=True)
    test= models.ForeignKey(User,on_delete=models.CASCADE,default="")

    def __str__(self):
        return self.name



class staff(models.Model):
    name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    email_id = models.CharField(max_length=255)
    desk_no = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    field_of_specilization= models.CharField(max_length=255,null=True)
    current_research_activities = models.CharField(max_length=255,null=True)
    content= RichTextField(null=True)#changes done by afaan
    is_featured = models.BooleanField(default=True)
    def __str__(self):
        return self.name


# Create your models here.
class readmore(models.Model):
    title = models.CharField(max_length=200,null=True)
    content = RichTextField()#changes done by afaan
    is_featured = models.BooleanField(default=True)
    def __str__(self):
        return self.title


# Create your models here.
class vessel(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextField()#changes done by afaan
    is_featured = models.BooleanField(default=True)
    def __str__(self):
        return self.title

class administrative(models.Model):
    sl_No = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    email_id = models.CharField(max_length=255,null=True)
    desk_no = models.CharField(max_length=255,null=True)
    is_featured = models.BooleanField(default=True)
    def __str__(self):
        return self.name

class finance(models.Model):
    sl_No = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    email_id = models.CharField(max_length=255,null=True)
    desk_no = models.CharField(max_length=255,null=True)
    is_featured = models.BooleanField(default=True)
    def __str__(self):
        return self.name

class procurement(models.Model):
    sl_No = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    email_id = models.CharField(max_length=255,null=True)
    desk_no = models.CharField(max_length=255,null=True)
    is_featured = models.BooleanField(default=True)
    def __str__(self):
        return self.name

class estate(models.Model):
    sl_No = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    is_featured = models.BooleanField(default=True)
    def __str__(self):
        return self.name

# Create your models here.
class e_state(models.Model):
    sr_no = models.CharField(max_length=200)
    content = RichTextField()#changes done by afaan
    is_featured = models.BooleanField(default=True)
    def __str__(self):
        return self.sr_no

# Create your models here.
class feedback(models.Model):
    sr_no = models.CharField(max_length=200)
    content = RichTextField()#changes done by afaan
    is_featured = models.BooleanField(default=True)
    def __str__(self):
        return self.content


class rit(models.Model):
    sl_No = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    download=models.URLField(blank=True)
    is_featured = models.BooleanField(default=True)
    def __str__(self):
        return self.title



class bytes(models.Model):
    title = models.CharField(max_length=255)
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/')
    is_featured = models.BooleanField(default=True)
    def __str__(self):
        return self.title


# Create your models here.
class about(models.Model):
    title = models.CharField(max_length=200)
    content =  RichTextField()#changes done by afaan
    slug = models.CharField(max_length=300)
    is_featured = models.BooleanField(default=True)
    def __str__(self):
        return self.title






# Create your models here.
class get_help(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextField()#changes done by afaan
    slug = models.CharField(max_length=300)
    is_featured = models.BooleanField(default=True)
    def __str__(self):
        return self.title





class informationResearch(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextField()#changes done by afaan
    slug = models.CharField(max_length=300)
    is_featured = models.BooleanField(default=True)
    def __str__(self):
        return self.title







class antarctic(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextField()#changes done by afaan
    slug = models.CharField(max_length=300)
    is_featured = models.BooleanField(default=True)
    def __str__(self):
        return self.title

class arctic(models.Model):
    title = models.CharField(max_length=200)
    content =  RichTextField()#changes done by afaan
    slug = models.CharField(max_length=300)
    is_featured = models.BooleanField(default=True)
    def __str__(self):
        return self.title

class southern_ocean(models.Model):
    title = models.CharField(max_length=200)
    content =  RichTextField()#changes done by afaan
    slug = models.CharField(max_length=300)
    is_featured = models.BooleanField(default=True)
    def __str__(self):
        return self.title

class himalaya(models.Model):
    title = models.CharField(max_length=200)
    content =  RichTextField()#changes done by afaan
    slug = models.CharField(max_length=300)
    is_featured = models.BooleanField(default=True)
    def __str__(self):
        return self.title



class corigendum(models.Model):
    slno=models.CharField(max_length=2)
    tenderno=models.CharField(max_length=200)
    download=models.URLField(blank=True)
    downloadname=models.CharField(max_length=300,blank=True)
    description=models.CharField(max_length=300)
    releasedate=models.DateTimeField(default=timezone.now)
    closingdate=models.DateField()
    is_featured = models.BooleanField(default=True)

    def __str__(self):
        return self.slno

class gem(models.Model):
    slno=models.CharField(max_length=2)
    tenderno=models.CharField(max_length=200)
    download=models.URLField(blank=True)
    downloadname=models.CharField(max_length=300,blank=True)
    description=models.CharField(max_length=300)
    releasedate=models.DateTimeField(default=timezone.now)
    closingdate=models.DateField()
    is_featured = models.BooleanField(default=True)
    def __str__(self):
        return self.slno
class eprocurement(models.Model):
    slno=models.CharField(max_length=2)
    tenderno=models.CharField(max_length=200)
    download=models.URLField(blank=True)
    downloadname=models.CharField(max_length=300,blank=True)
    description=models.CharField(max_length=300)
    releasedate=models.DateTimeField(default=timezone.now)
    closingdate=models.DateField()
    is_featured = models.BooleanField(default=True)
    def __str__(self):
        return self.slno

class panelment(models.Model):
    slno=models.CharField(max_length=2)
    tenderno=models.CharField(max_length=200)
    download=models.URLField(blank=True)
    downloadname=models.CharField(max_length=300,blank=True)
    description=models.CharField(max_length=300)
    releasedate=models.DateTimeField(default=timezone.now)
    closingdate=models.DateField()
    is_featured = models.BooleanField(default=True)
    def __str__(self):
        return self.slno

class enquiry(models.Model):
    slno=models.CharField(max_length=2)
    tenderno=models.CharField(max_length=200)
    download=models.URLField(blank=True)
    downloadname=models.CharField(max_length=300,blank=True)
    description=models.CharField(max_length=300)
    releasedate=models.DateTimeField(default=timezone.now)
    closingdate=models.DateField()
    is_featured = models.BooleanField(default=True)
    def __str__(self):
        return self.slno

class career(models.Model):
    slno=models.CharField(max_length=2)
    tenderno=models.CharField(max_length=200)
    download=models.URLField(blank=True)
    downloadname=models.CharField(max_length=300,blank=True)
    description=models.CharField(max_length=300)
    releasedate=models.DateTimeField(default=timezone.now)
    closingdate=models.DateField()
    is_featured = models.BooleanField(default=True)
    def __str__(self):
        return self.slno

# class research_drop(models.Model):
#     title = models.CharField(max_length=200)
#     content = models.TextField()
#     slug = models.ForeignKey(research,on_delete=models.CASCADE)
#     slug_drop = models.CharField(max_length=300,null=True)

#     def __str__(self):
#         return self.title
#     (drop-dowm-->dropdowm through cms / made by priyanshi)

class polarscience(models.Model):
    title = models.CharField(max_length=200)
    content =  RichTextField()#changes done by afaan
    slug = models.CharField(max_length=300)
    is_featured = models.BooleanField(default=True)
    def __str__(self):
        return self.title

class atmosphere(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextField()#changes done by afaan
    slug = models.CharField(max_length=300)
    is_featured = models.BooleanField(default=True)
    def __str__(self):
        return self.title

class geosciences(models.Model):
    title = models.CharField(max_length=200)
    content =  RichTextField()#changes done by afaan
    slug = models.CharField(max_length=300)
    is_featured = models.BooleanField(default=True)
    def __str__(self):
        return self.title

class polaroceans(models.Model):
    title = models.CharField(max_length=200)
    content =  RichTextField()#changes done by afaan
    slug = models.CharField(max_length=300)
    is_featured = models.BooleanField(default=True)
    def __str__(self):
        return self.title

class polarenvironments(models.Model):
    title = models.CharField(max_length=200)
    content =  RichTextField()#changes done by afaan
    slug = models.CharField(max_length=300)
    is_featured = models.BooleanField(default=True)
    def __str__(self):
        return self.title

class mineralresources(models.Model):
    title = models.CharField(max_length=200)
    content =  RichTextField()#changes done by afaan
    slug = models.CharField(max_length=300)
    is_featured = models.BooleanField(default=True)
    def __str__(self):
        return self.title

class new(models.Model):
    sno = models.CharField(max_length=300)
    description=models.CharField(max_length=300)
    content =  RichTextField()#changes done by afaan
    closingdate=models.DateField()
    is_featured = models.BooleanField(default=True)
    def __str__(self):
        return self.sno

class event(models.Model):
    sno = models.CharField(max_length=300)
    description=models.CharField(max_length=300)
    content =  RichTextField()#changes done by afaan
    closingdate=models.DateField()
    is_featured = models.BooleanField(default=True)
    def __str__(self):
        return self.sno

class data(models.Model):
    description=models.CharField(max_length=300)
    link = models.CharField(max_length=300,blank=True)
    slug = models.CharField(max_length=300)
    is_featured = models.BooleanField(default=True)
    def __str__(self):
        return self.description



# Create your models here.
class ict(models.Model):
    title = models.CharField(max_length=200)
    content =  RichTextField()#changes done by afaan
    slug = models.CharField(max_length=300)
    is_featured = models.BooleanField(default=True)

    def __str__(self):
        return self.title
