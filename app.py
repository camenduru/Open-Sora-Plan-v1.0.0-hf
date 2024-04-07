import os
os.system('pip install -e .')
import time
time.sleep(10)
os.system('python  opensora/serve/gradio_web_server.py')