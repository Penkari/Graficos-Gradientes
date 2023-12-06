from numpy import linspace, meshgrid, sin, cos, tan, arctan, e, pi, log, sqrt
from matplotlib.pyplot import figure, show
from re import findall
from sys import exit

# Função para adicionar o caractere '√' na entrada de dados
def raiz(entrada_funcao):
    entrada = entrada_funcao.get()
    entrada_funcao.delete(0, 'end')
    entrada_funcao.insert('end', entrada + '√(')


# Função para adicionar o caractere 'π' na entrada de dados
def ip(entrada_funcao):
    entrada = entrada_funcao.get()
    entrada_funcao.delete(0, 'end')
    entrada_funcao.insert('end', entrada + 'π')


# Função de entrada da função gradiente visando qualquer possibilidade
def funcao_gradiente(entrada, erro, x, y):
    entrada = f'{entrada.get()}'.replace('tan^1', 'arctan').replace('ln', 'log').replace('√', 'sqrt').replace('π', 'pi').replace('^', '**').replace('.', '*').replace('sen', 'sin').replace(',', '.').strip()
    funcoes_permitidas = ['sin', 'cos', 'tan', 'arctan', 'log', 'pi', 'e', 'sqrt', 'x', 'y', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    funcoes_encontradas = findall(r'\b\w+\b', entrada)

    try:
        for funcao in funcoes_encontradas:
            if funcao not in funcoes_permitidas:
                raise ValueError
            
            else:
                erro.configure(text = '...')
                return eval(entrada)

    except (SyntaxError, ValueError):
        return erro.configure(text = f'Valor Inserido Inválido:\n{entrada.get()}')


# Função de criação do gráfico 3d
def botao(texto, entrada, erro, escala):
    try:
        erro.configure(text = '...')

        x = linspace(int(f'{escala.get()}') * -1, int(f'{escala.get()}'), 100)
        y = linspace(int(f'{escala.get()}') * -1, int(f'{escala.get()}'), 100)

        X, Y = meshgrid(x, y)

        Z = funcao_gradiente(entrada, erro, X, Y)

        fig = figure(figsize = (13, 7))
        ax = fig.add_subplot(111, projection='3d')

        surf = ax.plot_surface(X, Y, Z, cmap='viridis')

        fig.colorbar(surf)
        
        texto.configure(text = f'F(x, y) = {entrada.get()}')

        ax.set_xlabel('Eixo X')
        ax.set_ylabel('Eixo Y')
        ax.set_zlabel('Eixo Z')

        show()

    except Exception as error:
        erro.configure(text = f'Ocorreu um erro na geração do gráfico:\n{error.__cause__}')


# Função para o encerramento do programa sem vestigios de eventos em aguardo
def sair(tK):
    for after_id in tK.tk.eval('after info').split():
        tK.after_cancel(after_id)
    tK.destroy()
    exit()

