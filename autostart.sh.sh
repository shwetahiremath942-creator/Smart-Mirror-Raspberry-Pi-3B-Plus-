#!/bin/bash

# Disable screen blanking and power saving
xset s off
xset -dpms
xset s noblank

# Start MagicMirror Framework in production mode
cd ~/MagicMirror
npm start &

# Start Facial Recognition Background Process
cd ~/SmartMirror_AI
python3 face_recognition_module.py &