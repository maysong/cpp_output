import subprocess

def get_clipboard_data():
    p = subprocess.Popen(['pbpaste'], stdout=subprocess.PIPE)
    retcode = p.wait()
    data = p.stdout.read()
    return data

strings = get_clipboard_data().splitlines()

for s in strings:
    print("cout << \"" + s + "\" << endl;")
