from tortoise import models, fields

from src.domain.user.model import User


class UserModelMapper(models.Model):
    id = fields.IntField(pk=True)
    first_name = fields.CharField(max_length=50)
    last_name = fields.CharField(max_length=50)
    password = fields.CharField(max_length=255)

    def cast(self) -> User:
        return User(self.id, self.first_name, self.last_name, self.password)
