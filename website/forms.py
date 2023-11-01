from django import forms
from website.models import Record


class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ["first_name","last_name","email","phone","address","city","state","zipcode",]



    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"