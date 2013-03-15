from django.views.generic import TemplateView
from simple_faq.models import Topic


class Topics(TemplateView):
    template_name = "topics.html"
    context_object_name = "topics"
    model = Topic