from django.shortcuts import render
from .models import Book

def index(request):
    records = Book.objects.all()
    return render(request, "index.html", {"records": records})