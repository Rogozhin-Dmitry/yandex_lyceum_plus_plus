from django.shortcuts import render
from django.views.generic import TemplateView


class About(TemplateView):
    TEMPLATE = "about/description.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.TEMPLATE)
