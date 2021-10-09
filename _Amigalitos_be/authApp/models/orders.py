from django.db import models
from .user import User

class Orders(models.Model):
    id = models.AutoField(primary_key=True)
    cantidad = models.IntegerField(unique=True)
    fechaPedido = models.DateTimeField()
    estadoPedido = models.CharField('Estado', max_length=30)
    user_id_fk = models.ForeignKey(User, related_name='user_id', on_delete=models.CASCADE)
    user_email_fk = models.OneToOneField(User, to_field='email', related_name='user_email', default='-', on_delete=models.CASCADE)
    user_dirFacturacion_fk = models.OneToOneField(User, to_field='dirFacturacion', related_name='user_dirFacturacion', default='-', on_delete=models.CASCADE)
    user_dirEntrega_fk = models.OneToOneField(User, to_field='dirEntrega', related_name='user_dirEntrega', default='-', on_delete=models.CASCADE)