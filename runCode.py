import subprocess
PATH = "Code/"
def runCode(text):
    subprocess.call(['python', (PATH + text)])


