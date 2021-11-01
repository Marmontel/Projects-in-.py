# Objective: Create local music player with pygame

import pygame
pygame.init()
# Change to the path of your mp3 file
pygame.mixer.music.load('Path-your-music-file.mp3')
pygame.mixer.music.play()
pygame.event.wait()
