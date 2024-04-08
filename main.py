from scipy.io import wavfile # for working with the .wav files
import wave

def stringToBits(string):
    bitList = []
    for character in string:
        asciiValue = ord(character)
        binaryVal = bin(asciiValue).lstrip("0b").rjust(8, "0")
        bitList.append(binaryVal)

    bits = map(int, "".join(bitList))
    return list(bits)

song = wave.open("./assets/audioSample.wav", mode="rb")
frameBytes = bytearray(list(song.readframes(song.getnframes())))

message = "Father Christmas does not exist"
# Append dummy data to fill out rest of the bytes
filler = ""
for i in range(int((len(frameBytes) - (len(message) * 8 *8 )) / 8)):
    filler += "#"
message += filler

# Convert text to bit array
bits = stringToBits(message)

# Replace LSB of each byte of the audio data by one bit from the text bit array
i = 0
while i < len(bits) - 1:
    frameBytes[i] = (frameBytes[i] & 0xFC) | ((bits[i] & 0x02) >> 1) | (bits[i] & 0x01)
    i += 1

modifiedFrame = bytes(frameBytes)

# Write bytes to a new wave audio file
with wave.open("embedded_audio.wav", "wb") as fd:
    fd.setparams(song.getparams())
    fd.writeframes(modifiedFrame)

def bitsToString(bitList):
    string = ""
    for i in range(0, len(bitList), 8):
        # Extract 8 bits at a time and convert them to a number
        bits = bitList[i: i + 8]
        bitString = "".join(map(str, bits))
        
        # remove any non-binary characters
        bitString = "".join(c for c in bitString if c in "01")
        
        # Check if the filtered string is empty
        if not bitString:
            break
        
        # Convert the number value to a character and append to the string
        numValue = int(bitString, 2)
        character = chr(numValue)
        string += character
    return string

audioRate, audioData = wavfile.read("./embedded_audio.wav")
frameBytes = audioData.tobytes()

extracted = []
for i in range(0, len(frameBytes) - 1, 2):
    byte1 = frameBytes[i]
    byte2 = frameBytes[i + 1]

    # use 3 since in binary 0011, and we need two bits
    bit1 = byte1 & 0x03 
    bit2 = byte2 & 0x03

    extracted.append(bit1)
    extracted.append(bit2)

rawMessage = bitsToString(extracted)
# remove the dummy fillter characters
message = rawMessage.split("###")[0]

print("Secret Message:", "\"", message, "\"")