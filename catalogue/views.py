from django.shortcuts import render,redirect

# Create your views here.
def profile_view(request):
    if request.user.is_authenticated:

        return render(request,"pages/profile.html")
    else:
       
        return redirect("login")