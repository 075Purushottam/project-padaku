from django.db import models
import uuid

class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True)
    price = models.IntegerField(null=False,blank=False)
    rating = models.FloatField(null=True,blank=True)
    purchase_link = models.CharField(max_length=2000,null=True,blank=True)
    check_sample_link = models.CharField(max_length=2000,null=True,blank=True)
    document = models.FileField(null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    product_image = models.ImageField(upload_to='static/styles/uploaded/', null=True,blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True,editable=False)

    def __str__(self):
        return self.title

class Features(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    feature = models.CharField(max_length=250)
    id = models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True,editable=False)

    def __str__(self):
        return self.feature

class Enquiry(models.Model):
    full_name = models.CharField(max_length=40)
    email = models.EmailField(max_length=100)
    mobile_no = models.BigIntegerField()
    address = models.CharField(max_length=100)
    getfor_choice = (
        ('school','School'),
        ('coaching','Coaching'),
        ('personal','Personal'),
        ('institution','Institution'),
        ('college','College'),
        ('other','Other'),
    )
    getfor = models.CharField(max_length=100,choices=getfor_choice)
    class_choice = (
        ('class_6','Class 6'),
        ('class_7','Class 7'),
        ('class_8','Class 8'),
        ('class_9','Class 9'),
        ('class_10','Class 10'),
        ('class_11','Class 11'),
        ('class_12','Class 12'),
    )
    Class = models.CharField(max_length=100,choices=class_choice)
    product_choice = (
        ('animation_video','Animation Video'),
        ('notes_with_mind_map','Notes with mind map'),
        ('study_notes','Study Notes'),
        ('mcq_package','MCQ Package'),
        ('attendance_tool','Attendance Tools'),
        ('exam_paper_tool','Exam Paper Tool'),
        ('ncert_solution','Ncert Solutions'),
    )
    product = models.CharField(max_length=200,choices=product_choice)

    def __str__(self):
        return self.full_name

class Feedback(models.Model):
    user_name = models.CharField(max_length=200)
    user_email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.user_name