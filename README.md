# Bharat_Academix_AI_Surveillance_Sysyem_Project
# AI-Powered Hand Gesture Detection Surveillance System

An advanced computer vision security solution that monitors real-time video feeds to identify specific hand poses and instantly trigger automated emergency actions. Unlike traditional passive CCTV systems that require a human operator to notice an incident, this system actively intercepts threats and distress calls by analyzing human intent via hand gestures.

## 🚀 Features
* **Real-time Edge Processing:** Low-latency frame processing using lightweight coordinate extraction instead of heavy pixel arrays.
* **Custom Gesture Logic:**
  * 👍 **Thumbs to the Side:** Flags a suspicious nature, unusual behavior, or a potential threat in the surroundings.
  * 👎 **Thumbs Down:** Signals an active danger situation, immediate distress, or an emergency needing urgent intervention.
* **Automated Threat Alerts:** Dispatches multi-channel notification threads (logs, dashboard alerts, or email/SMS) when confidence exceeds a threshold (e.g., >85%).
* **Zero Hardware Overhead:** Operates on standard webcams or existing CCTV infrastructure without the need for wearable sensors.

---

## 🏗️ Technical Architecture & Pipeline

The system operates on a lightweight, sequential pipeline designed for low-latency deployment:
[ Video Input ] ──> [ Hand Landmark Tracking ] ──> [ Gesture Classification ] ──> [ Action/Alert Trigger ]
(CCTV/Webcam)          (MediaPipe/OpenCV)             (CNN / Deep Learning)          (SMS, Email, Logs)
**Video Input & Pre-processing:** Captures video streams via OpenCV, resizing and normalizing frames for illumination variations.
2. **Hand Landmark Tracking:** Uses **Google MediaPipe** to isolate hand regions and extract 21 distinct 3D knuckle coordinates.
3. **Feature Extraction & Classification:** Transforms coordinates into spatial geometric vectors (angles/distances) and passes them into a trained **Deep Learning Model (CNN/MobileNet)**.
4. **Automated Notification:** Activates immediate security protocols upon positive gesture verification.

---

## 🛠️ Built With

* **Language:** Python
* **Computer Vision:** OpenCV, MediaPipe
* **Deep Learning:** TensorFlow / Keras (or PyTorch)
* **Data Infrastructure:** NumPy, Pandas, Scikit-learn

---

## 💻 Installation & Setup

Follow these steps to set up the project locally on your machine.

### Prerequisites
Ensure you have **Python 3.8 or higher** installed on your system. You can check your version by running:
```bash
python --version

Set Up a Python Virtual Environment
It is highly recommended to isolate dependencies using a virtual environment.

On Windows:

Bash
python -m venv venv
venv\Scripts\activate
On macOS/Linux:

Bash
python3 -m venv venv
source venv/bin/activate



Install Dependencies
Once the virtual environment is active, upgrade pip and install the required libraries:

Bash
pip install --upgrade pip
pip install opencv-python mediapipe tensorflow numpy pandas scikit-learn
(Alternatively, if you provide a requirements.txt file, use the command below)

Bash
pip install -r requirements.txt
🖥️ Usage
To run the real-time surveillance application using your default webcam feed:

Bash
python app.py
python gesture_detector.py
