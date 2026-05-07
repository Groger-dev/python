#reprodutor de áudio .mp3 funcionaaaaaaaa!
import pygame

# Inicializa o mixer do pygame
pygame.mixer.init()

# Carrega e toca o arquivo MP3
pygame.mixer.music.load('oceano.mp3')
pygame.mixer.music.play()

# Mantém o script rodando enquanto a música toca
input("Pressione Enter para parar...")
pygame.mixer.music.stop()
