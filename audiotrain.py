import speech_recognition as sr
import torchaudio as ta
import torch
import os
import pandas as pd

# Load the audio file
waveform, sample_rate = ta.load("Recordings/SrRecording(1).mp3")

# Print metadata
print(f"Sample Rate: {sample_rate}")
print(f"Waveform: {waveform.shape}")