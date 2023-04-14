from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default = 'default.jpg', upload_to='profile_pics')
    
    def __str__(self):
        return f'{self.user.username} Profile'
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        img = Image.open(self.image.path)
        
        # Square-cropping the image
        width, height = img.size
        if width != height:
            min_size = min(width, height)
            left = (width - min_size) // 2
            top = (height - min_size) // 2
            right = (width + min_size) // 2
            bottom = (height + min_size) // 2
            img = img.crop((left, top, right, bottom))
        
        if img.height>300 or img.width>300:
            output_size = (300,300) 
            img.thumbnail(output_size)
            img.save(self.image.path)   
