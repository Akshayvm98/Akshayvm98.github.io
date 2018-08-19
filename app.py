import os
from bottle import route, run, jinja2_view , request

@route('/')
@jinja2_view('index.html')

def index():
	return {'name': 'Akshay'}


@route('/', method ="post")
@jinja2_view('index.html')

def form_handler():
	para = request.forms.get('para')
	old = request.forms.get('old')
	new = request.forms.get('new')
	new_para = para.replace(old,new)

	return {"para":new_para}

	run(host='0.0.0.0', port=int(os.environ.get("PORT",5000)))
