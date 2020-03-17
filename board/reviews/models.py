from django.core.validators import validate_comma_separated_integer_list
from django.db import models

# Create your models here.
from user.models import User


class Valoration(models.Model):
    toUser = models.ForeignKey(User, related_name='to_user_valoration', on_delete=models.CASCADE,)
    fromUser = models.ForeignKey(User, related_name='from_user_valoration', on_delete=models.CASCADE)
    rate = models.FloatField(validators=[validate_comma_separated_integer_list])

    def __str__(self):
        return '{}[{}]'.format(self.toUser,self.fromUser)


class Comment(models.Model):
    toUser = models.ForeignKey(User, on_delete=models.CASCADE, related_name='to_user_comment')
    fromUser = models.ForeignKey(User, on_delete=models.CASCADE, related_name='from_user_comment')
    comment = models.TextField(max_length=500)

    def __str__(self):
        return '{}[{}]'.format(self.toUser, self.fromUser)