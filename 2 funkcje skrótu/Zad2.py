import hashlib
from time import time, sleep
import plotly.express as plotly
from pandas import DataFrame
import datetime

class Hash:
    def __init__(self, dane):
        self.dane = dane
        self.wynik = {}
    

    def hashuj(self):
        algorytmy = hashlib.algorithms_available
        dane = self.dane.encode()
        for algorytm in algorytmy:
            start = datetime.datetime.now()
            if "shake" not in algorytm:
                hash = hashlib.new(algorytm, dane).hexdigest()
            else:
                hash = hashlib.new(algorytm, dane).hexdigest(20)
            sleep(0.01)
            koniec = datetime.datetime.now()
            delta = (koniec - start)
            self.wynik[algorytm] = delta.total_seconds() * 1000 - 10
            print(f"Algorytm: {algorytm}")
            print(hash)
            print(f"Czas hashowania: {self.wynik[algorytm]}")

    def hash_plik(self, sciezka):
        with open(sciezka, "rb") as f:
            hasher = hashlib.file_digest(f, "sha256")
        obliczony = hasher.hexdigest()
        print(f"Hash pliku: {obliczony}")

    def tabela(self):
        plot = DataFrame(list(self.wynik.items()), columns=['Algorytm', 'Milisekundy'])
        wynik = plotly.scatter_polar(plot, r="Milisekundy",theta="Algorytm")
        wynik.show()



h = Hash("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")
h.hashuj()
h.hash_plik(r"C:\Users\szymk\Downloads\boot.img")
h.tabela()