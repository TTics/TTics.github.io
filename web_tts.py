from flask import Flask, request, jsonify, render_template
from gtts import gTTS
import os
import time
import pygame
import tempfile
import re  # For splitting the text based on spaces or newlines

app = Flask(__name__)

# Initialize Pygame mixer
pygame.mixer.init()

@app.route('/')
def home():
    return render_template('index.html')  # Serve the HTML form for user input

@app.route('/play', methods=['POST'])
def play_audio():
    try:
        # Get input from the form
        dur = float(request.form.get('duration', 1.0))  # Default to 1.0 seconds if not provided
        text = """51. บวชชี                     52. บาสเกตบอล       53. บิณฑบาต                54. บุคลากร           55. เบญจเพส
56. แบตเตอรี่               57. ประณีต               58.ประดิดประดอย          59. ประดิษฐาน      60. ประหัตประหาร  
61.ปรานี                      62. ปาร์เกต์               63. เปอร์เซ็นต์                64. ผัดไทย            65. ผัดวันประกันพรุ่ง
66.ผาสุก                    67. เผอเรอ                68. พัศดี                          69. พิศวาส             70. เพชฌฆาต
71. ภาพยนตร์             72. ม่อลอกม่อแลก   73. มัธยัสถ์                       74. ย่อมเยา            75. รังเกียจเดียดฉันท์
76. แร็กเกต                77. ล็อกเกอร์            78. ลอตเตอรี่                    79. ลายเซ็น           80. เลิ่กลั่ก
81.โลกาภิวัตน์          82. เว็บไซต์               83. โศกศัลย์                      84. สังเกต              85. สับปะรด
86.สัมมนา                 87. สาบสูญ               88. สาปแช่ง                      89. สำมะโนครัว      90. สีสัน
91.หมาใน                 92. เหล็กใน               93. ออฟฟิศ                       94. อัธยาศัย           95. อาเพศ
96. อำนาจบาตรใหญ่ 97. อินเทอร์เน็ต        98. อิเล็กทรอนิกส์              99. อุทธรณ์            100.ไอศกรีม"""

        # Split text into words or phrases based on multiple spaces or newlines
        words = re.split(r'\s{2,}|\n', text)
        words = [word.strip() for word in words if word.strip()]  # Clean up and filter empty strings

        # Create the temp_files directory if it doesn't exist
        temp_dir = os.path.join(os.getcwd(), 'temp_files')
        if not os.path.exists(temp_dir):
            os.makedirs(temp_dir)

        for word in words:
            # Create a temporary file for the audio
            temp_audio_file_path = os.path.join(temp_dir, f"temp_word_{int(time.time())}.mp3")

            print(f"Generating audio for word: {word}")
            print(f"Audio file will be saved to: {temp_audio_file_path}")

            # Generate and save the audio file
            tts = gTTS(word, lang="th", slow=False)
            tts.save(temp_audio_file_path)  # Save the audio to the temp file

            # Play the audio
            pygame.mixer.music.load(temp_audio_file_path)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                time.sleep(0.1)

            # Stop the music and quit the mixer to release the file lock
            pygame.mixer.music.stop()
            pygame.mixer.quit()  # Ensure the mixer is reset and the file is released

            # Add a small delay before removing the file
            time.sleep(0.2)  # Give some time for the file to be released

            # Delete the temporary file after use
            if os.path.exists(temp_audio_file_path):
                os.remove(temp_audio_file_path)
            else:
                print(f"Failed to delete temp file: {temp_audio_file_path}")

            # Reinitialize the mixer for the next audio file
            pygame.mixer.init()

            # Adjust pause based on word length
            pause_duration = dur * 1.5 if len(word) > 9 else dur
            time.sleep(pause_duration)

        return jsonify({"message": "Audio playback completed successfully."})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Ensure the temp_files folder exists and print debug information
    temp_dir = os.path.join(os.getcwd(), 'temp_files')
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)
    print(f"Using directory for temp files: {temp_dir}")
    
    app.run(debug=True)
