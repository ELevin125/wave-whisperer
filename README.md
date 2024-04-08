# Wave Whisperer

Wave Whisperer is a Python application that allows you to embed a secret message into a WAV audio file or extract a previously embedded message from a WAV file. 
This project utilizes the LSB (Least Significant Bit) technique to hide data within the audio file. However, in this implementation, the 2 least significant bits are utilised.

## Features

- **Embed Message:** Embed a secret message into a WAV audio file.
- **Extract Message:** Extract a previously embedded message from a WAV audio file.

## Required packages 
- SciPy library

## Usage

1. Run the application by executing `main.py`.
2. Select whether you want to embed a message or extract a message from a WAV file.
3. Specify the file you want to embed to, or extract from.
4. If embedding, provide the message you want to hide and select the WAV file.
5. Click on the "Process" button to initiate the embedding or extraction process.

## Code Structure

- `WaveWhisperer.py`: Main application script containing the graphical user interface.
- `Embedder.py`: Contains the Embedder class responsible for converting and embedding messages into WAV files.
- `Extractor.py`: Contains the Extractor class responsible for attempting to extract messages from WAV files.
- `Utility.py`: Contains utility functions related to conversion between strings and binary.
