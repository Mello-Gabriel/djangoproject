from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect, get_object_or_404
from datetime import date

from .models import Member
from .forms import MemberForm


def members(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('members/all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))
  
def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('members/details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))


def main(request):
    template = loader.get_template("members/main.html")
    return HttpResponse(template.render({}, request))

def add_member(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            member = form.save(commit=False)
            member.joined_date = date.today()
            member.save()
            return redirect('members')  # Redireciona para a lista de membros após adicionar
    else:
        form = MemberForm()
    return render(request, 'members/add_member.html', {'form': form})

def edit_member(request, id):
    member = get_object_or_404(Member, pk=id)

    if request.method == 'POST':
        form = MemberForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return redirect('details', id=member.id)
    else:
        form = MemberForm(instance=member)

    return render(request, 'members/add_member.html', {'form': form, 'member': member})
    
