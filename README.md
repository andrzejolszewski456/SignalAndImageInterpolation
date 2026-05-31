# Signal & Image Interpolation Benchmark

A comprehensive Python performance and visual analysis tool that evaluates various signal and image interpolation techniques. The project implements 1D and 2D resampling methods using custom interpolation kernels (convolution-based) and measures their reconstruction accuracy using Mean Squared Error (MSE).

---

## How to Run

### Method 1: Google Colaboratory (fastest)
1. Download the files `SignalInterpolation.py` and `ImageInterpolation.py` from GitHub.
2. Open **[Google Colaboratory](https://colab.research.google.com/)**. This environment has all required libraries (`numpy`, `scipy`, `matplotlib`) pre-installed.
3. Click the blue button **"New notebook"**.
4. Paste the code from GitHub into the notebook cells.
5. Run the program.

### Method 2: Anaconda
1. Download the **[Anaconda Distribution](https://www.anaconda.com/download)**. This environment has all required libraries (`numpy`, `scipy`, `matplotlib`) pre-installed.
2. Open the **Anaconda Navigator** app, go to *Home*, find **Jupyter Notebook** (or *Anaconda Toolbox*) and click **"Launch"**.
3. Create a new notebook or open the downloaded files.
4. Run the program.

### Method 3: Local execution
1. Download the files from github
2. Install your favourite environment and needed libraries - NumPy, matplotlib and scipy
3. Run program


## Key Features
* **1D Signal Interpolation:** Evaluates various interpolation kernels on different functional patterns, including smooth continuous functions sin(x), high-frequency oscillating behaviors sin(1/x), and non-continuous step functions sgn(sin(8x)).
* **2D Image Processing:** Simulates an image downsampling-upsampling pipeline using synthetic 2D geometric patterns to test structural preservation.
* **Custom Convolution Kernels:** Pure NumPy/SciPy-backed implementations of multiple sampling kernels:
  * **h1 / h2:** Nearest-neighbor and box-car averaging filters.
  * **h3:** Linear / Bilinear interpolation (triangle kernel).
  * **h4:** Sinc interpolation for superior high-frequency preservation.
* **Statistical Metrics & Visualization:** Automatically computes real-time **Mean Squared Error (MSE)** to quantify reconstruction quality and plots side-by-side comparative charts via Matplotlib.
  
---

```text
signal-and-image-interpolation/
├── README.md                     # Project documentation and guidelines
├── SignalInterpolation.py        # 1D signal sampling and kernel benchmark
└── ImageInterpolation.py         # 2D image downsampling & interpolation pipeline
```
