# Tocando um MP3

import pygame as py

py.mixer.init()


py.mixer.music.load("/home/leonardo/Documentos/projetos/Curso-Python/Desafios Mundo 01/Desafio-21/music-game.mp3")

py.mixer.music.set_volume(0.7)

py.mixer.music.play()

input('Precione enter para parar a musica...')
py.mixer.music.stop()
