from pytube import YouTube as YT

URL = input("다운로드 할 YouTube 영상의 주소를 입력해 주세요:")
video = YT(URL)
audio = video.streams.get_audio_only()
audio.download('./download')
print("다운로드가 완료되었습니다 ^^")

