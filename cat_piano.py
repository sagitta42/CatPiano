# the package that does the playing
import simpleaudio as sa
# the package that does the key input reading
import pygame as pg
# only to print out the 'Nooooo' :)
import random

# correspondence of the keys to the audio files
SOUNDS = {pg.K_m: 'mozart.wav', pg.K_n: 'mewmew.wav', pg.K_b:'meeeew.wav',
          pg.K_a: 'kurz.wav', pg.K_s:'kurz1.wav', pg.K_d: 'meeewKurz.wav',
          pg.K_f:'ewew.wav', pg.K_g:'yeah.wav',
          pg.K_p:'whaaat.wav', pg.K_o: 'toscanein.wav', pg.K_i:'moreno.wav',
          pg.K_w: 'woof.wav', pg.K_h: 'hahaha.wav'}

# how is there no built in method for the key to tell its string name???
KEYS = ['m', 'n', 'b', 'a', 's', 'd', 'f', 'g', 'p', 'o', 'i', 'w', 'h']

soundfolder = 'sounds/'
# random "no" messages
NO = ['no', 'NOOOO', 'No', 'NoOoooOOO', 'MEWMEW', 'mew', 'miuuu']


######################################3


# main function
def piano():
    '''
    '''

    print('Available keys:')
    print(', '.join(KEYS))
    print('To quit press q')

    # this creates a window (necessary)
    # that will respond to the keys and do everything
    pg.init()

    # image not to have a boring black window
    img = pg.image.load('nononocatSmall.jpg')
    white = (255, 64, 64)
    screen = pg.display.set_mode((200, 200))
    screen.fill((white))

    # technical trick for later
    # playing silence first to create this "pl" object
    w = sa.WaveObject.from_wave_file(soundfolder + 'silence.wav')
    pl = w.play()

    running = True

    # it keeps running with some sort of 25 frames per second rate or sth
    while running:
        # put the image to the screen
        screen.blit(img,(0,0))
        pg.display.flip()

        # check if anything is happening all the time
        for event in pg.event.get():
            # if key is pressed
            if event.type == pg.KEYDOWN:
                # if a key corresponds to a sound
                if event.key in SOUNDS:
                    # print random message
                    print(random.choice(NO))
                    # stop the previous sound
                    pl.stop()
                    # play the sound
                    pl = note(soundfolder + SOUNDS[event.key])

                elif event.key == pg.K_q:
                    # if the key does not correspond to a sound
                    # do nothing unless it's "Q" which is our quit button
                    print('Quitting...')
                    running = False

    pg.quit()

# helper function
def note(name):
    w = sa.WaveObject.from_wave_file(name)
    pl = w.play()
    # will make the code wait rathe than execute the lines below
    #pl.wait_done()
    return pl


if __name__ == '__main__':
    piano()
