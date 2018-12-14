import os

# lista plikow w katalogu
def run(**args):
    print "[*] W module dirlister"
    files = os.listdir(".")

    return str(files)