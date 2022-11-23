from django.shortcuts import redirect


def login_required(func):
    def wrap( request, *args, **kwrgs):
        if not (request.session.get("userid")):
            return redirect("log")
        else:
            return func(request, *args, **kwrgs)
    return wrap