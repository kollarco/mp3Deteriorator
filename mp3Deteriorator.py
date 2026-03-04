import wave
import soundfile as sf
import config
import io
import lameenc

fileName = config.INPUT_FILE
output = config.OUTPUT_FILE


wavBuffer = io.BytesIO()

data, samplerate = sf.read(fileName);

# writes the wav file into the buffer in the correct 16bit format
sf.write(wavBuffer, data, samplerate, subtype='PCM_16', format='WAV')
wavBuffer.seek(0)

wavFile = wave.open(wavBuffer, 'rb')

#gets all the needed info from the wav file
channels = wavFile.getnchannels()
sampleWidth = wavFile.getsampwidth()
frameRate = wavFile.getframerate()
frames = wavFile.getnframes()

print("Channels: " + str(channels))
print("Sample Width: " + str(sampleWidth))
print("Frame Rate: " + str(frameRate))
print("Number of Frames: " + str(frames))

#initialises the encoder and sets configurations
encoder = lameenc.Encoder()
encoder.set_bit_rate(config.BIT_RATE)
encoder.set_in_sample_rate(frameRate)
encoder.set_channels(channels)
encoder.set_quality(config.QUALITY)

#creates an empty bytes object
all_mp3_data = b''

chunk_size = config.CHUNK_SIZE
frames_read = 0

while frames_read < frames:
    frames_to_read = min(chunk_size, frames - frames_read)

    chunk_bytes = wavFile.readframes(frames_to_read)

    mp3_chunk = encoder.encode(chunk_bytes)

    all_mp3_data += mp3_chunk

    frames_read += frames_to_read
    #print("Processed " +str(frames_read) + "/" + str(frames)+ "frames")

# Flush when finished encoding the entire stream
all_mp3_data += encoder.flush()

with open(output, "wb") as f:
    f.write(all_mp3_data)
