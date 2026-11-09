import os
from pathlib import Path

folders = [
    "part_a_numerical",
    "part_b_images",
    "part_c_text",
    "gui",
    "models"
]

files = {
    "README.md": "# Machine Learning Project\n\nوصف المشروع وكيفية تشغيله.",
    "requirements.txt": "pandas\nnumpy\nscikit-learn\nstreamlit\nopencv-python\nmatplotlib",
    ".gitignore": "venv/\n__pycache__/\n*.pkl\n*.joblib\n.ipynb_checkpoints/\n",
    "part_a_numerical/car_price_regression.ipynb": "",
    "part_b_images/flowers_classification.ipynb": "",
    "part_c_text/bbc_news_classification.ipynb": "",
    "gui/app.py": "import streamlit as st\n\nst.title('ML Project Dashboard')"
}

for folder in folders:
    os.makedirs(folder, exist_ok=True)
    print(f"Created folder: {folder}/")

for filepath, content in files.items():
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Created file: {filepath}")

print("\n✅ تم إنشاء هيكل المشروع بنجاح!")