import pydub as pd
import time
import threading
execfile('pydub_help.py')

def viz_play(song, viz):
	t = time.time

	prev_t = 0.0
	i = 0
	
	thread = threading.Thread(target=play, args=(song,))
	thread.start()
	finish = t()+song.duration_seconds
	cur_t = t()

	while cur_t < finish:
		cur_t = t()

		if cur_t - prev_t >= 0.001:
			print viz[i]
			i += 1
			prev_t = cur_t




def main():
	
	path = ''
	while path != 'EXIT':
		path = str(raw_input('MP3 Path ("EXIT" to quit):')).strip()
		song = pd.AudioSegment.from_file(path, format='mp3')
		song_max = float(song.max)
		duration = len(song)

		#A list with the max amplitude of the song at every millisecond.
		viz = list()

		for i in xrange(1, duration):
			chunk = song[i-1:i]
			bar = '|' * int((chunk.max/song_max)*60)
			bar = bar+'\n'+bar
			viz.append(bar)

		viz_play(song, viz)


main()