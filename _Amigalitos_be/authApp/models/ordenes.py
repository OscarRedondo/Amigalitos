from django.db import models
from .usuarios import User

class Ordenes(models.Model):
    orden_id = models.AutoField(primary_key=True)
    orden_cantidad = models.IntegerField()
    orden_fechaPedido = models.DateTimeField()
    orden_estadoPedido = models.CharField('Estado', max_length=30)
    usuario_correo = models.ForeignKey(User, related_name='usuario_correo', on_delete=models.CASCADE)
    #usuario_dirFacturacion = models.ForeignKey(User, related_name='usuario_dirFacturacion', on_delete=models.CASCADE)
    #usuario_dirEntrega = models.ForeignKey(User, related_name='usuario_dirEntrega', on_delete=models.CASCADE)