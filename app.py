from flask import Flask, request, redirect, url_for
from jinja2 import Template, Environment, FileSystemLoader
import yaml

file_loader = FileSystemLoader('templates')
env = Environment(loader = file_loader)

app = Flask(__name__)
with open('data.yml') as yaml_file:
    my_yaml = yaml.load(yaml_file)
    print(my_yaml)

def reves(txt: str) -> str:
    cadena = txt[::-1]
    return cadena

def largo(txt: str) -> int:
    lar = len(txt)
    return lar

def vowels(txt: str) -> int:
    cont = 0
    for car in txt:
        if car in 'aeiouAEIOU':
            cont = cont + 1
    return cont

def consonants(txt: str) -> int:
    cont = 0
    for car in txt:
        if car in 'aeiouAEIOU':
            cont = cont
        else:
            if car in ' ':
                cont = cont
            else:
                cont = cont + 1
    return cont

def mayus(txt: str) -> str:
    return txt.upper()

def minus(txt: str) -> str:
    return txt.lower()    

def interc(txt: str) -> str:
    new = ""
    p = ''
    for c in txt:
        if p != minus(p):
            p = minus(c)
            new += p
        else:
            p = mayus(c)
            new += p
    return new

def cambio(txt: str) -> str:
    resul = ""
    for a in txt:
        if a in 'aA':
            resul += '@'
        elif a in'eE':
            resul += '3'
        elif a in 'iI':
            resul += '!'
        elif a in 'oO':
            resul += '0'
        elif a in 'uU':
            resul += ')' 
        else:
            resul += a
    return resul

def solucion(txt: str):
    sol = {}
    if txt == ' ':
        return sol
    sol['Original'] = txt
    sol['Inverso'] = reves(txt)
    sol['Largo'] = largo(txt)
    sol['Vocales'] = vowels(txt)
    sol['Consonantes'] = consonants(txt)
    sol['Upper'] = mayus(txt)
    sol['Lower'] = minus(txt)
    sol['UpDown'] = interc(txt)
    sol['Naive'] = cambio(txt)
    return sol

@app.route('/', methods=['GET', 'POST'])
def index():
    entrada = request.form.get("string", "")
    image_file = url_for('static', filename = my_yaml['fotografia'])
    template = env.get_template('base.html')

    sol = solucion(entrada)
    return template.render(image_file=image_file, sol=sol)

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug = True)