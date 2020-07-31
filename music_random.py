#!/usr/bin/env python
import math
import pyaudio
import random

PyAudio = pyaudio.PyAudio


def play_note(note):
	#See http://en.wikipedia.org/wiki/Bit_rate#Audio
	BITRATE = 16000 #number of frames per second/frameset.      

	FREQUENCY = note #Hz, waves per second, 261.63=C4-note.
	LENGTH = 0.3 #seconds to play sound

	if FREQUENCY > BITRATE:
	    BITRATE = FREQUENCY+100

	NUMBEROFFRAMES = int(BITRATE * LENGTH)
	RESTFRAMES = NUMBEROFFRAMES % BITRATE
	WAVEDATA = ''    

	for x in xrange(NUMBEROFFRAMES):
	 WAVEDATA = WAVEDATA+chr(int(math.sin(x/((BITRATE/FREQUENCY)/math.pi))*127+128))    

	for x in xrange(RESTFRAMES): 
	 WAVEDATA = WAVEDATA+chr(128)

	p = PyAudio()
	stream = p.open(format = p.get_format_from_width(1), 
	                channels = 1, 
	                rate = BITRATE, 
	                output = True)

	stream.write(WAVEDATA)
	stream.stop_stream()
	stream.close()
	p.terminate()


A4 = 440.00
B4 = 493.88
C5 = 523.25
D5 = 587.33
E5 = 659.25
F5 = 698.46
G5 = 783.99
A5 = 880.00
B5 = 987.77
C6 = 1046.50

def note(number):
	if number % 10 == 0:
		return A4
	if number % 10 == 1:
		return B4
	if number % 10 == 2:
		return C5
	if number % 10 == 3:
		return D5
	if number % 10 == 4:
		return E5
	if number % 10 == 5:
		return F5
	if number % 10 == 6:
		return G5
	if number % 10 == 7:
		return A5
	if number % 10 == 8:
		return B5
	if number % 10 == 9:
		return C6

for i in range(20):
	note_number = random.randint(1, 10)
	play_note(note(note_number))		
	print(note_number)