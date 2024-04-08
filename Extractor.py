from scipy.io import wavfile

class Extractor:
    def __init__(self, audio_file, end_string = "^^^"):
        self.audio_file = audio_file
        self._end_string = end_string

    @staticmethod
    def bits_to_string(bit_list):
        string = ""
        for i in range(0, len(bit_list), 8):
            # Extract 8 bits at a time and convert them to a number
            bits = bit_list[i: i + 8]
            bit_string = "".join(map(str, bits))
            
            # Remove any non-binary characters
            bit_string = "".join(c for c in bit_string if c in "01")
            
            # Check if the filtered string is empty
            if not bit_string:
                break
            
            # Convert the number value to a character and append to the string
            num_value = int(bit_string, 2)
            character = chr(num_value)
            string += character
        return string

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

        raw_message = self.bits_to_string(extracted)
        # Only remove the message before the "end" string
        message = raw_message.split(self._end_string)[0]
        print(message)

        return message
