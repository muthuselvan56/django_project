from django.shortcuts import redirect

def request_redirect(request):
    return redirect('/todos')