import os
import sys
current_path = os.path.abspath(__file__)
parent_path = os.path.dirname(current_path)
print(parent_path)
sys.path.append(parent_path)
print(sys.path)
os.system('CUDA_VISIBLE_DEVICES=0 python opensora/serve/gradio_web_server.py')