# C++ & Python Linear Regression Tool
A high-performance linear regression application that combines a **C++ backend** for mathematical calculations with a **Python frontend** for data visualization.

## Features
- **High Performance:** Calculation logic (slope and y-intercept) is written in C++ and linked via `ctypes`.
- **Visualization:** Generates professional-grade regression plots using Matplotlib.
- **Standalone Executable:** Fully bundled for macOS using PyInstaller.

## How It Works
The project uses a "bridge" approach:
1. **LinReg.cpp**: Contains the math logic. It is compiled into a shared library (`liblinreg.dylib`).
2. **LinearRegressionGraph.py**: The user interface. It loads the compiled C++ library using Python's `ctypes` module to perform the calculations.
3. **Matplotlib**: Used to render the scatter plot of data points and the calculated line of best fit.
4. **Math equation for linear regression:** Y = a + bx, a = [ (Σy)(Σx²) − (Σx)(Σxy) ] / [ n(Σx²) − (Σx)² ], b = [ n(Σxy) − (Σx)(Σy) ] / [ n(Σx²) − (Σx)² ]


## Files in this Repo
- `LinearRegressionGraph.py`: The main Python script.
- `LinReg.cpp`: The human-readable C++ source code.
- `liblinreg.dylib`: The compiled machine-code library (Apple Silicon).
- `dist/`: Contains the standalone executable version.

## Installation & Usage

### Method 1: Use the Standalone App (Easiest) - Works only with Mac, M1 chips and after
1. Go to the **Releases** section of this GitHub repo.
2. Download the `LinearRegressionGraph.zip`.
3. Unzip the file.
4. **Right-click** the file and select **Open** (required for the first run on macOS to bypass the "unidentified developer" warning).

### Method 2: Run from Source
If you want to run the code manually, ensure you have Python 3.14+ and Matplotlib installed:
```bash 
pip install matplotlib
python3 LinearRegressionGraph.py
```







