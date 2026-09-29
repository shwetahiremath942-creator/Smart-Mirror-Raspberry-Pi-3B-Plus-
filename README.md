# AI-Powered Smart Mirror using Raspberry Pi 3 B+

## Overview
An interactive **Smart Mirror** system built using a Raspberry Pi 3 B+ and a two-way mirror integrated with a monitor screen. The system displays real-time contextual information—such as time, date, local weather, upcoming calendar events, and news updates—while utilizing OpenCV-based facial recognition to personalize display layouts based on identified users.

---

## Hardware Components
* **Raspberry Pi 3 Model B+**
* **Two-Way Mirror / Acrylic Mirror**
* **Monitor Screen / Display Panel**
* **Pi Camera Module / USB Webcam**
* **Power Supply (5V, 2.5A)**
* **HDMI to VGA/HDMI Cable**

---

## Software & Frameworks
* **Operating System:** Raspberry Pi OS (32-bit / Debian)
* **Smart Mirror Platform:** MagicMirror² (Node.js framework)
* **Computer Vision:** OpenCV & `face_recognition` (dlib 128-point vector encoding)
* **Programming Languages:** Python 3, JavaScript, Shell Scripting

---

## System Architecture & Features
1. **Real-time Interface:** Displays live clock, calendar, weather forecast, and news tickers using asynchronous API calls.
2. **Facial Recognition:** Captures video stream frames via the Pi Camera, generates facial encodings, and matches them against stored profile datasets.
3. **Automated Personalization:** Switches UI modules dynamically upon recognizing a specific user.
4. **Auto-Boot Scripting:** Configured using system `autostart.sh` to run headlessly on system startup.

---

## Setup & Installation

1. **Clone the Repository:**
   ```bash
   git clone [https://github.com/shweta-hiremath942-creator/Smart-Mirror-Raspberry-Pi-3B-Plus.git](https://github.com/shweta-hiremath942-creator/Smart-Mirror-Raspberry-Pi-3B-Plus.git)
   cd Smart-Mirror-Raspberry-Pi-3B-Plus
