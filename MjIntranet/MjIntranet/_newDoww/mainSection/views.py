from django.shortcuts import render
from .models import Member


def render_doww(request):
    qs = Member.objects.all()
    q = request.GET.get('q', '')
    if q:
        qs = qs.filter(title__icontains = q)
    return render(request, 'mainSection/main.html', {
    'dbList' : qs,
})



