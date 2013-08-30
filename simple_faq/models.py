from django.db import models
from tinymce import models as tinymce_models
from django.utils.translation import ugettext_lazy as _

photos_path = "simple-faq/"


class Topic(models.Model):
    text = models.CharField(max_length=200)
    number = models.IntegerField()

    class Meta:
        verbose_name = _("Topic")
        verbose_name_plural = _("Topics")
        ordering = ['number']

    def __unicode__(self):
        return u'(%s) %s' % (self.number, self.text, )


class Question(models.Model):
    text = models.CharField(max_length=200)
    answer_text = tinymce_models.HTMLField()
    topic = models.ForeignKey(Topic, related_name="questions")
    header_picture = models.ImageField(upload_to=photos_path, blank=True)
    number = models.IntegerField()
    related_questions = models.ManyToManyField("self", related_name="related_questions", blank=True, null=True)

    class Meta:
        verbose_name = _("Question")
        verbose_name_plural = _("Questions")
        ordering = ['number']

    def __unicode__(self):
        return u'(%s) %s' % (self.number, self.text, )
