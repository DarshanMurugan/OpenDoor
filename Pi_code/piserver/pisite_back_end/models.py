from django.db import models

class Recordings(models.Model):
    title = models.Charfield(max_length=150)
    save_date = models.DateTimeField(auto_add_now= True)
    recording_file = models.FileField(upload_to='recordings/')

    def __str__(self):
        return self.title


    
# Create your models here.
