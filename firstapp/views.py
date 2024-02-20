from django.shortcuts import render
from django.http import HttpResponse

tax_rate = 0.15

def intro(request):
    return render(request, "taxCalc/intro.html")

def calc(request, num):
    total = num * (tax_rate + 1)
    return HttpResponse(f"For an amount of {num}, tax is {(tax_rate * 100)}%, total with tax is {total}.")

def show_tax(request):
    return render(request, "taxCalc/taxrate.html", {"rate": tax_rate * 100})