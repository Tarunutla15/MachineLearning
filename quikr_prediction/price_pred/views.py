# views.py
from django.shortcuts import render
from .forms import CarPriceForm

def car_price_prediction(request):
    if request.method == 'POST':
        form = CarPriceForm(request.POST)
        if form.is_valid():
            # Get form data
            company = form.cleaned_data['company']
            model = form.cleaned_data['model']
            year = form.cleaned_data['year']
            fuel = form.cleaned_data['fuel']
            kms = form.cleaned_data['kms']
            
            # Pass data to new template
            context = {
                'company': company,
                'model': model,
                'year': year,
                'fuel': fuel,
                'kms': kms
            }
            return render(request, 'prediction_result.html', context)
    else:
        form = CarPriceForm()
    
    return render(request, 'car_price_form.html', {'form': form})
