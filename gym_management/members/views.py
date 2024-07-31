from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Member,FeePayment
from .forms import MemberForm,FeePaymentForm
from django.utils.dateparse import parse_date


def dashboard(request):
    members = Member.objects.all()
    members_due_soon = [member for member in members if member.is_fee_due()]
    # make the paid status not paid
    for member in members_due_soon:
        if member.status != 'due':
            member.status = 'due'
            member.save()
    return render(request, 'members/dashboard.html', {
        'members': members,
        'members_due_soon': members_due_soon,
    })


def reports(request):
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    total_revenue = 0
    payments = []
    if start_date and end_date:
        payments = FeePayment.objects.filter(date__range=[start_date, end_date])
        total_revenue = sum(payment.amount for payment in payments)

    return render(request, 'members/reports.html', {
        'total_revenue': total_revenue,
        'start_date': start_date,
        'end_date': end_date,
        'payments': payments,
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

def update_member(request,pk):
    member = get_object_or_404(Member,pk=pk)
    if request.method=="POST":
        form = MemberForm(request.POST,request.FILES,instance=member)
        if form.is_valid():
            form.save()
            return redirect('member_details',pk=pk)
    else:
        form= MemberForm(instance=member)
    return render(request,'members/update_member.html',{'form':form})
    
     

def member_details(request, pk):
    members = get_object_or_404(Member,pk=pk)
    return render(request, 'members/member_details.html', {'members': members   })

def delete_member(request,pk):
    member = get_object_or_404(Member,pk= pk)
    if request.method == 'POST':
        member.delete()
        return redirect('dashboard')
    return render(request,'members/delete_,member.html',{'member':member})

def add_payment(request, pk):
    member = get_object_or_404(Member, pk=pk)
    if request.method == 'POST':
        form = FeePaymentForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.member = member
            payment.save()
            member.status = 'paid'
            member.fee_date = payment.date
            member.save()
            return redirect('dashboard')
    else:
        form = FeePaymentForm()
    return render(request, 'members/add_payment.html', {'form': form, 'member': member})