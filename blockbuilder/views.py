import json

from django.conf import settings
from django.core.urlresolvers import reverse
from django.forms.util import ErrorList
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView

from blockbuilder.models import Phrase
from block_builder import BlockSolver

block_solver = BlockSolver(settings.BLOCK_SETS)


class PhraseCreate(CreateView):
    model = Phrase
    fields = ['block_set_name', 'phrase_text']

    def form_valid(self, form):
        block_set_name = form.cleaned_data['block_set_name']
        phrase_text = form.cleaned_data['phrase_text']
        solution = block_solver(block_set_name, phrase_text)
        self.object = form.save(commit=False)
        if not solution:
            self.object.possible = False
            self.object.save()
            form._errors['phrase_text'] = ErrorList([
                u'Cannot build phrase "{0}" with blocks.'.format(phrase_text)])
            return super(PhraseCreate, self).form_invalid(form)
        self.object.solution = solution
        self.object.possible = True
        self.object.save()
        return HttpResponseRedirect(reverse('phrase-detail', args=(self.object.id,)))


class PhraseDetailView(DetailView):
    model = Phrase

    def get_context_data(self, **kwargs):
        context = super(PhraseDetailView, self).get_context_data(**kwargs)
        return context


def get_lastest_phrases(request):
    phrase = Phrase.objects.all()[5]
    return HttpResponse(json.dumps(phrase), mimetype='application/json')
