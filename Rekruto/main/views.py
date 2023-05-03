from django.http import HttpResponse
from django.template import loader

def hello(request):
    name = request.GET.get('name', None)
    message = request.GET.get('message', None)
    if name and message:
        response_text = f'Hello {name}! {message}'

    else:
        response_text = 'Rekruto! Давай дружить!'

    template = loader.get_template('hello.html')
    context = {'response_text': response_text}
    response_html = template.render(context)

    return HttpResponse(response_html)