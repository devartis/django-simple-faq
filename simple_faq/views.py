from django.views.generic import ListView
from simple_faq.models import Topic


class Topics(ListView):
    template_name = "topic_list.html"
    context_object_name = "topics"
    model = Topic