from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, ReadOnlyPasswordHashField
from django.contrib.auth.models import Group, Permission
from django.forms import ModelForm, ValidationError
from register.models import Student, Tutor, Review, User
#from captcha.fields import CaptchaField
from datetime import date



class RegisterForm(forms.ModelForm):
	agree_to_terms_of_service = forms.BooleanField(required=True)
	password1 = forms.CharField(label='Type your password', widget=forms.PasswordInput)
	password2 = forms.CharField(label='Confirm your password', widget=forms.PasswordInput)

	def clean_password2(self):
		# Check that the two password entries match
		password1 = self.cleaned_data.get("password1")
		password2 = self.cleaned_data.get("password2")
		if password1 and password2 and password1 != password2:
			raise forms.ValidationError("Passwords don't match")
		return password2

	class Meta:
		model = User
		fields = ['email','first_name','last_name','profile_pic']

	def save(self, commit=True):
		# Save the provided password in hashed format
		user = super(RegisterForm, self).save(commit=False)
		user.set_password(self.cleaned_data.get("password1")) #password instead of password1 if not working
		#user.active = False
		if commit:
			user.save()
		return user


class UserAdminCreationForm(forms.ModelForm):
	"""
	A form for creating new users. Includes all the required
	fields, plus a repeated password.
	"""
	password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
	password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ['email', 'first_name','last_name']

	def clean_password2(self):
		# Check that the two password entries match
		password1 = self.cleaned_data.get("password1")
		password2 = self.cleaned_data.get("password2")
		if password1 and password2 and password1 != password2:
			raise forms.ValidationError("Passwords don't match")
		return password2

	def save(self, commit=True):
		# Save the provided password in hashed format
		user = super(UserAdminCreationForm, self).save(commit=False)
		user.set_password(self.cleaned_data.get("password1"))
		if commit:
			user.save()
		return user


class UserAdminChangeForm(forms.ModelForm):
	"""A form for updating users. Includes all the fields on
	the user, but replaces the password field with admin's
	password hash display field.
	"""
	password = ReadOnlyPasswordHashField()

	class Meta:
		model = User
		fields = ['email', 'password', 'is_active', 'is_admin', 'first_name','last_name']

	def clean_password(self):
		# Regardless of what the user provides, return the initial value.
		# This is done here, rather than on the field, because the
		# field does not have access to the initial value
		return self.initial["password"]

class UpdateUser(forms.ModelForm):
	"""A form for updating users. Includes all the fields on
	the user, but replaces the password field with admin's
	password hash display field.
	"""

	class Meta:
		model = User
		fields = ['email', 'first_name','last_name', 'profile_pic']





class TutorCreation(forms.ModelForm):
	birth_date = forms.DateField(help_text="YYYY-MM-DD")

	class Meta:
		model = Tutor
		fields = ['qualifications', "birth_date", "what_you_teach", "subjects", "bio", "rates", "linkedIn", "occupation","prof_exp","teach_exp","education","availability","school","gpa","major","gender","paypal_email"]
		labels = {
			"prof_exp":"Professional Experience in years",
			"teach_exp":"Teaching Experience in years",
		}


	def clean_birth_date(self):
		birth_date = self.cleaned_data["birth_date"]
		today = date.today()
		age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
		if age < 15:
			raise ValidationError("You must be at least 15 years old")
		return birth_date

	def clean_linkdIn(self):
		linkdIn = self.cleaned_data["linkdIn"]
		url = linkdIn.split("https://www.linkedin.com/in/")
		if len(linkdIn) == 0:
			return linkdIn
		else:
			if len(url) > 2:
				raise ValidationError("This url is an invalid link")
			elif len(url) == 1:
				raise ValidationError("This url is not a LinkdIn url")
			return linkdIn

	def clean_rates(self):
		rates = self.cleaned_data.get("rates")
		if rates < 0 and rates != 0 or rates < 0.31 and rates != 0:
			raise ValidationError("Your rates are not valid")
		return rates

	def clean_prof_exp(self):
		birth_date = self.cleaned_data["birth_date"]
		prof_exp = self.cleaned_data.get("prof_exp")
		today = date.today()
		age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
		if prof_exp < 0:
			raise ValidationError("This cannot be negative")
		if prof_exp >= age:
			raise ValidationError("Age must not be greater than professional experience")
		return prof_exp

	def clean_teach_exp(self):
		birth_date = self.cleaned_data["birth_date"]
		teach_exp = self.cleaned_data.get("teach_exp")
		today = date.today()
		age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
		if teach_exp < 0:
			raise ValidationError("This cannot be negative")
		if teach_exp >= age:
			raise ValidationError("Age must not be greater than teaching experience")
		
		return teach_exp


class UpdateTutor(forms.ModelForm):
	class Meta:
		model = Tutor
		fields = ['qualifications', "birth_date", "what_you_teach", "subjects", "bio", "rates", "linkedIn", "occupation","prof_exp","teach_exp","education","availability","school","gpa","major","gender","paypal_email"]

	def clean_birth_date(self):
		birth_date = self.cleaned_data["birth_date"]
		today = date.today()
		age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
		if age < 15:
			raise ValidationError("You must be at least 15 years old")
		return birth_date

	def clean_linkdIn(self):
		linkdIn = self.cleaned_data["linkdIn"]
		url = linkdIn.split("https://www.linkedin.com/in/")
		if len(linkdIn) == 0:
			return linkdIn
		else:
			if len(url) > 2:
				raise ValidationError("This url is an invalid link")
			elif len(url) == 1:
				raise ValidationError("This url is not a LinkdIn url")
			return linkdIn

	def clean_rates(self):
		rates = self.cleaned_data.get("rates")
		if rates < 0 and rates != 0 or rates < 0.31 and rates != 0:
			raise ValidationError("Your rates are not valid")
		return rates

	def clean_prof_exp(self):
		prof_exp = self.cleaned_data.get("prof_exp")
		if prof_exp < 0:
			raise ValidationError("This cannot be negative")
		return prof_exp

	def clean_teach_exp(self):
		teach_exp = self.cleaned_data.get("teach_exp")
		if teach_exp < 0:
			raise ValidationError("This cannot be negative")
		return teach_exp


class StudentCreation(forms.ModelForm):
	class Meta:
		model = Student
		fields = ["parent_email", "birth_date"]

class UpdateStudent(forms.ModelForm):
	class Meta:
		# helper = FormHelper()
		# helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))

		# helper.form_method = 'POST'
		model = Student
		fields = ["parent_email", "birth_date"]




class CreateReview(forms.ModelForm):
	class Meta:
		model = Review
		fields = ["description", "stars"]

class ChangePassword(forms.Form):
	password1 = forms.CharField(label='Type your password', widget=forms.PasswordInput)
	password2 = forms.CharField(label='Confirm your password', widget=forms.PasswordInput)

	def clean_password2(self):
		# Check that the two password entries match
		password1 = self.cleaned_data.get("password1")
		password2 = self.cleaned_data.get("password2")
		if password1 and password2 and password1 != password2:
			raise forms.ValidationError("Passwords don't match")
		return password2

class EmailForm(forms.Form):
	email = forms.EmailField()