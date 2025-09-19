# 🤖 Rock-Paper-Scissors Smart AI

A computer vision-based Rock-Paper-Scissors game that uses hand gesture recognition and AI pattern learning to create an intelligent opponent.

## 🎮 Features

- **Real-time Hand Gesture Detection**: Uses MediaPipe to detect rock, paper, scissors, and thumbs-up gestures
- **Smart AI Opponent**: Learns from your playing patterns to predict and counter your moves
- **Interactive Gameplay**: Visual countdown and real-time scoring
- **Computer Vision**: Live camera feed with hand landmark visualization

## 🚀 How It Works

1. **Gesture Recognition**: The system uses MediaPipe to track hand landmarks and classify gestures
2. **Pattern Learning**: The AI analyzes your move patterns to predict your next move
3. **Strategic Countering**: The AI counters your predicted move to maximize its chances of winning
4. **Real-time Feedback**: Visual feedback shows your move, AI's move, and the result

## 📋 Prerequisites

- Python 3.7 or higher
- Webcam or camera device
- Windows, macOS, or Linux

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/rock-paper-smart-ai.git
   cd rock-paper-smart-ai
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv env
   ```

3. **Activate the virtual environment**
   - **Windows:**
     ```bash
     env\Scripts\activate
     ```
   - **macOS/Linux:**
     ```bash
     source env/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## 🎯 Usage

1. **Run the game**
   ```bash
   python main.py
   ```

2. **Game Controls**
   - Show a **thumbs up** gesture to start a new round
   - Make your move during the countdown (Rock, Paper, Scissors, Shoot!)
   - Press **'q'** to quit the game

3. **Gesture Recognition**
   - **Rock**: Closed fist (all fingers down)
   - **Paper**: Open hand (all fingers up)
   - **Scissors**: Two fingers up (index and middle finger)
   - **Thumbs Up**: Thumb up, other fingers down

## 🧠 AI Strategy

The AI uses a pattern recognition algorithm that:
- Tracks your move sequences
- Identifies common patterns in your gameplay
- Predicts your next move based on previous moves
- Counters your predicted move to win

## 📁 Project Structure

```
rock-paper-smart-ai/
├── main.py              # Main game loop and UI
├── game_logic.py        # Game rules and winner determination
├── gesture_detector.py  # Hand gesture recognition
├── pattern_ai.py        # AI pattern learning algorithm
├── requirements.txt     # Python dependencies
├── .gitignore          # Git ignore file
└── README.md           # This file
```

## 🔧 Technical Details

- **Computer Vision**: OpenCV for camera handling and image processing
- **Hand Tracking**: MediaPipe for robust hand landmark detection
- **AI Algorithm**: Markov chain-based pattern recognition
- **Real-time Processing**: Optimized for smooth gameplay experience

## 🎮 Gameplay Tips

- The AI learns from your patterns, so try to be unpredictable!
- Make sure your hand is clearly visible in the camera frame
- Good lighting helps with gesture recognition
- The AI gets smarter as you play more rounds

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests
- Improve the AI algorithm

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- [MediaPipe](https://mediapipe.dev/) for hand tracking capabilities
- [OpenCV](https://opencv.org/) for computer vision processing
- The computer vision and AI communities for inspiration

---

**Have fun playing! 🎉**
