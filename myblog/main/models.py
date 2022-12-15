# from django.db import models
# from django.contrib.auth.models import User
# from django.urls import reverse
# from django.db.models.signals import post_save
# from django.dispatch import receiver
#
#
# class Comments(models.Model):
#     post = models.ForeignKey('Posts', on_delete=models.CASCADE)
#     commentator_name = models.OneToOneField('Profile', on_delete=models.CASCADE)
#     comment = models.TextField()
#
#     def __str__(self):
#         return self.comment
#
#
# class Rating(models.Model):
#     post = models.ForeignKey('Posts', on_delete=models.CASCADE, related_name='+')
#     likes = models.IntegerField(default=0)
#     dislikes = models.IntegerField(default=0)
#
#     def __str__(self):
#         return self.likes, self.dislikes
#
#
# class Posts(models.Model):
#     username = models.OneToOneField('Profile', on_delete=models.CASCADE)
#     post_name = models.CharField(max_length=155)
#     rating = models.ForeignKey('Rating', on_delete=models.PROTECT)
#     comment = models.OneToOneField('Comments', on_delete=models.PROTECT)
#     is_published = models.BooleanField(default=None)
#     published_time = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return self.username
#
#     def get_absolute_url(self):
#         return reverse('post', kwargs={'post_id': self.pk})
#
#
# class Profile(models.Model):
#     username = models.OneToOneField('User', on_delete=models.CASCADE)
#     post = models.ForeignKey('Posts', on_delete=models.PROTECT, null=True, blank=True)
#     avatar = models.ImageField(upload_to='profile/', default='default.png')
#     bio = models.TextField()
#
#     @receiver(post_save, sender=User)  # add this
#     def create_user_profile(sender, instance, created, **kwargs):
#         if created:
#             Profile.objects.create(user=instance)
#
#     @receiver(post_save, sender=User)  # add this
#     def save_user_profile(sender, instance, **kwargs):
#         instance.profile.save()
#
#     def __str__(self):
#         return self.username
#
#     def get_absolute_url(self):
#         return reverse('user', kwargs={'user_id': self.pk})

