from sys import platform


if platform == "linux" or platform == "linux2":
    os.system("pip install -r requirements.txt")
elif platform == "darwin":
    os.system("pip3 install -r requirements.txt")
elif platform == "win32":
    os.system("pip install -r requirements.txt")
