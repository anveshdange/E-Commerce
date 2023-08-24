from django.db import models

class item(models.Model):
    item_id = models.AutoField
    item_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50 , default="")
    sub_category = models.CharField(max_length=50,default="")
    price = models.IntegerField(default=0)
    item_desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    image = models.ImageField(upload_to="shop/images",default="")

    def __str__(self):
        return self.item_name


class contact_us(models.Model):
    msg_id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=70)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70,default="")
    desc = models.CharField(max_length=500)

    def __str__(self):
        return self.Name