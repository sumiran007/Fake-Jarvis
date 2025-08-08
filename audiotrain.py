import speech_recognition as sr
import torchaudio as ta
import torch
import os
import pandas as pd
import scipy as sp
import librosa as lb

for j in range(1, 2):
    names = ['Sr', 'Su']
    for i in range(1, int((len(os.listdir("Recordings")) + 1)/2)):
        file_path = f"Recordings/{names[j]}Recording ({i}).mp3"
        if os.path.exists(file_path):
            print(f"Processing {file_path}...")
            # Load the audio file
            waveform, sample_rate = ta.load(file_path)
            print(f"Waveform shape: {waveform.shape}, Sample rate: {sample_rate}")
# Load the audio file - capture both waveform and sample_rate
    #file_path = "Recordings\SrRecording (1).mp3"
        #waveform, sample_rate = lb.load(file_path, sr=22050, mono=True)

# Print metadata
        print(f"Sample Rate: {sample_rate}")
        print(f"Waveform: {waveform.shape}")
        print(sp.fft.fft(waveform))