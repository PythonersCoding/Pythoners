# task 7
__Author = "Pythoners"
import pyaudio
import wave
import os
import shutil

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 5000
CHUNK = 1024
RECORD_SECONDS = 10
WAVE_OUTPUT_FILENAME = "file.wav"
path = raw_input("enter the path u want to move your file to : ")
list = []
def record():
    audio = pyaudio.PyAudio()
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True, frames_per_buffer=CHUNK)
    print("recording...")
    frames = []
    for i in range(0, (int(RATE / CHUNK * RECORD_SECONDS))):
        data = stream.read(CHUNK)
        frames.append(data)
    print("finished recording")

    stream.stop_stream()
    stream.close()
    audio.terminate()

    waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()

    for root, dirs, files in os.walk("/root/"):
        for name in files:
            if name == WAVE_OUTPUT_FILENAME:
                name = str(name)
                name = os.path.join(root, name)
                list.append(name)
    shutil.copy(list[0], path)


record()