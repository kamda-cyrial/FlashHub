from django.db import models
from schools.models import School, Course

class UserType(models.TextChoices):
    STUDENT = 'STUDENT', 'Student'
    TEACHER = 'TEACHER', 'Teacher'
    ADMIN = 'ADMIN', 'Admin'

class FriendRequestStatus(models.TextChoices):
    PENDING = 'PENDING', 'Pending'
    ACCEPTED = 'ACCEPTED', 'Accepted'
    REJECTED = 'REJECTED', 'Rejected'


# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    phone = models.CharField(max_length=100)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    courses = models.ManyToManyField(Course)
    username = models.CharField(max_length=100, unique=True)
    user_type = models.CharField(max_length=100, choices=UserType.choices, default=UserType.STUDENT)
    directory_id = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
    
    def save(self, *args, **kwargs):
        self.directory_id = f'{self.__class__.__name__}-{self.id}'
        super(User, self).save(*args, **kwargs)

class UserToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name

# class UserSession(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     session_key = models.CharField(max_length=100)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.user.first_name + ' ' + self.user.last_name

class UserCourses(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name
    
class Friends(models.Model):
    requester = models.ForeignKey(User, on_delete=models.CASCADE, related_name='requester')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
    status = models.CharField(max_length=100, choices=FriendRequestStatus.choices, default=FriendRequestStatus.PENDING)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.requester.first_name + ' ' + self.requester.last_name + ' - ' + self.receiver.first_name + ' ' + self.receiver.last_name
    
