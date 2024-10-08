from django import forms
from .models import Logger

SHIFTS = (
    ("1", "Morning"),
    ("2", "Evening"),
    ("3", "Afternoon"),
)
class InputForm(forms.Form):
    first_name = forms.CharField(max_length=200, required=False, label="Full Name")
    last_name = forms.CharField(max_length=200)
    shift = forms.ChoiceField(choices=SHIFTS)
    time_log = forms.TimeField(help_text="Enter the Exact Time")

class LogForm(forms.ModelForm):
    class Meta:
        model = Logger
        fields = "__all__"
