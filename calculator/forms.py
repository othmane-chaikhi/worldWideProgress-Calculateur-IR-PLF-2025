from django import forms

class SalaryCalculationForm(forms.Form):
    salaire_base = forms.FloatField(
        label='Salaire de Base (MAD)',
        min_value=0,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ex: 10000',
            'step': '0.01'
        })
    )
    
    primes_conges = forms.FloatField(
        label='Primes et Congés (MAD)',
        min_value=0,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ex: 1000',
            'step': '0.01'
        })
    )
    
    indemnite_exoneree = forms.FloatField(
        label='Indemnité Exonérée (MAD)',
        min_value=0,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ex: 500',
            'step': '0.01'
        })
    )
    
    nb_charge_familiale = forms.IntegerField(
        label='Nombre de Charges Familiales',
        min_value=0,
        max_value=10,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ex: 2'
        })
    )