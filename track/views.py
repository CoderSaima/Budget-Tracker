from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import track

def trackbudget(request):
    if request.method == "POST":
        name = request.POST.get('item_name')
        description = request.POST.get('item_des')
        amount = request.POST.get('item_amount')
        income_text = request.POST.get('user_income')
        expenses_text = request.POST.get('user_expenses')

        income_val = float(income_text) if income_text else 0.0
        expenses_val = float(expenses_text) if expenses_text else 0.0
        total_cal = income_val - expenses_val

        track.objects.create(
            name=name, 
            description=description, 
            amount=amount,
            my_income=income_text,
            my_expenses=expenses_text,
            total_savings=total_cal,
            )
        return redirect("track")

    filter_type = request.GET.get('type')
    
    if filter_type == 'savings':
        # Advanced Logic: Only get entries where total_savings is greater than 1000
        all_budget = track.objects.filter(total_savings__gt=1000).order_by('-created_at')
    else:
        # Default: Fetch all records normally
        all_budget = track.objects.all().order_by('-created_at')
        
    return render(request, "index.html", {"budgets": all_budget})