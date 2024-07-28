from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Member
from .forms import MemberForm

def dashboard(request):
    members = Member.objects.all()
    members_due_soon = [member for member in members if member.is_fee_due()]
    return render(request, 'members/dashboard.html', {
        'members': members,
        'members_due_soon': members_due_soon,
    })

def reports(request):
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    total_revenue = 0

    if start_date and end_date:
        members = Member.objects.filter(fee_date__range=[start_date, end_date])
        total_revenue = sum(member.fee_amount for member in members)

    return render(request, 'members/reports.html', {
        'total_revenue': total_revenue,
        'start_date': start_date,
        'end_date': end_date,
    })

def add_member(request):
    if request.method == 'POST':
        form = MemberForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = MemberForm()
    return render(request, 'members/add_member.html', {'form': form})
