from Embedder import Embedder
from Extractor import Extractor

message_end_string = "^^^"

# Embed message into audio file
embedder = Embedder("./assets/audioSample.wav", message_end_string)
message_to_embed = """
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you"""
embedder.embed_message(message_to_embed)

# Extract message from embedded audio file
extractor = Extractor("embedded_audio.wav", message_end_string)
extracted_message = extractor.extract_message()

print("Extracted Message:", extracted_message)