# Spectranova

![Language](https://img.shields.io/badge/Language-Python-3776AB?style=flat-square) ![Stars](https://img.shields.io/github/stars/Devanik21/SpectraNova?style=flat-square&color=yellow) ![Forks](https://img.shields.io/github/forks/Devanik21/SpectraNova?style=flat-square&color=blue) ![Author](https://img.shields.io/badge/Author-Devanik21-black?style=flat-square&logo=github) ![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square)

> Spectral analysis and signal intelligence — Fourier, wavelet, and AI-powered spectrum characterisation for scientific and engineering applications.

---

**Topics:** `astronomy` · `astrophysics-ml` · `attention-mechanism` · `deep-learning` · `dimensionality-reduction` · `machine-learning` · `neural-networks` · `spectroscopy` · `astronomical-spectra` · `spectral-line-identification`

## Overview

SpectraNova is a comprehensive spectral analysis platform that combines classical signal processing
(Fourier transform, Short-Time Fourier Transform, Continuous Wavelet Transform) with machine learning
methods (spectral clustering, anomaly detection, classification from spectral features) for a wide
range of spectral data types: audio signals, vibration data, optical spectra, electromagnetic spectra,
and time-series measurements from scientific instruments.

The platform is designed to serve multiple user communities simultaneously. For signal processing
engineers, it provides a rigorous implementation of spectral estimation methods (periodogram,
Welch's method, multitaper) with window function comparison and resolution-variance trade-off
analysis. For data scientists, it provides a feature extraction pipeline that converts raw spectra
into ML-ready feature vectors and feeds them into scikit-learn classifiers and anomaly detectors.
For domain scientists, it provides a configurable analysis pipeline for specific spectral formats
including astronomical spectra (FITS), vibrational spectra (CSV from spectrometers), and audio
recordings.

A key strength of SpectraNova is its wavelet analysis module: unlike Fourier analysis, which assumes
stationarity, the Continuous Wavelet Transform (CWT) provides time-frequency localisation — revealing
how the frequency content of a signal evolves over time. This makes it particularly powerful for
analysing non-stationary signals like seismic data, financial time series, and biomedical signals.

---

## Motivation

Spectral analysis is a universal analytical tool that appears in physics, engineering, biology, finance,
and astronomy — yet each domain typically uses domain-specific software with limited cross-pollination
of methods. SpectraNova was built to provide a domain-agnostic spectral analysis environment
that makes the mathematical machinery of signal processing accessible to any discipline working with
time-series or spectral data.

---

## Architecture

```
Signal Input (time-series / spectrum data)
        │
  Preprocessing: detrending, normalisation, windowing
        │
  ┌──────────────────────────────────────────────┐
  │  Classical Spectral Analysis:                │
  │  ├── FFT / Periodogram / Welch's method      │
  │  ├── STFT (spectrogram)                      │
  │  └── CWT (time-frequency wavelet map)        │
  └──────────────────────────────────────────────┘
        │
  ┌──────────────────────────────────────────────┐
  │  ML Analysis:                                │
  │  ├── Feature extraction (spectral centroid,  │
  │  │   bandwidth, rolloff, MFCC, peaks)        │
  │  ├── Spectral classification (RF / SVM)      │
  │  └── Anomaly detection (Isolation Forest)   │
  └──────────────────────────────────────────────┘
        │
  Interactive Plotly / Matplotlib visualisation
```

---

## Features

### Multi-Method Power Spectral Density Estimation
Comparison of periodogram, Welch's method, multitaper estimation, and Lomb-Scargle (for unevenly sampled data) — with resolution and variance trade-off visualisation.

### Short-Time Fourier Transform Spectrogram
STFT spectrogram with configurable window function (Hann, Hamming, Blackman, Kaiser), window length, and hop size — displayed as an interactive Plotly heatmap with log frequency axis.

### Continuous Wavelet Transform
CWT with Morlet, Mexican Hat, and Paul wavelet families for time-frequency analysis of non-stationary signals, with scalogram (wavelet power spectrum) visualisation.

### Spectral Feature Extraction
Automatic computation of 20+ spectral features per signal: centroid, bandwidth, spectral rolloff, flatness, kurtosis, MFCCs (for audio), and peak frequency/amplitude pairs.

### ML Spectral Classifier
Train a RandomForest or SVM classifier on spectral feature vectors for signal type classification (e.g., bearing fault type, material identification, instrument recognition).

### Anomaly Detection
Isolation Forest and One-Class SVM anomaly detection on spectral features — flagging measurements that deviate significantly from the baseline distribution for quality control applications.

### Window Function Comparison
Side-by-side comparison of Hann, Hamming, Blackman, Flat-top, and Kaiser window functions with their frequency domain characteristics (main lobe width, side lobe level, scalloping loss).

### Batch Spectral Processing
Process directories of signal files with the same analysis configuration, outputting feature CSVs and spectral plots for each file — suitable for large-scale spectral databases.

---

## Tech Stack

| Library / Tool | Role | Why This Choice |
|---|---|---|
| **NumPy / SciPy** | Signal processing core | FFT, Welch, STFT, window functions, filtering |
| **PyWavelets** | Wavelet transforms | CWT, DWT, scalogram computation |
| **LibROSA** | Audio spectral features | MFCC, spectral centroid, chromagram |
| **scikit-learn** | ML classification/anomaly | RandomForest, SVM, Isolation Forest on spectral features |
| **Plotly** | Interactive visualisation | Spectrograms, CWT scalograms, feature comparison charts |
| **Matplotlib** | Static publication figures | High-resolution spectral plots for reports |
| **Astropy (optional)** | Astronomical spectra | FITS file I/O and Lomb-Scargle for unevenly sampled data |

---

## Getting Started

### Prerequisites

- Python 3.9+ (or Node.js 18+ for TypeScript/JavaScript projects)
- A virtual environment manager (`venv`, `conda`, or equivalent)
- API keys as listed in the Configuration section

### Installation

```bash
git clone https://github.com/Devanik21/SpectraNova.git
cd SpectraNova
python -m venv venv && source venv/bin/activate
pip install numpy scipy pywavelets librosa scikit-learn plotly matplotlib pandas streamlit
streamlit run app.py
```

---

## Usage

```bash
# Analyse a signal file
streamlit run app.py

# FFT analysis from CLI
python spectral_analysis.py --input signal.wav --method welch --window hann

# CWT scalogram
python wavelet_analysis.py --input vibration.csv --wavelet morlet --scales 32

# Train spectral classifier
python train_classifier.py --data spectra_labelled/ --model rf

# Batch processing
python batch_analyse.py --input_dir ./spectra/ --output features.csv
```

---

## Configuration

| Variable | Default | Description |
|---|---|---|
| `DEFAULT_METHOD` | `welch` | PSD estimation: periodogram, welch, multitaper |
| `WINDOW_FUNCTION` | `hann` | Spectral window: hann, hamming, blackman, kaiser |
| `WAVELET_FAMILY` | `morlet` | CWT wavelet: morlet, mexh, paul |
| `N_MFCC` | `13` | Number of MFCC coefficients to extract |
| `ANOMALY_CONTAMINATION` | `0.05` | Expected anomaly fraction for Isolation Forest |

> Copy `.env.example` to `.env` and populate required values before running.

---

## Project Structure

```
SpectraNova/
├── README.md
├── requirements.txt
├── app.py
└── ...
```

---

## Roadmap

- [ ] Hilbert-Huang Transform for adaptive analysis of nonlinear, non-stationary signals
- [ ] Neural spectral analysis: 1D-CNN trained on spectral images for end-to-end classification
- [ ] Real-time analysis mode with streaming input from audio devices or serial port sensors
- [ ] Spectral database: store and query labelled spectra with metadata for reference comparison
- [ ] Publication-ready figure generator with configurable DPI, font size, and colour scheme

---

## Contributing

Contributions, issues, and suggestions are welcome.

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-idea`
3. Commit your changes: `git commit -m 'feat: add your idea'`
4. Push to your branch: `git push origin feature/your-idea`
5. Open a Pull Request with a clear description

Please follow conventional commit messages and add documentation for new features.

---

## Notes

CWT computation time scales with the number of scales and signal length — large signals with many scales may take 10–60 seconds. For real-time applications, prefer STFT or DWT (faster) over CWT. Spectral analysis results depend critically on preprocessing choices (detrending, windowing) — document these carefully in any scientific publication.

---

## Author

**Devanik Debnath**  
B.Tech, Electronics & Communication Engineering  
National Institute of Technology Agartala

[![GitHub](https://img.shields.io/badge/GitHub-Devanik21-black?style=flat-square&logo=github)](https://github.com/Devanik21)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-devanik-blue?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/devanik/)

---

## License

This project is open source and available under the [MIT License](LICENSE).

---

*Built with curiosity, depth, and care — because good projects deserve good documentation.*
