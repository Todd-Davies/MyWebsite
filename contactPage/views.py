import random
from django.template import Context, loader
from contactPage.models import Question
from django.http import HttpResponse

def contact(request):
    question = Question.objects.all().order_by('?')[0]
    t = loader.get_template('contactPage/index.html')
    c = Context({
        'question': question,
    })
    return HttpResponse(t.render(c))
