from django import forms
from Store.models import User, Product

class UserRegistrationForm(forms.ModelForm):
    """
    form for user registration.
    This form extends the default user model to include additional fields if needed.
    """
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        
        
class UserLoginForm(forms.Form):
    """
    form for user login.
    This form is used for user authentication.
    """
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name','description','price','size','image')