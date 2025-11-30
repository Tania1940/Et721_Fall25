from django import forms

class Todolisform(forms.Form):
    text = forms.CharField(max_length=45, widget=forms.TextInput(
            attrs={
                'class': 'todo_text',
                'placeholder': 'Enter to do...',
                'aria-label': 'Todo',
                'aria-describedby': 'add-btn',
            }
        ))