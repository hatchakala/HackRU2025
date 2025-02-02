import time
import audioop
import pyaudio
import numpy as np
import math

# constants
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2  # recording in stereo --> 2 channels --> left & right
RATE = 44100
RECORD_SECONDS = 10  # Record for 10 seconds
WAIT_SECONDS = 20  # Wait for 20 seconds after recording
FRAMES_PER_10_SEC = (RATE * RECORD_SECONDS) // CHUNK

# rms list for 1 min
rms_list = []
rms_average = 0  # AVERAGE OF 1 MINUTE --> NEEDS TO BE SENT TO MONGODB

# initialize pyaudio
p = pyaudio.PyAudio()
stream = p.open(
    format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK
)

while True:
    print("Recording for 10 seconds...")
    frames = []

    # record 10 seconds of audio
    for _ in range(FRAMES_PER_10_SEC):
        data = stream.read(CHUNK, exception_on_overflow=False)
        frames.append(data)

    # process 10-second chunk
    full_data = b"".join(frames)
    samples = np.frombuffer(data, dtype=np.int16)  # raw data to numpy array
    rms_volume = audioop.rms(full_data, 2)  # root mean square

    print(
        "Average volume in last 10 seconds:", rms_volume
    )  # audioop.rms(fragment, width) --> width is number of channels
    rms_list.append(rms_volume)

    if len(rms_list) == 2:
        print(rms_list)
        rms_average = math.ceil(
            sum(rms_list) / len(rms_list)
        )  # THIS is the data point that needs to be sent to MongoDB
        print(" (1-MINUTE) Average volume: ", rms_average)
        rms_list.clear()

    # wait 20 seconds b4 recording again
    print("Waiting for 20 seconds before restarting...")
    time.sleep(WAIT_SECONDS)
