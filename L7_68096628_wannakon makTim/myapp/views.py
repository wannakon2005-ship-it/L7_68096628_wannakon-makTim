from django.shortcuts import render
from django.http import HttpResponse

def contact(request):
    return HttpResponse("""
        <h1>ติดต่อ</h1>
        รหัสนักศึกษา: 68096628 <br>
        ชื่อ: warnnkon <br>
    """)

def form(request):
    return render(request, 'form.html')