import os
os.system('pip install -e .')
os.system('pip install -e ".[train]"')
os.system('python -m  opensora.serve.gradio_web_server')