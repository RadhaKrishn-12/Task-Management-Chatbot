from django.db import models

from django.core.validators import (
    EmailValidator,
)    

from django.core.exceptions import ValidationError

def email_checker(email):
    if "@gmail.com" not in email:
        raise ValidationError("Please check your email address again.")


class Signup_Form(models.Model):
    GRADUATION = (
        ('b', 'B.Tech'),
        ('m', 'M.tech/MS'),
        ('p', 'PhD')
    )
    GENDERS = (
        ('f', 'Female'),
        ('m', 'Male'),
        ('u', 'Undisclosed')
    )

    UserName = models.CharField(primary_key = True, max_length=20, blank=False, null=False)
    Gender = models.CharField(max_length=1, choices=GENDERS, blank=False, null=False)
    Graduation = models.CharField(max_length=1, choices=GRADUATION, blank=False, null=False)
    
    def __str__(self):
        return "{}-{}".format(self.UserName, self.Graduation)
