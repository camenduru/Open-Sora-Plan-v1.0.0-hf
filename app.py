import os
os.system('pip install -e .')
import time
print(111111111)
time.sleep(3)
print(222222222)
os.system('python  opensora/serve/gradio_web_server.py')