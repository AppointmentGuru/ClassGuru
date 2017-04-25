from django.db import models

CLASS_STATUSES = [
    ('new', 'new'),
    ('closed', 'closed'),
    ('cancelled', 'cancelled'),
]

class Class(models.Model):

    def __str__(self):
        return self.name

    owner_id = models.CharField(max_length=36,blank=True, null=True)
    title = models.CharField(max_length=36,blank=True, null=True)
    instructor_name = models.CharField(max_length=36,blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=36,blank=True, null=True, default='new', choices=CLASS_STATUSES)

    start_time = models.DateTimeField(blank=True, null=True, db_index=True)
    end_time = models.DateTimeField(blank=True, null=True, db_index=True)
    booking_close_time = models.DateTimeField(blank=True, null=True, db_index=True)

    currency = models.CharField(max_length=4,blank=True, null=True, default='ZAR')
    price = models.DecimalField(decimal_places=2, max_digits=10, default=0)

    attendance_limit = models.PositiveIntegerField(default=0, db_index=True)

    created_date = models.DateTimeField(auto_now_add=True, db_index=True)
    modified_date = models.DateTimeField(auto_now=True, db_index=True)


class ClassMember(models.Model):

    class_instance = models.ForeignKey('class', related_name='class_instance')
    user_id = models.CharField(max_length=36,blank=True, null=True)