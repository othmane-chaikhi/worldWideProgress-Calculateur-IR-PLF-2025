from django.db import models
from django.utils import timezone

class SalaryCalculation(models.Model):
    # Input fields
    salaire_base = models.FloatField()
    primes_conges = models.FloatField()
    indemnite_exoneree = models.FloatField()
    nb_charge_familiale = models.IntegerField()
    
    # Calculated fields
    salaire_brut = models.FloatField()
    salaire_brut_imposable = models.FloatField()
    cnss = models.FloatField()
    amo = models.FloatField()
    mutuelle = models.FloatField()
    frais_professionnels = models.FloatField()
    salaire_net_imposable = models.FloatField()
    ir_brut = models.FloatField()
    charge_famille = models.FloatField()
    ir_net = models.FloatField()
    salaire_net = models.FloatField()
    
    # Metadata
    created_at = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Calculation {self.id} - {self.created_at.strftime('%Y-%m-%d %H:%M')}"