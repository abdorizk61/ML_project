# End-to-End Machine Learning Project

This repository hosts a multi-modal Machine Learning project covering numerical regression, image classification, text classification, and a unified interactive GUI. The development environment is fully containerized using Docker to ensure reproducibility across all operating systems (Windows, macOS, and Linux).

---

## 📁 Repository Structure

```text
ML_Project_Team/
│
├── part_a_numerical/                     # Part A: Numerical Regression (Car Price)
│   ├── 01_eda_and_preprocessing.ipynb
│   ├── 02_linear_regression.ipynb
│   ├── 03_knn_regression.ipynb
│   └── 04_model_comparison.ipynb
│
├── part_b_images/                        # Part B: Image Classification (Flowers)
│   ├── 01_image_preprocessing_logistic.ipynb
│   ├── 02_knn_and_kmeans.ipynb
│   └── 03_ensemble_and_comparison.ipynb
│
├── part_c_text/                          # Part C: Text Classification (BBC News / Arabic)
│   ├── 01_text_preprocessing_logistic.ipynb
│   ├── 02_linear_svm.ipynb
│   └── 03_comparison_and_evaluation.ipynb
│
├── gui/                                  # Part D: Deployment GUI
│   └── app.py                            # Streamlit web interface
│
├── models/                               # Exported serialized models (.pkl / .joblib)
├── Dockerfile                            # Container specification
├── docker-compose.yml                    # Multi-container orchestration config
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

## 🚀 Quickstart: Setup & Run with Docker

To avoid dependency issues and version mismatches, all team members should run the environment via Docker.

### Prerequisites

1. **Install Docker:**
   * **Windows / macOS:** Install [Docker Desktop](https://www.docker.com/products/docker-desktop/). Ensure Docker Desktop is launched and running.
   * **Linux (Fedora / Ubuntu):** Install `docker` and `docker-compose-plugin`, then start the system service (`sudo systemctl enable --now docker`).
2. **Git:** Ensure Git is installed locally.

---

### Step-by-Step Instructions

#### 1. Clone the Repository
Open your terminal or Git Bash and clone the project:
```bash
git clone https://github.com/<YOUR_GITHUB_USERNAME>/ML_Project_Team.git
cd ML_Project_Team
```

#### 2. Start the Environment
Build the Docker image and launch the container by running:
```bash
docker compose up --build
```
> *Note: The initial build downloads base images and installs libraries (this takes a few minutes). Subsequent launches will take only seconds using `docker compose up`.*

#### 3. Access JupyterLab
Once the terminal displays startup logs, open your web browser and navigate to:
```text
http://localhost:8888
```
* You can create, edit, and run all `.ipynb` notebooks directly from your browser.
* All changes saved in JupyterLab are mirrored instantaneously on your host disk.

#### 4. Run the Streamlit GUI
When models are trained and saved into `models/`, launch the interactive dashboard:

In a new terminal window (from the project directory), run:
```bash
docker compose exec ml-environment streamlit run gui/app.py --server.port=8501 --server.address=0.0.0.0
```
Open your browser and visit:
```text
http://localhost:8501
```

#### 5. Stop the Environment
To stop the running container, press `Ctrl + C` in the running terminal, or execute:
```bash
docker compose down
```

---

## 🛠️ Team Collaboration & Git Best Practices

* **Feature Branches & Separate Notebooks:** Each member must work in their assigned notebooks and create meaningful commits to demonstrate individual contributions.
* **Avoid Modifying the Same Notebook Concurrently:** To prevent merge conflicts, keep changes compartmentalized within your designated notebook.
* **Random State:** Ensure `random_state=42` (or a standardized seed) is used across all train/test splits and model initializations for full reproducibility.
