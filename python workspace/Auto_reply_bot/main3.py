import pyautogui
import pyperclip
import time

time.sleep(2)

pyautogui.click(1130, 1050)

time.sleep(1)

pyautogui.moveTo(714,191)
pyautogui.dragTo(1628, 920, duration=1, button='left')

time.sleep(1)

pyautogui.hotkey('ctrl', 'c')
pyautogui.click(1555, 967)
time.sleep(0.3)

copied_text = pyperclip.paste()

pyautogui.click(1290,1045)
time.sleep(0.2)

print("Copied text:")
print(copied_text)

from google import genai

# Pass your Gemini API key here
client = genai.Client(api_key="AIzaSyBQPaRhb4JpqYEegQlQnQDTieNEvRixSpM")

response = client.models.generate_content(
    model="gemini-2.5-flash-lite",
    contents=f"""You are a close friend chatting on WhatsApp. 
When I send you a message, you reply informally, naturally, and concisely. 
Do NOT explain, analyze, or give multiple options — just one short unfriendly,rude and slang reply also use abusing words.just do Tit for tat.
Message: {copied_text}"""
)

print(response.text)


reply_text = response
pyperclip.copy(response.text)
time.sleep(0.2)

pyautogui.click(1130, 1050)
time.sleep(0.2)

pyautogui.click(871, 968)
time.sleep(0.2)


pyautogui.hotkey("ctrl", "v")
time.sleep(0.2)
pyautogui.press("enter")

pyautogui.click(1345,1045)
time.sleep(0.2)

print("Reply sent:")