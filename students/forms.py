from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'roll_number', 'math_marks', 'science_marks', 'english_marks']
