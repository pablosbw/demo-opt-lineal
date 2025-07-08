from django import forms

class UploadForm(forms.Form):
    file = forms.FileField()
    max_prod_a = forms.IntegerField(required= False, min_value=0, label="Cantidad Máxima a producir de A (opcional)")
    max_prod_b = forms.IntegerField(required= False, min_value=0, label="Cantidad Máxima a producir de B (opcional)")
    