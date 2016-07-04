from bottle import run, get, post, view, request, redirect, route
import threading
import sys
from request import *

messages = [("Nobody", "Hello!")]
conhecidos = ['8080', '8081', '8082']

@route('/')
@route('/<nome>')
@view('index')
def index(nome='Nobody'):
	return {'messages': messages, 'nick': nome}


@get('/mensagens')
def retornaMensagens():
	global messages
	return json.dumps(messages)


@post('/send')
def sendMessage():
	m = request.forms.get('message')
	n = request.forms.get('nick')
	messages.append([n, m])
	redirect('/' + n)


if len(sys.argv) < 2:
	print('Informe a porta como parâmetro')
	exit()

threading.Thread(target = sincronizarMensagens, args=[messages, conhecidos]).start()

run(host='localhost', port=sys.argv[1])
