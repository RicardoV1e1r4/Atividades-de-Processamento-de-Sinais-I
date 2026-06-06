# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 17:47:08 2026

@author: Ricardo Alexandre
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider

# Valores iniciais do Sliders
# -Vetor tempo
fs = 1
Ts = 1/fs
t_final = 60
t = np.arange(0, t_final, Ts)

omega = 0.1


# Taxa de amostragem
def geracao_sinal(w, const=False):
    if const==True:
        # Sinal x[n]
        y_n = np.cos(t)
    else:
        # Sinal variável h[h]
        y_n = np.sin(w*t)
    
    return y_n

# Criação dos gráficos
figure, (eix1, eix2) = plt.subplots(2, 1, figsize=(8,7))
# Espaço extra para os botões deslizantes
plt.subplots_adjust(left=0.12, bottom=0.15, hspace=0.5)

# configuração do gráfico do sinal x[n] original
eix1.stem(t, geracao_sinal(omega, True))
eix1.set_xlabel('Time [s]', size=10)
eix1.set_ylabel('Amplitude', size=10)
eix1.set_title('Sinal x[n]')
eix1.grid(True)

# Configuração do gráfico do 
# eix2.stem(t, h_n)
stem2 = eix2.stem(t, geracao_sinal(omega, False),
                  linefmt='C0-',
                  markerfmt='C0o',
                  basefmt='k-')


eix2.set_xlabel('Time [s]', size=10)
eix2.set_ylabel('Amplitude', size=10)
eix2.set_title('Sinal variável')
eix2.grid(True)

###_____BOTÕES DESLIZANTES_____###
# Deslizante 1 - raio da esfera A
# fsample = plt.axes([0.2, 0.25, 0.65, 0.03])
# slider_sample = Slider(fsample, 'Amostragem', 0.01, 5, valinit=fs)

# #Deslizante 2 - Frequência angular
freq_ang = figure.add_axes([0.2, 0.25, 0.65, 0.03])

slider_omega = Slider(
    ax=freq_ang,
    label='Frequêncai angular',
    valmin=0.1,
    valmax=30,
    valinit=omega,)

###___Função que vai atualizar o gráfico___###
def atualizar(val):
    global stem2
    omega = slider_omega.val
    
    # Remover o gráfico anterior
    stem2.makerline.remove()
    
    try:
        stem2.stemlines.remove()
    except:
        for linha in stem2.stemlines:
            linha.remove()
            
    stem2.baseline.remove()
    
    # Cria o novo gráfico stem
    stem2 = eix2.stem(t, geracao_sinal(omega, False))
    
    # raioa = slider_raioa.val
    # eix1.set_ydata(PreencheDensidade(raioa, raiob))
    figure.canvas.draw_idle()


# Conecta os slides à função
# slider_raioa.on_changed(atualizar)
slider_omega.on_changed(atualizar)

plt.show()
