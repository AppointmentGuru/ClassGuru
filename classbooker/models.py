from django.db import models

class Class(models.Model):

    def __str__(self):
        return self.name

    owner_id = models.CharField(max_length=36,blank=True, null=True)

    name = models.CharField(max_length=36,blank=True, null=True)
    description = models.TextField()

    currency = models.CharField(max_length=4,blank=True, null=True, default='ZAR')
    price = models.DecimalField(decimal_places=2, max_digits=10, default=0)

    attendance_limit = models.PositiveIntegerField(default=0, db_index=True)

    created_date = models.DateTimeField(auto_now_add=True, db_index=True)
    modified_date = models.DateTimeField(auto_now=True, db_index=True)


class ClassMember(models.Model):

    class_instance = models.ForeignKey('class', related_name='class_instance')
    user_id = models.CharField(max_length=36,blank=True, null=True)