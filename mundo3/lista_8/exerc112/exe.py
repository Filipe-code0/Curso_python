import urllib.request

try:
    site = urllib.request.urlopen('https://www.pudim.com.br/')
except urllib.error.URLError:
    print('Falha ao procurar url')
else:
    print('Sucesso ao procurar url')
