from datetime import date

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.template import loader

from .forms import MemberForm
from .models import Member


def members(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template("members/all_members.html")
    context = {"mymembers": mymembers}
    total_members = mymembers.count()
    return HttpResponse(template.render(context, request))


def details(request, id):
    mymember = Member.objects.get(id=id)
    template = loader.get_template("members/details.html")
    context = {
        "mymember": mymember,
    }
    return HttpResponse(template.render(context, request))


def main(request):
    template = loader.get_template("members/main.html")
    return HttpResponse(template.render({}, request))


def add_member(request):
    if request.method == "POST":
        form = MemberForm(request.POST)
        if form.is_valid():
            member = form.save(commit=False)
            member.joined_date = date.today()
            member.save()
            return redirect(
                "members"
            )  # Redireciona para a lista de membros após adicionar
    else:
        form = MemberForm()
    return render(request, "members/add_member.html", {"form": form})


def update_member(request, id):
    member = get_object_or_404(Member, pk=id)

    if request.method == "POST":
        form = MemberForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return redirect("details", id=member.id)
    else:
        form = MemberForm(instance=member)

    return render(request, "members/update_member.html", {"form": form, "member": member})


def delete_member(request, id):
    member = get_object_or_404(Member, pk=id)
    if request.method == "POST":
        member.delete()
        return redirect("members")
    return render(request, "members/delete_member.html", {"member": member})
