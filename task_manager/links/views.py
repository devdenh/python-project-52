from django.views.generic import TemplateView


class LinksView(TemplateView):
    template_name = 'links.html'
