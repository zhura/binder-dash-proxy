from subprocess import Popen


def load_jupyter_server_extension(nbapp):
    Popen(["python", "app.py"])