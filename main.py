from pytube import YouTube as YT

video = YT('https://www.youtube.com/watch?v=0JrlKcoD1Qw')
audio = video.streams.get_audio_only()
audio.download('./download')