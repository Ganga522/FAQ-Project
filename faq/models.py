from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from deep_translator import GoogleTranslator  # Import the correct Translator
from django.core.cache import cache

class FAQ(models.Model):
    question = models.TextField()
    answer = CKEditor5Field()
    question_hi = models.TextField(blank=True, null=True)
    question_bn = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.question_hi:
            self.question_hi = GoogleTranslator(source='en', target='hi').translate(self.question)  # Using GoogleTranslator correctly
        if not self.question_bn:
            self.question_bn = GoogleTranslator(source='en', target='bn').translate(self.question)  # Using GoogleTranslator correctly
        cache.set(f'faq_{self.pk}', self)
        super().save(*args, **kwargs)

    def get_translation(self, lang='en'):
        return getattr(self, f'question_{lang}', self.question)
    
    def __str__(self):
        return self.question
