from django.db import models

class Candidate(models.Model):
    user_id = models.CharField(
        max_length=256,
        unique=True, 
        primary_key=True, 
        blank=False, 
        null=False,
    )
    username = models.CharField(
        max_length=256, 
        blank=True, 
        null=True,
    )
    avatar = models.URLField(
        max_length=256,
        blank=True, 
        null=True,
    )
    votes = models.IntegerField(
        default=0
    )

    class Meta:
        db_table = "candidates"
    
    def __str__(self):
        return f"User <{self.username}:{self.user_id}>"

