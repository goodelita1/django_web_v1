from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import NameForm



def get_name(request):
    if request.method == "POST":
        form = NameForm(request.POST)
        if form.is_valid():
            first = request.POST.get('first', '')
            second = request.POST.get('second', '')
            res = int(first) + int(second)
            context ={'res_triangle': res}
            return render(request, "main/about.html" , context)
    else:
        form = NameForm()
    return render(request, "main/about.html" , {"form": form})
# Create your views here.
def index(request):
    return render(request, 'main/index.html')

#def about(request):
#    return render(request, 'main/about.html')
