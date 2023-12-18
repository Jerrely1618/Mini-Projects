from pytube import YouTube

def example1():
    vid = YouTube("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    vid_mod = vid.streams.filter(file_extension="mp4").get_by_resolution("720p")
    vid_mod.download('../Short')

def example2():
    vid = YouTube("https://www.youtube.com/watch?v=U1mqDs20kVY")
    vid_mod = vid.streams.filter(file_extension="mp4").get_audio_only()
    vid_mod.download('../Short')
    
    
if __name__ == "__main__":
    example1()
    example2()