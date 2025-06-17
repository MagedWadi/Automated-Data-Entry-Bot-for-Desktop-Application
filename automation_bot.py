import os
import time
import requests
import pyautogui
import subprocess
from botcity.core import DesktopBot
# Ensure pauses between actions
pyautogui.PAUSE = 0.2
bot = DesktopBot()
bot.screenshot_path = "./assets"
#Prepare the directory
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
project_dir = os.path.join(desktop, 'tjm-project')

# Create the folder if it doesn't exist
if not os.path.exists(project_dir):
    os.makedirs(project_dir)
    print(f"Created project directory at {project_dir}")
else:
    # Folder exists: delete all .txt files
    for filename in os.listdir(project_dir): #loop through files in the directory
        # Check if the file is a .txt file
        if filename.endswith(".txt"):
            # Construct full file path
            file_path = os.path.join(project_dir, filename)
            try:
                os.remove(file_path) # delete the file
            except Exception as e:
                print(f"Failed to delete {file_path}. Reason: {e}")

def fetch_posts():
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/posts") # Fetching posts from the API
        response.raise_for_status() 
        return response.json()[:10] 
    except requests.RequestException as e:
        print(f"Error fetching posts: {e}") 
        return []

def open_notepad():
    try:
        # Launch Notepad
        subprocess.Popen(["notepad.exe"])
        time.sleep(2)  
    except Exception as e:
        print(f"Error launching Notepad: {e}")
        bot.screenshot(f"error_launching_Notepad.png")
        return False
    return True

def type_blog_post(post):
    try:
        # Type the blog post title and body in the .txt file
        pyautogui.write(f"{post['title']}\n\n")
        pyautogui.write(post['body'])
    except Exception as e:
        print(f"Error typing blog post: {e}")
        bot.screenshot(f"error_typing_{post['id']}.png")

def save_file(post_id):
    try:
        # Save the file with the post ID as the filename
        pyautogui.hotkey('ctrl', 's')
        time.sleep(1)
        save_path = os.path.join(project_dir, f"post {post_id}.txt")
        pyautogui.write(save_path)
        pyautogui.press('enter')
        time.sleep(1)
    except Exception as e:
        print(f"Error saving file: {e}")

def close_notepad():
    pyautogui.hotkey('ctrl', 'w')
    time.sleep(1)

def main():
    posts = fetch_posts()
    #loop on all posts fetched from the API
    for post in posts:
        print(f"Processing Post ID {post['id']}")
        if open_notepad():
            type_blog_post(post)
            save_file(post['id'])
            close_notepad()
        else:
            print("Skipping this post due to Notepad error.")
            bot.screenshot(f"error_post_{post['id']}.png")

if __name__ == "__main__":
    main()