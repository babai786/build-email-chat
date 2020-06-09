from django.db import models

# Create your models here.
# maichimp  email= mukher....   username = babai0786   password = Mukherjee@1122




class  Signup(models.Model):
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.email





