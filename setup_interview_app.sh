#!/bin/bash

# Create and activate a virtual environment
python3 -m venv interview_env
source interview_env/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install core libraries
pip install streamlit opencv-python-headless moviepy

# Install Vosk and its dependencies
pip install vosk sounddevice

# Install NLP libraries
pip install spacy scikit-learn nltk textstat
python -m spacy download en_core_web_sm

# Install audio processing libraries
pip install librosa soundfile

# Install computer vision libraries
pip install dlib mediapipe

# Install facial emotion recognition library
pip install fer

# Install reporting libraries
pip install reportlab jinja2

# Install data manipulation and visualization libraries
pip install pandas numpy matplotlib plotly

# Install additional utilities
pip install python-Levenshtein

# Create a requirements.txt file
pip freeze > requirements.txt

echo "Installation complete. Virtual environment 'interview_env' created and activated."
echo "To activate this environment in the future, run:"
echo "source interview_env/bin/activate"
echo ""
echo "Important: You need to download a Vosk model separately."
echo "Visit https://alphacephei.com/vosk/models and download an appropriate model."
echo "Place the model in your project directory and update your code to point to it."
