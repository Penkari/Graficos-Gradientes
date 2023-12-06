from customtkinter import CTk, CTkFrame, CTkLabel, CTkEntry, CTkButton, CTkOptionMenu
from gradiente_funcoes import raiz, ip, botao, sair
from os.path import dirname, join
from sys import argv

# Iniciando interface customtkinter
janela = CTk()
janela.geometry('1020x600')
janela.title('Gradientes')
janela.resizable(True, False)
janela.iconbitmap(default = join(dirname(argv[0]), 'icon.ico'))

# Criação de Frames, Labels, Entrada, Botões e Menu de Opções
frame_esquerdo = CTkFrame(janela, width = 160, height = 600, border_width = 0)
frame_esquerdo.pack(side = 'left', expand = True, fill = 'both')

observacao_1 = CTkLabel(frame_esquerdo, text = '''Observações:\nUsar . para definir multiplicações\nUsar ^ para definir potências\nLembre-se sempre de fechar os parênteses ()''', justify = 'left')
observacao_1.pack(side = 'left', padx = 20)

frame_meio = CTkFrame(janela, width = 480, height = 600, border_width = 0)
frame_meio.pack(side = 'left', expand = True, fill = 'both')

espacamento = CTkLabel(frame_meio, text = '')
espacamento.pack(side = 'top', pady = 100)

frame_entrada = CTkFrame(frame_meio, width = 480)
frame_entrada.pack(side = 'top')

texto = CTkLabel(frame_entrada, text = 'F(x, y) =', font = ('merriweather', 20, 'italic'))
texto.pack(side = 'left')

# Função botao() encontrasse no pacote gradiente_funcoes.py
entrada_funcao = CTkEntry(frame_entrada, placeholder_text= 'Digite a função aqui', font = ('merriweather', 20, 'italic'), width = 300, height= 50)
entrada_funcao.pack(side = 'right')
entrada_funcao.bind('<Return>', lambda event: botao(texto_funcao, entrada_funcao, erro, escala))

# Função raiz() encontrasse no pacote gradiente_funcoes.py
botao_raiz = CTkButton(frame_meio, text = '√', command =lambda: raiz(entrada_funcao), width = 0)
botao_raiz.pack(side = 'left', anchor = 'n', padx = 8)

# Função ip() encontrasse no pacote gradiente_funcoes.py
botao_pi = CTkButton(frame_meio, text = 'π', command =lambda: ip(entrada_funcao), width = 0)
botao_pi.pack(side = 'left', anchor = 'n', padx = 10)

escala = CTkOptionMenu(frame_meio, values = ['5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15'], width = 50)
escala.pack(side = 'right', anchor = 'n')

texto_escala = CTkLabel(frame_meio, text = 'Escala:', width = 0, font = ('arial', 15))
texto_escala.pack(side = 'right', anchor = 'n', padx = 0, pady = 0)

texto_funcao = CTkLabel(frame_meio, text = '...', font = ('merriweather', 20, 'italic'))
texto_funcao.pack(side = 'top', pady = 30)

frame_direita = CTkFrame(janela, width = 160, height = 600, border_width = 0)
frame_direita.pack(side = 'left', expand = True, fill = 'both')

erro = CTkLabel(frame_direita, text = '...', text_color = 'red', font = ('arial', 15))
erro.pack(side = 'top', pady = 120)

observacao_2 = CTkLabel(frame_direita, text = '''Isto é apenas um protótipo.\nFunções do tipo F(x, y, z) ainda não disponíveis''', justify = 'left')
observacao_2.pack(side = 'top', padx = 20)

# Função botao() encontrasse no pacote gradiente_funcoes.py
botao_grafico = CTkButton(frame_meio, text = 'Gerar Gráfico', command =lambda: botao(texto_funcao, entrada_funcao, erro, escala), font = ('arial', 20), width = 125, height= 50)
botao_grafico.pack(side = 'top')

# Função sair() encontrasse no pacote gradiente_funcoes.py
janela.protocol('WM_DELETE_WINDOW', func =lambda: sair(janela))

# Manter a interface em loop
janela.mainloop()
