from django import forms
#表单文件，所有的表单类都写在这里
class ContactForm(forms.Form):
    id = forms.CharField(required=False,max_length=20, label='ID')
    one_name = forms.CharField(required=False,max_length=100,label='车牌')
    one_name.widget.attrs.update({'class': 'special'})
    one_name.widget.attrs.update(size='20')
