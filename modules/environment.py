import os

# Pokaz zmienne srodowiskowe ze zdalnej maszyny
def run(**args):
    print "[*] W module environment."
    return str(os.environ)

