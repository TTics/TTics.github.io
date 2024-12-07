from gtts import gTTS
import os
import time
import pygame

dur = float(input("How long would you like the program to pause between each word?(seconds) "))
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

line = text.split("  ")

game = []
for gay in line:
    game.extend(gay.split("\n"))

game = [bro for bro in game if bro != ""]
pygame.mixer.init()
import tempfile

# Replace `temp_audio_file` generation with:
temp_dir = tempfile.gettempdir()  # Get the system's temp directory
temp_audio_file = os.path.join(temp_dir, f"temp_word_{id}.mp3")

for x in game:
    
    sound = gTTS(x, lang="th", slow=False)
    sound.save("temp.mp3")
    
    pygame.mixer.music.load("temp.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)
    pygame.mixer.music.stop()
    pygame.mixer.quit()
    pygame.mixer.init()  # Reinitialize mixer to prepare for next word

    
    if len(x) > 9:
        time.sleep(dur * 1.5)

    else:
        time.sleep(dur)
    
    os.remove("temp.mp3")

n = input("Enter any key to exit")