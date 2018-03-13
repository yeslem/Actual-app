from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


# Create your views here.
# def login_view(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(data=request.POST)
#         if form.is_valid():
#             # log the user in
#             user = form.get_user()
#             login(request, user)
#             return redirect('/calculator/')
#     else:
#         form = AuthenticationForm()
#     return render(request, 'registration/login.html', { 'form': form })


@login_required(login_url="/login/")
def calculator(request):
    return render(request, 'webapp/calculator.html')
