from django.shortcuts import render
from django.http import HttpResponse
from .forms import SurviveForm
import os
from django.conf import settings
import pickle

def index(request):
    message = ''
    val = -1
    if request.method == 'POST':
        form = SurviveForm(request.POST)
        if form.is_valid():
            f = form.cleaned_data
            loaded = pickle.load(open(os.path.join(settings.BASE_DIR, 'survive', 'static', 'model', 'model.sav'), 'rb'))
            if f['sex_choice'] == 'male':
                val = loaded.predict([[f['pclass_choice'], f['sibsp'], f['parch'], 0, 1]])
            else:
                val = loaded.predict([[f['pclass_choice'], f['sibsp'], f['parch'], 1, 0]])
    
    form = SurviveForm()
    context = {
        'form': form,
        'val': val
    }

    return render(request, 'index.html', context)