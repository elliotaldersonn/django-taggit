from .models import DemoFormm
from django import forms

class CreateForm(forms.ModelForm):
	
	class Meta:
		model = DemoFormm
		fields = ['name' , 'msg' , 'img','tags',]

			

