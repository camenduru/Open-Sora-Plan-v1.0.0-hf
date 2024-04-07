import os
from time import time
os.system('pip install -e .')
time.sleep(10)
os.system('python  opensora/serve/gradio_web_server.py')