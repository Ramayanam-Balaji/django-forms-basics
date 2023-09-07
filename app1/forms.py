from django import forms
class StudentForm(forms.Form):
    Sname=forms.CharField()
    sid=forms.IntegerField()