'''
Crie um código em Python que teste se o site PUDIM está acessível pelo computador usado.
'''
import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
    print(site)
except urllib.error.URLEror:
    print('O site está inacessível')
else:
    print('O site está acessível')
    print(site.read()) #Este comando exibe o código do site acessado