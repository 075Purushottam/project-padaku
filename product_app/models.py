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