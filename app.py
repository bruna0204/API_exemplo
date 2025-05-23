from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    """
    mostra a mensagem inicial
    :return: 'hello world'
    """
    return 'Hello World!'


@app.route('/<name>') #aparece no nevegador /qualquer coisa
def hello(name):
    """
    mostra o nome
    :param name: nome do usuario
    :return: nome do usuario
    """
    return 'Hello' + name


@app.route('/soma/<number1>+<number2>')
def soma(number1, number2):
    """
    calcula a soma dos dois numeros
    :param number1: primeiro numero
    :param number2: segundo numero
    :return: soma dos dois numeros
    """
    try:
        number1 = int(number1)
        number2 = int(number2)
        return str(number1 + number2)
    except ValueError:
        return 'Só numeros inteiros'

@app.route('/subtracao/<number1>-<number2>')
def subtract(number1, number2):
    """
    subtrai dos dois numeros
    :param number1: primeiro numero
    :param number2: segundo numero
    :return: subtracão dos dois numeros
    """
    try:
        number1 = int(number1)
        number2 = int(number2)
        return str(number1 - number2)
    except ValueError:
        return 'Só numeros inteiros'

@app.route('/multiplicacao/<number1>*<number2>')
def multiply(number1, number2):
    """
    multiplica dos dois numeros
    :param number1: primeiro numero
    :param number2: segundo numero
    :return: multiplicacao dos dois numeros
    """
    try:
        number1 = int(number1)
        number2 = int(number2)
        return str(number1 * number2)
    except ValueError:
        return 'Somente numeros inteiros'

@app.route('/divisao/<number1>/<number2>')
def divisao(number1, number2):
    """
        divisao dos dois numeros
        :param number1: primeiro numero 
        :param number2: segundo numero
        :return: divide  dois numeros
        """""
    try:
        number1 = int(number1)
        number2 = int(number2)
        if number1 / number2 == 0:
            return str (number1 / number2)
         else:
            return 'O numero precisa ser maior que zero'

    except ValueError:
            print("Digite apenas numeros inteiros")


@app.route('/par_impar/<number1>')
def par_impar(number1):
    try:
        number1 = int(number1)
        verificar = number1 % 2
        if verificar == 0:
            return "par"
        else:
            return "impar"

    except ValueError:
        return "Digite apenas numeros inteiros"










if __name__ == '__main__':
    app.run(debug=True) #presisa desabilitar ele quando subir pra internet