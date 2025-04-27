import pyautogui
import easyocr
import time

# Initialize the EasyOCR reader
reader = easyocr.Reader(['en'])

# Function to capture the question area and return the extracted text
def capture_question(region):
    screenshot = pyautogui.screenshot(region=region)
    screenshot.save('question.png')  # Save the screenshot for OCR processing
    result = reader.readtext('question.png')
    if result:
        # Assuming the first detected text is the question
        return result[0][1].strip()
    return ""

# Function to parse the question and calculate the answer
def calculate_answer(question_text):
    # Assuming the question is in the format "7 x 8"
    parts = question_text.split('x')
    if len(parts) == 2:
        try:
            num1 = int(parts[0].strip())
            num2 = int(parts[1].strip())
            return num1 * num2
        except ValueError:
            return None
    return None

# Function to automate answering the question
def answer_question(region):
    question_text = capture_question(region)
    answer = calculate_answer(question_text)
    if answer is not None:
        pyautogui.typewrite(str(answer))
        pyautogui.press('enter')

# Main loop to continuously answer questions
def main():
    question_region = (x, y, width, height)  # Define the region where the question appears
    while True:
        answer_question(question_region)
        time.sleep(1)  # Adjust the delay as needed

# Run the main loop
main()