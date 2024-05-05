import play
import pygame

play.set_backdrop('light blue')
introduce1 = play.new_text(words = 'Создайте свою мелодию!', x = 0, y =200 )
introduce2 = play.new_text(words = 'Нажимайте на клавиши!', x= 0, y=150)

key_play_melody = play.new_box(color='light green', border_color='black', border_width=1, x=-100, y=-170, width=160, height=50)
kpm = play.new_text(words='Проиграть мелодию', x=-100, y=-170, font_size=20)
key_clear_melody = play.new_box(color='light yellow', border_color='black', border_width=1, x=100, y=-170, width = 160, height=50)
kcm = play.new_text(words='Очистить мелодию', x=100, y=-170, font_size=20)

keys = []
sounds = []
for i in range(8):
    key_x = -180+i*50
    key = play.new_box(color='white', border_color = 'black', border_width=3, x=key_x, y=0, width = 40, height = 100)
    sound = pygame.mixer.Sound(str(i+1)+'.ogg')
    keys.append(key)
    sounds.append(sound)

melody = []

sound_clear_melody = pygame.mixer.Sound('clear_melody.wav')

@play.when_program_starts
def start():
    pygame.mixer_music.load('hello.mp3')
    pygame.mixer_music.play()

@key_clear_melody.when_clicked
def clear():
    melody.clear()
    sound_clear_melody.play()

@key_play_melody.when_clicked
async def play_m():
    for i in range(len(melody)):
        await play.timer(seconds=0.5)
        sounds[melody[i]].play()

@play.repeat_forever
async def play_piano():
    for i in range(len(keys)):
        if keys[i].is_clicked:
            keys[i].color = 'light grey'
            sounds[i].play()
            await play.timer(seconds=0.3)
            keys[i].color = 'white'
            melody.append(i)

play.start_program()