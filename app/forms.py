from django import forms
from app.models import Teacher, Subject, Department, Student, Fees, Expenses, Holiday, Library, Salary, Exam, Event, \
    TimeTable
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput
from simplemathcaptcha.fields import MathCaptchaField


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    captcha = MathCaptchaField()


class LoginForm(forms.Form):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())
    captcha = MathCaptchaField()


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = '__all__'


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = '__all__'


class FeesCollection(forms.ModelForm):
    class Meta:
        model = Fees
        fields = '__all__'


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expenses
        fields = '__all__'


class HolidayForm(forms.ModelForm):
    class Meta:
        model = Holiday
        fields = '__all__'


class BookForm(forms.ModelForm):
    class Meta:
        model = Library
        fields = '__all__'


class SalaryForm(forms.ModelForm):
    class Meta:
        model = Salary
        fields = '__all__'


class ExamForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = '__all__'


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'


class TimeTableForm(forms.ModelForm):
    class Meta:
        model = TimeTable
        fields = '__all__'
