from django.contrib.auth.middleware import get_user
from django.http import HttpResponse, JsonResponse
from rest_framework.request import Request
from rest_framework.views import APIView

_STEPS = [
    [
        {
            "name": "firstName",
            "label": "First Name",
            "type": "text",
            "required": True,
        },
        {
            "name": "lastName",
            "label": "Last Name",
            "type": "text",
        },
        {
            "name": "country",
            "label": "Country",
            "type": "text",
        },
        {
            "name": "bio",
            "label": "Bio",
            "type": "multiline-text",
        },
    ],
    [
        {
            "name": "receiveNotifications",
            "label": "Would you like to receive email notifications for new messages when logged out?",
            "type": "yes-no",
            "required": True,
        },
        {
            "name": "receiveUpdates",
            "label": "Would you like to receive product updates via email?",
            "type": "yes-no",
            "required": True,
        },
    ],
]


class Onboarding(APIView):
    def get(self, request: Request):
        """Get onboarding data"""
        try:
            user = get_user(request)

            if user.is_anonymous:
                return HttpResponse(status=401)

            return JsonResponse({"steps": _STEPS}, safe=False)
        except Exception as e:
            return HttpResponse(status=500)
