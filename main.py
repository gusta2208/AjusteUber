from flask import Flask, render_template, request
import conexao

import conexaoCliente
import operacoes
import this


this.cpf = 0
this.nome = ""
this.telefone = ""
this.endereco = ""
this.data = ""
this.dados = ""
this.mensagem = ""
this.dado = ""
this.ndado = ""
this.campo = ""


cliente = Flask(__name__) #Representando uma variável do tipo flask

@cliente.route('/', methods=['GET','POST'])
def menu():
    return render_template('menu.html', titulo='Página Principal', resultado=this.dados)

@cliente.route('/indexBoot.html', methods=['GET','POST'])
def cadastrar():
    if request.method == 'POST':
        this.cpf     = request.form['tNovoCpf']
        this.nome    = request.form['tNovoNome']
        this.telefone = request.form['tNovoTelefone']
        this.endereco = request.form['tNovoEndereco']
        this.dataNascimento     = request.form['tNovaDataNascimento']
        this.senha = request.form['tNovoSenha']
        this.dados    = conexaoCliente.inserir(this.cpf, this.nome, this.telefone, this.endereco, this.dataNascimento, this.senha)
    return render_template('indexBoot.html', titulo='Página Principal', resultado=this.dados)

@cliente.route('/motoristaCadastro.html', methods=['GET','POST'])
def cadastroMotorista():
    if request.method == 'POST':
        this.cpf      = request.form['tNovoCpf']
        this.nome     = request.form['tNovoNome']
        this.telefone = request.form['tNovoTelefone']
        this.endereco = request.form['tNovoEndereco']
        this.modelo = request.form['tNovoModelo']
        this.placa = request.form['tNovaPlaca']
        this.dataNascimento     = request.form['tNovaDataNascimento']
        this.senha = request.form['tNovoSenha']
        this.dados = operacoes.cadastrarMotorista(this.cpf, this.nome, this.telefone, this.endereco, this.modelo, this.placa, this.dataNascimento, this.senha)
    return render_template('motoristaCadastro.html', titulo='Cadastro Motorista', resultado=this.dados)



@cliente.route('/atualizar.html', methods=['GET','POST'])
def atualizarDados():
    if request.method == 'POST':
        this.cpf = request.form['tCpf']
        this.campo  = request.form['tCampo']
        this.nDado  = request.form['tNovoDado']
        this.dado = operacoes.atualizar(this.cpf, this.campo, this.nDado)
    return render_template('atualizar.html', titulo='Atualizar', resultado=this.dado)

@cliente.route('/atualizarCliente.html', methods=['GET','POST'])
def atualizarDadosCliente():
    if request.method == 'POST':
        this.cpf = request.form['tCpf']
        this.campo  = request.form['tCampo']
        this.nDado  = request.form['tNovoDado']
        this.dado = conexaoCliente.atualizar(this.cpf, this.campo, this.nDado)
    return render_template('atualizarCliente.html', titulo='Atualizar', resultado=this.dado)

@cliente.route('/consultarCodigo', methods=['GET','POST'])
def consultarIndividual():
    if request.method == 'POST':
        this.cpf = request.form['tCpf']
        this.mensagem = operacoes.consultar(this.cpf)
    else:
        this.mensagem = ""
    return render_template('consultarCodigo.html', titulo='Consultar por cpf', dados=this.mensagem)

@cliente.route('/consultarCliente', methods=['GET','POST'])
def consultarCliente():
    if request.method == 'POST':
        this.cpf = request.form['tCpf']
        this.mensagem = operacoes.consultar(this.cpf)
    else:
        this.mensagem = ""
    return render_template('consultarCliente.html', titulo='Consultar por cpf', dados=this.mensagem)

@cliente.route('/excluir.html', methods=['GET', 'POST'])
def excluirDados():
    if request.method == 'POST':
        this.cpf = request.form['tCpf']
        this.dado = operacoes.deletar(this.cpf)
    return render_template('excluir.html', titulo='Excluir', resultado=this.dado)


@cliente.route('/excluirCliente.html', methods=['GET', 'POST'])
def excluirDadosCliente():
    if request.method == 'POST':
        this.cpf = request.form['tCpf']
        this.dado = conexaoCliente.deletar(this.cpf)
    return render_template('excluirCliente.html', titulo='Excluir', resultado=this.dado)


if __name__ == '__main__':
    cliente.run(debug=True, port=5000)
