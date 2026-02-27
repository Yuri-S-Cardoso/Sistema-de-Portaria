from django.shortcuts import redirect

def login_required_custom(view_func):
    def wrapper(request, *args, **kwargs):
        if "porteiro_id" not in request.session:
            return redirect("login")  # Redireciona para a página de login se não estiver autenticado
        return view_func(request, *args, **kwargs)
    return wrapper
