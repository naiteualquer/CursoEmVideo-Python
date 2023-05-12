#abra e reproduza o áudio de arquivo mp3

import pygame

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('ex21musicamp3.mp3')
pygame.mixer.music.play()
pygame.event.wait()
