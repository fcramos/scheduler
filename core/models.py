from django.db import models
from django.utils.translation import ugettext_lazy as _


class Scheduling(models.Model):
    STATUS = (
        (0, _('Aguardando')),
        (1, _('Enviado'))
    )
    METHODS = (
        (1, 'E-mail'),
        (2, 'SMS'),
        (3, 'Push'),
        (4, 'WhatsApp')
    )
    status = models.IntegerField(choices=STATUS, default=0)
    method = models.IntegerField(choices=METHODS)
    timestamp = models.DateTimeField()
    receiver = models.CharField(max_length=60)
    message = models.TextField()

    class Meta:
        ordering = ['-timestamp']
