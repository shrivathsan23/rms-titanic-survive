from django import forms

class Select(forms.Select):
    def create_option(self, *args, **kwargs):
        option = super().create_option(*args, **kwargs)
        if not option.get('value'):
            option['attrs']['disabled'] = True
        
        if option.get('value') == 2:
            option['attrs']['disabled'] = True
        
        return option



class SurviveForm(forms.Form):
    PCLASS_CHOICE = [('', 'Passenger Class'), (1, 'First'), (2, 'Second'), (3, 'Third')]
    SEX_CHOICE = [('', 'Sex'), ('male', 'Male'), ('female', 'Female')]
    EMBARKED_CHOICE = [('', 'Embarked'), ('c', 'Cherbourg'), ('q', 'Queenstown'), ('s', 'Southampton')]

    pclass_choice = forms.CharField(label = 'Passenger Class', widget = forms.Select(choices = PCLASS_CHOICE))
    sex_choice = forms.CharField(label = 'Sex', widget = forms.Select(choices = SEX_CHOICE))
    embarked_choice = forms.CharField(label = 'Embarked', widget = forms.Select(choices = EMBARKED_CHOICE))
    age = forms.IntegerField(min_value = 1, max_value = 99, widget = forms.NumberInput(attrs = {'placeholder': 'Age'}))
    sibsp = forms.IntegerField(max_value = 99, min_value = 0, widget = forms.NumberInput(attrs = {'placeholder': 'Siblings/Spouse'}))
    parch = forms.IntegerField(max_value = 99, min_value = 0, widget = forms.NumberInput(attrs = {'placeholder': 'Parent/Child'}))