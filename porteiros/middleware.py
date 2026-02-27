from django.shortcuts import redirect
from django.utils.timezone import now
import datetime

class SessionTimeoutMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path == "/":
            return self.get_response(request)

        last_activity = request.session.get("last_activity")

        if last_activity:
            last_activity = datetime.datetime.fromisoformat(last_activity)  
            elapsed_time = (now() - last_activity).total_seconds()
            if elapsed_time > 600: # 10 minutos de inatividade
                request.session.flush()
                return redirect("login")

        request.session["last_activity"] = now().isoformat()

        return self.get_response(request)
