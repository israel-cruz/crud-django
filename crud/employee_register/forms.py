from django import forms

from .models import Employee


class EmployeeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = "Select a position"
        self.fields['emp_code'].required = False

        self.fields['fullname'].widget.attrs.update({
            'placeholder': 'Enter fullname'
        })

        self.fields['phone'].widget.attrs.update({
            'placeholder': 'Enter phone number'
        })

        self.fields['emp_code'].widget.attrs.update({
            'placeholder': 'Enter employee number'
        })
    
    class Meta:
        model = Employee
        fields = '__all__'
    