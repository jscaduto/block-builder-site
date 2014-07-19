from django.db import models
from django.forms import ModelForm
from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse
from django.core.validators import RegexValidator

BLOCK_SET_CHOICES = (
    ('ED_ELETHA_BLOCKS', 'Ed and Eletha Blocks'),
    ('ROGER_MOLLY_BLOCKS', 'Roger and Molly Blocks'),
)

def validate_phrase_length(value):
    if len(value.replace(' ','')) > 16:
        raise ValidationError(u'Phrase cannot contain more than 16 characters.')

class Phrase(models.Model):
    block_set_name = models.CharField(max_length=100, choices=BLOCK_SET_CHOICES, blank=False)
    phrase_text = models.CharField(max_length=140, blank=False, validators=[validate_phrase_length, 
        RegexValidator(r'^[\sa-zA-Z4]*$',u"Phrase must ONLY contain letters and the number '4' to represent '4th'.",ValidationError)])
    request_date = models.DateTimeField(auto_now=True)
    possible = models.BooleanField(editable=False)
    solution = models.CommaSeparatedIntegerField(max_length=16, blank=True, null=True)
    difficulty = models.IntegerField(blank=True, null=True)
    def __unicode__(self):
        return self.phrase_text
    def get_absolute_url(self):
        return reverse('phrase-detail', kwargs={'pk': self.pk})