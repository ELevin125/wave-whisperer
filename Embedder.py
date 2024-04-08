import wave

class Embedder:
    def __init__(self, audio_file):
        self.audio_file = audio_file
        self.audio = wave.open(self.audio_file, mode="rb")

    @staticmethod
    def string_to_bits(string):
        bit_list = []
        for character in string:
            ascii_value = ord(character)
            binary_val = bin(ascii_value).lstrip("0b").rjust(8, "0")
            bit_list.append(binary_val)

        bits = map(int, "".join(bit_list))
        return list(bits)

    def embed_message(self, message):
        frame_bytes = bytearray(list(self.audio.readframes(self.audio.getnframes())))

        # Append dummy data to fill out rest of the bytes
        filler = ""
        for i in range(int((len(frame_bytes) - (len(message) * 8 * 8)) / 8)):
            filler += "#"
        message += filler

        # Convert text to bit array
        bits = self.string_to_bits(message)

        # Modifies the 2 least significant bit (LSB) of the corresponding byte in frame_bytes.
        i = 0
        while i < len(bits) - 1:
            frame_bytes[i] = (frame_bytes[i] & 0xFC) | ((bits[i] & 0x02) >> 1) | (bits[i] & 0x01)
            i += 1

        modified_frame = bytes(frame_bytes)

        self._write_to_file(modified_frame)

    def _write_to_file(self, modified_frame):
        with wave.open("embedded_audio.wav", "wb") as fd:
            fd.setparams(self.audio.getparams())
            fd.writeframes(modified_frame)

