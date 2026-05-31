import numpy as np
import matplotlib.pyplot as plt
from scipy import signal, ndimage

def h2(skala):
  t = np.linspace(-0.5, 0.5, skala, endpoint=False)
  jadro = np.ones_like(t)
  return jadro / np.sum(jadro) * skala

def h3(skala):
  promien = 1
  numPunktow = 2 * skala + 1
  t = np.linspace(-promien, promien, numPunktow)
  jadro = np.maximum(0, 1 - np.abs(t))
  return jadro / np.sum(jadro) * skala

def pomniejszObraz(obraz, skala):
  jadroUsredniajace = np.ones((skala, skala)) / (skala**2)
  obrazRozmyty = signal.convolve2d(obraz, jadroUsredniajace, mode='same')
  malyObraz = obrazRozmyty[::skala, ::skala]
  return malyObraz

def powiekszObraz(obraz, skala, funkcjaJadra):
  wysokosc, szerokosc = obraz.shape
  jadro1d = funkcjaJadra(skala)

  obrazKolumny = np.zeros((wysokosc, szerokosc * skala))
  obrazKolumny[:, ::skala] = obraz
  interpPozioma = ndimage.convolve1d(obrazKolumny, jadro1d, axis=1, mode='reflect')

  obrazFinalny = np.zeros((wysokosc * skala, szerokosc * skala))
  obrazFinalny[::skala, :] = interpPozioma
  interpPionowa = ndimage.convolve1d(obrazFinalny, jadro1d, axis=0, mode='reflect')

  return interpPionowa

def liczMse(obraz1, obraz2):
  h = min(obraz1.shape[0], obraz2.shape[0])
  w = min(obraz1.shape[1], obraz2.shape[1])
  return np.mean((obraz1[:h, :w] - obraz2[:h, :w])**2)

# 1. Tworzenie obrazu syntetycznego
rozmiar = 120
obrazOryginalny = np.zeros((rozmiar, rozmiar))
obrazOryginalny[30:90, 30:90] = 1.0
obrazOryginalny[50:70, 50:70] = 0.5

# 2. Definicja scenariuszy (skala_pomniejszenia, skala_powiekszenia, jadro, nazwa)
scenariusze = [
  (2, 2, h2, "Jądro h2"),
  (7, 7, h2, "Jądro h2"),
  (2, 2, h3, "Jądro h3"),
  (7, 7, h3, "Jądro h3")
]

fig, osie = plt.subplots(4, 3, figsize=(15, 18))
plt.subplots_adjust(hspace=0.4)

for i, (sPom, sPow, fJadro, nazwaJadra) in enumerate(scenariusze):
  # Kolumna 1: Oryginał
  osie[i, 0].imshow(obrazOryginalny, cmap='gray')
  osie[i, 0].set_title(f"Oryginał\n{obrazOryginalny.shape}")

  # Kolumna 2: Pomniejszony
  maly = pomniejszObraz(obrazOryginalny, sPom)
  osie[i, 1].imshow(maly, cmap='gray')
  osie[i, 1].set_title(f"Pomniejszony x{sPom}\n{maly.shape}")

  # Kolumna 3: Powiększony
  powiekszony = powiekszObraz(maly, sPow, fJadro)
  mseWartosc = liczMse(obrazOryginalny, powiekszony)
  osie[i, 2].imshow(powiekszony, cmap='gray')
  osie[i, 2].set_title(f"Powiększony x{sPow} ({nazwaJadra})\nMSE: {mseWartosc:.6f}")

for ax in osie.flat:
  ax.axis('off')

plt.show()