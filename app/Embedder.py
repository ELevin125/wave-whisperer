import wave
from app.Utility import string_to_bits

class Embedder:
    def __init__(self, audio_file, end_string = "^^^"):
        self.audio_file = audio_file
        self.audio = wave.open(self.audio_file, mode="rb")

        self._end_string = end_string

    def embed_message(self, message, path):
        frame_bytes = bytearray(list(self.audio.readframes(self.audio.getnframes())))

        # Append the "end" string to know when to stop the message when extracting it again
        bits = string_to_bits(message + self._end_string)

        # Modifies the 2 least significant bit (LSB) of the corresponding byte in frame_bytes.
        i = 0
        while i < len(bits) - 1:
            frame_bytes[i] = (frame_bytes[i] & 0xFC) | ((bits[i] & 0x02) >> 1) | (bits[i] & 0x01)
            i += 1

        modified_frame = bytes(frame_bytes)

        self._write_to_file(modified_frame, path)

    def _write_to_file(self, modified_frame, path):
        with wave.open(path, "wb") as fd:
            fd.setparams(self.audio.getparams())
            fd.writeframes(modified_frame)

