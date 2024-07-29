from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Member
from .forms import MemberForm

def dashboard(request):
    members = Member.objects.all()
    members_due_soon = [member for member in members if member.is_fee_due()]
    # make the paid status not paid
    for member in members_due_soon:
        member.status = 'not paid'
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