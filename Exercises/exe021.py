#Make a code that open and reproduce a mp3 audio

import pygame

#Startinh gaming module
pygame.init()

#Loading the music
pygame.mixer.music.load('music_exe021.mp3')

#Starting it
pygame.mixer.music.play()

#Holding the program until the music finishes
#while pygame.mixer.music.get_busy():
#    continue

#Stops the music whenever you want
input('Type anything to stop the music: ')
pygame.mixer.music.stop()







