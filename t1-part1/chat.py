from bottle import run, get, post, view, request, redirect, route

messages = [("Nobody", "Hello!")]

@route('/')
@route('/<nome>')
@view('index')
def index(nome='Nobody'):
	return {'messages': messages, 'nick': nome}


@post('/send')
def sendMessage():
	m = request.forms.get('message')
	n = request.forms.get('nick')
	messages.append([n, m])
	redirect('/' + n)


run(host='localhost', port=8080)
