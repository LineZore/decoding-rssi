# Reproduction of Key Figures and Table

## Project Description

This repository provides the complete code and data required to reproduce key figures from the paper *"Decoding RSSI Compression in RFID: Dynamic RCS Modeling and Tag-Intrinsic Power Metrics for Reliable Backscatter Networks"*. This resource enables researchers to:

- Verify key results presented in the paper
- Build upon existing code for further analysis

## 📊 Correspondence with Paper Figures

### Key Figures and Table
| Paper Figure | Code Files | Data Files | Environment |
|--------------|-----------------|-------------|-------------|
| **Figure 10** | `src/diff.py` | `data/diff.txt` | Python |
| **Figure 14** | `src/Fig14_process.py` <br> `src/Fig14.py` | `rssi_cor_error.txt` <br> `data/processed_data/csv/` | Python |
| **Figure 15** | `src/Fig15_process.py` <br> `src/Fig15.py`  | `rssi_cor_dis_error.txt` <br> `data/processed_data/csv/` | Python |
| **Figure 16** | `src/matlab/draw_3dbarR6P.m`<br> `src/matlab/draw_3dbarU8.m` <br> `src/matlab/draw_3dbar9640.m` | `data/processed_data/3d/` | MATLAB |
| **Figure 17** | `src/cdf.py` | `data/processed_data/itp/` | Python |
| **Figure 18** | `src/discdf.py` | `data/processed_data/dis/` | Python |
| **Table 1** |  | `data/time.xlsx` | EXCEL |

### Other Figures

| Paper Figure | Code Files | Data Files | Environment |
|--------------|-----------------|-------------|-------------|
| **Figure 8** | `others/Fig8.py` | `data/R420_H47.txt` | Python |
| **Figure 9** | `others/Fig9.py` | `data/R420_H47.txt` | Python |
| **Figure 12** | `others/Fig12.py`  | `data/R420_*.txt` <br> `data/9900_*.txt` | Python |
| **Figure 13** | `others/Fig13.py` | `data/R420_*.txt` <br> `data/9900_*.txt` | Python |
| **Figure 19** | `others/Fig19.py` | `data/R420_*.txt` | Python |

## Contents Overview

### 📁 Data Files

```text
data/
├── processed_data/     # Processed data derived from raw data
│   ├── 3d/             # Data used to generate Figure 16
│   ├── csv/            # Intermediate data used to generate Figure 14 and Figure 15
│   ├── dis/            # Data used to generate Figure 18
│   ├── itp/            # Data used to generate Figure 17
│   ├── rssi_cor_dis_error.txt/         # Data used to generate Figure 15
│   └── rssi_cor_error.txt/             # Data used to generate Figure 14
├── 9900_9640.txt        # Raw experimental data
├── 9900_R6P.txt         # Raw experimental data
├── 9900_U8.txt          # Raw experimental data
├── diff.txt             # Raw data across four scenarios, used to generate Figure 10
├── R420_9640.txt        # Raw experimental data
├── R420_H47.txt         # Raw experimental data
├── R420_R6P.txt         # Raw experimental data
├── R420_U8.txt          # Raw experimental data
└── time.xlsx            # Raw data related to time efficiency

```

### 🐍 Code Files

```text
src/
├── matlab/             # MATLAB scripts for analyzing the robustness of BPI (Figure 16)
├── cdf.py              # Python script for plotting errors of the in-situ method (Figure 17)
├── diff.py             # Python script for plotting BPI robustness across four scenarios (Figure 10)
├── discdf.py           # Python script for plotting errors in ITP-based distance estimation (Figure 18)
├── Fig14_process.py    # Script for further processing data
├── Fig14.py            # Script analyzing the impact of transmit power on correction error (Figure 14)
├── Fig15_process.py    # Script for further processing data
├── Fig15.py            # Script analyzing the impact of distance on correction error (Figure 15)
├── rssi_cor.py         # Script for preprocessing raw RSSI data
└── to_3d.py            # Script for preprocessing raw RSSI data

others/
├── Fig8.py            # Script analyzing the impact of transmit power on BPI (Figure 8)
├── Fig9.py            # Script analyzing the impact of χ on BPI (Figure 9)
├── Fig12.py            # Script analyzing the impact of transmit power on RSSI (Figure 12)
├── Fig13.py            # Script analyzing the impact of distance on RSSI (Figure 13)
└── Fig19.py            # Script analyzing the tag diversity on BPI. (Figure 19)

```

## Environment Requirements

### Python Environment
- **Python Version**: 3.8+
- **Dependencies**:
  - `numpy`,
  - `matplotlib`,
  - `math`,
  - `pandas`.

### MATLAB Environment
- **MATLAB Version**: R2020a+

## Quick Start
### 1. Clone or download this repository.

### 2. Install required Python dependencies.
### 3. Data preprocessing.
The raw experimental data is stored in  `./data` directory.


To prepare the data for visualization, you need to run the following two Python preprocessing scripts:

  - `rssi_cor.py`:
  - `to_3d.py`:

(Note: We have already included the processed data in the repository, so you may skip this step if you wish to use the pre-processed files directly.)

Run the following commands to execute the preprocessing scripts:​

```bash
python ./src/to_3d.py
python ./src/rssi_cor.py
```

After execution, the processed data will be saved in the `./data/processed_data/` directory.​

### 4. Generating Figures

Each figure in the report is generated by running its corresponding Python script located in the `./src/` directory.

The output figures will be automatically saved in the ./figures/directory (please ensure this folder exists or is created by the script).

**​​Example:​**

To generate ​​Figure 10​​ (BPI curves under four different scenarios), run:

```bash
python ./src/diff.py
```

Other available scripts for generating figures include:​

```bash
python ./src/cdf.py
python ./src/discdf.py
python ./others/Fig8.py
python ./others/Fig9.py
python ./others/Fig12.py
python ./others/Fig13.py
python ./others/Fig19.py
```

Further processing is required before drawing figure 14 or figure 15:

``` bash
python ./src/Fig14_process.py
python ./src/Fig15_process.py
```

And run:

``` bash
python ./src/Fig14.py
python ./src/Fig15.py
```

*​​Note:​​* The mapping between each script and its corresponding figure is also detailed in the earlier ​​"Data Files"​​ and ​​"Code Files"​​ tables (or the Table of Contents / Figure Legend section).

**Special Note for Figure 16:​**

Figure 16 is generated using ​​MATLAB​​. The corresponding MATLAB code is located in the `./src/matlab/` directory.

## Detailed Information

This section provides a comprehensive overview of the dataset structure, data processing procedures, and the mapping between source code, datasets, and generated figures.

### 🔢 Raw Data File Description

#### 1. Tag RSSI Data (`R420_xxxx.txt` and `9900_xxxx.txt`)
Files such as `R420_9640.txt`, `9900_9640.txt` contain **RSSI readings** collected from the readers (R420 or 9900) and different tags.

- **Structure:**
  - **7 segments**, each corresponding to a fixed **tag-to-reader distance**: 2 m, 3 m, 4 m, 5 m, 6 m, 7 m, 8 m. (`R420_H47.txt` is different, it includes data of 1m, 2m, 3m, 4m, 6m, 8m, 9m)
  - **5 lines per segment**, where each line represents an **individual RFID tag sample**.
  - **91 RSSI values per line**, corresponding to **transmit power levels** ranging from **10 dBm to 32.5 dBm** with a **step size of 0.25 dBm**.

#### 2. Four Scenarios Data (`diff.txt`)
This file includes **four independent datasets**, each corresponding to a **different environmental scenario** (e.g., outdoors, office, lab, tagged cup).

- **Format:**
  - Each dataset consists of **two rows**:
    - **First row**: χ (The difference between transmit power and the expected ITP).
    - **Second row**: BPI (Backscattered Power Index) values derived from the power sweep method.

#### 3. Time Efficiency Data (`time.xlsx`)
An excel sheet containing measurement time under different ITP measurement methods.

- **Content:**
  - Measurements collected from **3 types of tags**.
  - Each individual tested **5 different individuals** using both:
    - **Power scanning method**
    - **In-situ method**
  - Including the **time consumption** for calculating ITP using each method.

---

### ⚙️ Data Processing Scripts

#### 1. `rssi_cor.py`
- **Function:** Performs **RSSI correction** on the raw data.
- **Output:**
  - Saves both **uncorrected** and **corrected RSSI values** into the file:  
    `data/processed_data/rssi_cor_error.txt`.

#### 2. `to_3d.py`
- **Function:** Conducts multi-purpose **data transformation and feature extraction** from the raw dataset.
- **Outputs (4 main outputs):**
  1. **ITP Estimation Error (2m, 3m, 4m)** → Saved in: `data/processed_data/itp/`
  2. **Distance Estimation Error (ITP vs. RSSI-based)** → Saved in: `data/processed_data/dis/`
  3. **BPI & χ Values for 3D Visualization** → Saved in: `data/processed_data/3d/`
  4. **RSSI Distance Correction Error** → Saved in: `data/processed_data/rssi_cor_dis_error.txt`

---

### 📈 Figure Generation Details

All figures are generated by executing their corresponding Python (or MATLAB) scripts. The resulting figures are saved in the `./figure/` directory (ensure it exists or is auto-created).

---

#### ▶️ Figure 10: BPI h(χ) vs. χ (4 Scenarios)
- **Description:** Plots the BPI metric as a function of χ across four different environmental scenarios.
- **Dataset:** `data/diff.txt`  
  - Contains 4 datasets (one per scenario).
  - Each dataset has:
    - **First row:** χ
    - **Second row:** h(χ)
- **Code:** `src/diff.py`  
  - **Output:** Figure saved in `./figure/`
  - **Run command:**
    ```bash
    python ./src/diff.py
    ```

---

#### ▶️ Figure 14: RSSI Correction Error with Respect to the Transmit Power
- **Description:** Compares the **deviation of RSSI values before and after correction** against the expected (ideal) RSSI.
- **Dataset:** `data/processed_data/rssi_cor_error.txt`  
  - Contains 5 sets of data.
  - Each set contains data for 3 tags: `'U8'`, `'R6P'`, `'9640'`.
  - For each tag:
    - **Row 1:** Transmit power (dBm)
    - **Row 2:** Uncorrected RSSI deviation
    - **Row 3:** Corrected RSSI deviation
- **Code:** 
  - **Output:** Figure saved in `./figure/`
  - **Run command:**
    ```bash
    python ./src/Fig14_process.py
    python ./src/Fig14.py
    ```

---

#### ▶️ Figure 15: RSSI Correction Error with Respect to the Distance
- **Description:** Compares the **deviation of RSSI values before and after correction** against the expected (ideal) RSSI.
- **Dataset:** `data/processed_data/rssi_cor_dis_error.txt`  
  - Contains 5 sets of data.
  - Each set contains data for 3 tags: `'U8'`, `'R6P'`, `'9640'`.
  - For each tag:
    - **Row 1:** Distance (m)
    - **Row 2:** Uncorrected RSSI error
    - **Row 3:** Corrected RSSI error
- **Code:** 
  - **Output:** Figure saved in `./figure/`
  - **Run command:**
    ```bash
    python ./src/Fig15_process.py
    python ./src/Fig15.py
    ```
---

#### ▶️ Figure 16: 3D Histogram (BPI h(χ) vs. Distance & χ)
- **Description:** Visualizes the relationship between **BPI**, **distance**, and **χ** using a **3D histogram**.
- **Dataset:** Processed data stored in `data/processed_data/3d/`
  - Each file corresponds to a tag.
  - Each row contains a triplet: **distance, χ, BPI h(χ)**
- **Code:** MATLAB script (located in `./src/matlab/`)
  - **Prerequisite:** Ensure `to_3d.py` has been run to generate input data.
  - **Pre-generated figures** are provided in `./figure/`.

---

#### ▶️ Figure 17: In-Situ Method Accuracy (3m–5m)
- **Description:** Evaluates the **accuracy of the in-situ ITP estimation method** at distances of 3 m, 4 m, and 5 m.
- **Dataset:** `data/processed_data/itp/`
  - Each file corresponds to a tag.
  - Each file contains **three lines**, each representing the **error of the in-situ method** across samples at a given distance.
- **Code:** `src/cdf.py`
  - **Output:** Figure saved in `./figure/`
  - **Run command:**
    ```bash
    python ./src/cdf.py
    ```

---

#### ▶️ Figure 18: In-Situ Method vs. RSSI-Based Distance Estimation
- **Description:** Compares **distance estimation accuracy** between the **in-situ method** and the **original RSSI-based method**.
- **Dataset:** `data/processed_data/dis/`
  - Each file corresponds to a tag.
  - Each file contains:
    - **Line 1:** Error of ITP-based distance estimation of all samples.
    - **Line 2:** Error of RSSI-based distance estimation of all samples.
- **Code:** `src/discdf.py`
  - **Output:** Figure saved in `./figure/`
  - **Run command:**
    ```bash
    python ./src/discdf.py
    ```

---

#### ▶️ Table 1: Measurement Time Comparison
- **Description:** Presents the **time consumption** of the **power scanning method** vs. the **in-situ method**, measured across:
  - **5 individuals**
  - **3 tag types**
- **Source:** The data was measured using two methods, reader R420 and corresponding tags.
- **Usage in Paper:** The values shown in **Table 1** of the paper are derived from the **mean section** of this dataset.

---

#### ▶️ Other Figures:
Figure 8-9 , Figure 12-13 and Figure 19 used to showcase certain aspects of BPI.
- **Description:** Extract data directly from raw data for display purposes.
- **Dataset:** `data/R420_*.txt` and `data/9900_*.txt`
- **Code:** 
  - **Output:** Figure saved in `./figure/`
  - **Run command:**
    ```bash
      python ./others/Fig8.py
      python ./others/Fig9.py
      python ./others/Fig12.py
      python ./others/Fig13.py
      python ./others/Fig19.py
    ```

---