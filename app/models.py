from django.db import models
from uuid import uuid4



class UModel (models.Model) : 
    id = models.UUIDField(default=uuid4,primary_key=True,db_index=True,editable=False)
    body = models.TextField()

    class Meta:
        verbose_name = 'Model'

    def __str__(self) : 
        return str(self.id)