# End-to-End Machine Learning Project

This repository hosts a multi-modal Machine Learning project covering numerical regression, image classification, text classification, and a unified interactive GUI.

---

## 📁 Repository Structure

```text
ML_Project_Team/
│
├── part_a_numerical/                     # Part A: Numerical Regression (Car Price)
│   ├── 01_eda_and_preprocessing.ipynb
│   ├── 02_linear_regression.ipynb
│   ├── 03_knn_regression.ipynb
│   ├── 04_model_comparison.ipynb
│   └── 05_ensemble_models.ipynb
│
├── part_b_images/                        # Part B: Image Classification (Flowers)
│   ├── 01_image_preprocessing_logistic.ipynb
│   ├── 02_knn_and_kmeans.ipynb
│   └── 03_ensemble_and_comparison.ipynb
│
├── part_c_text/                          # Part C: Text Classification (BBC News / Arabic)
│   ├── 01_text_preprocessing_logistic.ipynb
│   ├── 02_linear_svm.ipynb
│   ├── 03_comparison_and_evaluation.ipynb
│   └── 04_from_scratch_numpy.ipynb
│
├── gui/                                  # Part D: Deployment GUI
│   └── app.py                            # Streamlit web interface
│
├── models/                               # Exported serialized models (.pkl / .joblib)
├── requirements.txt                      # Python dependencies list
└── README.md                             # Setup guide and instructions
```

---

## 📊 Datasets & Sources

| Part | Task Type | Target / Objective | Dataset Source |
| :--- | :--- | :--- | :--- |
| **Part A** | Numerical Regression | Predict vehicle selling price | [CarDekho Vehicle Dataset (Kaggle)](https://www.kaggle.com/datasets/nehalbirla/vehicle-dataset-from-cardekho) |
| **Part B** | Image Classification | 5-class flower recognition | [Flowers Recognition (Kaggle)](https://www.kaggle.com/datasets/alxmamaev/flowers-recognition/data) |
| **Part C** | Text Classification | Multi-class news topic classification | [BBC News Archive (Kaggle)](https://www.kaggle.com/datasets/hgultekin/bbcnewsarchive) |

---

## 🚀 Quickstart: Local Setup & Run

Follow these steps to set up a local Python environment and run the notebooks and Streamlit dashboard.

### Prerequisites

* **Python 3.10+** (recommended: Python 3.11)
* **Git** installed locally

---

### Step-by-Step Instructions

#### 1. Clone the Repository
Open your terminal or Git Bash and clone the project:
```bash
git clone https://github.com/<YOUR_GITHUB_USERNAME>/ML_Project_Team.git
cd ML_Project_Team
```

#### 2. Create and Activate a Virtual Environment
Using Python's built-in `venv`:
```bash
# Create the virtual environment
python -m venv .venv

# Activate on Linux / macOS:
source .venv/bin/activate

# Activate on Windows (PowerShell):
# .venv\Scripts\Activate.ps1
```
*(Alternatively, if using `uv`: `uv venv && source .venv/bin/activate`)*

#### 3. Install Dependencies
Install all required packages from `requirements.txt`:
```bash
pip install --upgrade pip
pip install -r requirements.txt
```
*(Optional, for Part C NLTK tokenization/stopwords if needed)*:
```bash
python -m nltk.downloader stopwords punkt
```

#### 4. Open JupyterLab / Notebooks
Launch JupyterLab from the project root:
```bash
jupyter lab
```
* Your browser will open at `http://localhost:8888`.
* Navigate to `part_a_numerical/`, `part_b_images/`, or `part_c_text/` to run and edit the `.ipynb` notebooks.

#### 5. Run the Streamlit GUI
Once models are trained and saved into `models/`, launch the interactive dashboard:
```bash
streamlit run gui/app.py
```
Open your browser and visit:
```text
http://localhost:8501
```

---

## 🛠️ Team Collaboration & Git Best Practices

* **Feature Branches & Separate Notebooks:** Each member must work in their assigned notebooks and create meaningful commits to demonstrate individual contributions.
* **Avoid Modifying the Same Notebook Concurrently:** To prevent merge conflicts, keep changes compartmentalized within your designated notebook.
* **Random State:** Ensure `random_state=42` (or a standardized seed) is used across all train/test splits and model initializations for full reproducibility.
