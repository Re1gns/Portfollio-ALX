from django.db import models

# Create your models here.

######## User profile model ########
# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)

#     avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
#     bio = models.TextField()

#     def __str__(self):
#         return self.user.username