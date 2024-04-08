from scipy.io import wavfile
from app.Utility import bits_to_string

class Extractor:
    def __init__(self, audio_file, end_string = "^^^"):
        self.audio_file = audio_file
        self._end_string = end_string

    def extract_message(self):
        audio_rate, audio_data = wavfile.read(self.audio_file)
        frame_bytes = audio_data.tobytes()

        extracted = []
        for i in range(0, len(frame_bytes) - 1, 2):
            byte1 = frame_bytes[i]
            byte2 = frame_bytes[i + 1]

            # Use 3 since in binary 0011, and we need two bits
            bit1 = byte1 & 0x03 
            bit2 = byte2 & 0x03

            extracted.append(bit1)
            extracted.append(bit2)

        raw_message = bits_to_string(extracted)
        # Only return the message before the "end" string
        message = raw_message.split(self._end_string)[0]

        return message
