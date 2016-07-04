import requests
import json
import time

def sincronizarMensagens(mensagens, vizinhos):
	while 1:
		time.sleep(1/5)
		for p in vizinhos:
			try:
				r = requests.get('http://localhost:' + p + '/mensagens')
				merge(mensagens, r.json())
			except requests.exceptions.ConnectionError:
				time.sleep(1/5)
			except ValueError:
				print("Erro no valor retornado do vizinho: " + p)


def merge(mensagens, novas):
	existe = False
	for n in novas:
		existe = False
		for m in mensagens:
			if m[0] == n[0] and m[1] == n[1]:
				existe = True
				break
		if not existe:
			mensagens.append(n)