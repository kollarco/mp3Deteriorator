# mp3Deteriorator
A small tool I want to develop to be able to push mp3 encoding to 
its max to be able to use the effects creatively in music production

My idea is to build it iteratively. So I'm just going to start with 
a very basic file load in and convert and build a GUI from there.
Of course it will not be as smooth as an actual VST and there are already
amazing PlugIns which achieve this effect, but I want this project to 
be one of the first steps I make in the direction of developing
audio tools.

## Current State
copy config_preset.py to config.py

fill in your file path for the WAV input file and mp3 output file

edit the compression options to your liking

The only thing I've done so far, is built an easier to use python file to compress wav files
into mp3 (using other peoples libraries) and being able to change the compression options. 


## Next Step
Next I could implement
a simple UI. 

My plan is also to mess with the bytes before/after the encoding process to see if i can find any technique
that sounds interesting. So maybe there could be some sort of jitter. 

I want to learn more about how Audio Streaming works. I have this idea to change the bitrate while encoding, which is 
what happens when your Internet connection suddenly gets worse while streaming something.

## Dependencies

- [lameenc](https://github.com/chrisstaite/lameenc) — MP3 encoding via LAME
- [soundfile](https://github.com/bastibe/python-soundfile) — Formatting of any WAV file into 16bit
