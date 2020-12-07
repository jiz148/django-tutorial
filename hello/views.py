# from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

# Create your views here.


class HelloView(View):

    def get(self, request):
        view_count = request.session.get('view_count', 0) + 1
        if view_count > 5:
            view_count = 1
        request.session['view_count'] = view_count
        response = HttpResponse('view count=' + str(view_count))
        response.set_cookie('dj4e_cookie', 'e99ce0cd', max_age=1000)
        return response
