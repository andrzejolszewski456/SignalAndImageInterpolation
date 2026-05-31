import numpy as np
import matplotlib.pyplot as plt

def f1(x):
  return np.sin(x)

def f2(x):
  noweX = np.where(x != 0, x, 1e-10)
  return np.sin(1.0 / noweX)

def f3(x):
  return np.sign(np.sin(8 * x))

def h1(skala):
  t = np.linspace(0, 1, skala, endpoint=False)
  jadro = np.ones_like(t)
  return jadro / np.sum(jadro) * skala

def h2(skala):
  t = np.linspace(-0.5, 0.5, skala, endpoint=False)
  jadro = np.ones_like(t)
  return jadro / np.sum(jadro) * skala

def h3(skala):
  numPunktow = 2 * skala + 1
  t = np.linspace(-1, 1, numPunktow)
  jadro = np.maximum(0, 1 - np.abs(t))
  return jadro / np.sum(jadro) * skala

def h4(skala):
  promien = 4
  numPunktow = 2 * promien * skala + 1
  t = np.linspace(-promien, promien, numPunktow)
  jadro = np.sinc(t) * np.hamming(len(t))
  return jadro / np.sum(jadro) * skala

def interpolujSygnal(xOrg, yOrg, skala, fJadro):
  n = len(yOrg)
  nNowe = n * skala
  yUpsampled = np.zeros(nNowe)
  yUpsampled[::skala] = yOrg
  jadro = fJadro(skala)
  yInterp = np.convolve(yUpsampled, jadro, mode='same')
  xNowe = np.linspace(xOrg[0], xOrg[-1], nNowe)
  return xNowe, yInterp

def liczMse(yPrawdziwe, yPred):
  return np.mean((yPrawdziwe - yPred)**2)

liczbaPunktow = 100
funkcje = [f1, f2, f3]
skale = [2, 4, 10]
listaJader = [h1, h2, h3, h4]
nazwyFunkcji = ["sin(x)", "sin(1/x)", "sgn(sin(8x))"]

for fIdx, funkcjaCel in enumerate(funkcje):
  for skalaInterp in skale:
    fig, osie = plt.subplots(2, 2, figsize=(15, 10))
    fig.suptitle(f'Funkcja: {nazwyFunkcji[fIdx]}, Skala: x{skalaInterp}, N={liczbaPunktow}', fontsize=16)

    xOryginalne = np.linspace(-np.pi, np.pi, liczbaPunktow)
    yOryginalne = funkcjaCel(xOryginalne)

    for i, fJadro in enumerate(listaJader):
      xWykres = i // 2
      yWykres = i % 2

      xNowe, yEst = interpolujSygnal(xOryginalne, yOryginalne, skalaInterp, fJadro)
      yPrawdziwePelne = funkcjaCel(xNowe)
      mseWartosc = liczMse(yPrawdziwePelne, yEst)

      osie[xWykres, yWykres].plot(xOryginalne, yOryginalne, 'bo', label='Oryginał', markersize=4)
      osie[xWykres, yWykres].plot(xNowe, yEst, 'ro', markersize=3, alpha=0.5, label='Zinterpolowane')

      osie[xWykres, yWykres].set_title(f'Jądro h{i+1}, błąd MSE: {round(mseWartosc, 6)}')
      osie[xWykres, yWykres].grid(True)
      osie[xWykres, yWykres].legend(loc='upper right')

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()