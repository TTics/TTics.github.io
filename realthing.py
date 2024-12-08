from flask import Flask, request, jsonify, render_template, send_file, url_for
from gtts import gTTS
from pydub import AudioSegment
import os
import tempfile

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_audio():
    try:
        # Retrieve user input
        dur = float(request.form.get('duration', 1.0))  # Default duration if not provided
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

        # Process text into words
        lines = [line.strip() for line in text.split("\n") if line.strip()]
        words = []
        for line in lines:
            words.extend(line.split("  "))
        words = [word.strip() for word in words if word.strip()]

        temp_dir = tempfile.gettempdir()
        combined_audio_path = os.path.join(temp_dir, "final_audio.mp3")
        combined = AudioSegment.empty()

        for word in words:
            temp_audio_file = os.path.join(temp_dir, f"{word}.mp3")
            
            # Generate word audio
            tts = gTTS(word, lang="th", slow=False)
            tts.save(temp_audio_file)
            
            # Combine audio with pauses
            word_audio = AudioSegment.from_file(temp_audio_file)
            combined += word_audio + AudioSegment.silent(duration=dur * 1000)
            
            # Remove temporary audio file
            os.remove(temp_audio_file)

        # Save the combined audio file
        combined.export(combined_audio_path, format="mp3")
        
        # Return download link
        return jsonify({"message": "Audio file created successfully.", "download_url": url_for('download_audio', filename="final_audio.mp3")})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/download/<filename>')
def download_audio(filename):
    temp_dir = tempfile.gettempdir()
    file_path = os.path.join(temp_dir, filename)
    return send_file(file_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
