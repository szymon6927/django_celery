from django.http import JsonResponse
from django.views import View

from django_celery.tasks import debug_task


class MyView(View):
    def get(self, request):
        debug_task.delay()
        return JsonResponse({'status': "OK!"})
