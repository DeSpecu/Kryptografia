import hashlib
import time
from datetime import datetime

class Hash:
    def __init__(self, dane):
        self.dane = dane
    
    def hashuj(self):
        algorytmy = hashlib.algorithms_available
        dane = self.dane.encode()
        for algorytm in algorytmy:
            start = time.perf_counter
            if "shake" not in algorytm:
                hash = hashlib.new(algorytm, dane).hexdigest()
            else:
                hash = hashlib.new(algorytm, dane).hexdigest(20)
            koniec = time.perf_counter
            #czas = koniec - start
            print(f"Algorytm: {algorytm}")
            print(hash)
            #print(f"Czas hashowania: {czas}")

    def check_sha256(self, sciezka):
        with open(sciezka, "rb") as f:
            hasher = hashlib.file_digest(f, "sha256")
        obliczony = hasher.hexdigest()
        print(f"Hash pliku: {obliczony}")



h = Hash("Lorem Ipsum")
h.hashuj()
h.check_sha256(r"C:\Users\szymk\Downloads\boot.img")