import random
from django.template import Context, loader
from contactPage.models import Question
from django.http import HttpResponse
import encrypt

def contact(request):
    question = Question.objects.all().order_by('?')[0]
    t = loader.get_template('contactPage/index.html')
    c = Context({
        'question': question, 'encryptedAnswer': encrypt.xor(True, question.answer, question.address),
    })
    return HttpResponse(t.render(c))
