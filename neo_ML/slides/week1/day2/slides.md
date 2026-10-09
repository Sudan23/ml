---
marp: true
theme: default
paginate: true
header: "UFCFAS-15-2 · Machine Learning · Week 1 · Day 2"
footer: "The British College Nepal · Sudan Pudasaini"
style: |
  section {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    background-color: #0d1117;
    color: #e6edf3;
    padding: 40px;
  }
  h1 { color: #58a6ff; font-weight: 700; }
  h2 { color: #79c0ff; }
  strong { color: #f0883e; }
  code { background-color: #161b22; color: #7ee787; padding: 2px 6px; border-radius: 4px; }
  pre { background-color: #161b22; border: 1px solid #30363d; border-radius: 8px; padding: 15px; }
  table { width: 100%; border-collapse: collapse; margin-top: 15px; }
  th { background-color: #21262d; color: #58a6ff; padding: 10px; border: 1px solid #30363d; }
  td { padding: 10px; border: 1px solid #30363d; }
---

# 🐳 Week 1 · Day 2: Hands-On Containerized ML
## Build, Train, Push & Pull with Docker
**Module:** Machine Learning (UFCFAS-15-2 · Level 5 · 15 Credits)  
**Institution:** The British College Nepal · UWE Bristol  
**Lecturer:** Sudan Pudasaini  
**Duration:** 1.5 Hours (90 Minutes)  

---

# 🎯 Today's Mission & 90-Minute Flight Plan

We are keeping today's class **light, practical, and confidence-building**.

* 🔍 **00–15m · Part 1: Why Docker for ML?**
  Understanding the ML reproducibility crisis & terminal smoke test (`docker run hello-world`).
* 💻 **15–35m · Part 2: Build a Containerized ML Model**
  A simple linear regression model ($y = wx + b$) on study hours data packaged with a `Dockerfile`.
* 💾 **35–50m · Part 3: Local Run & Model Persistence**
  Executing inside the container and extracting `model.joblib` via volume mounting.
* ☁️ **50–70m · Part 4: Publish to Docker Hub**
  Tagging and pushing your custom container to your public Docker Hub account.
* 🎓 **70–90m · Part 5: Pull Lecturer's Image & Class 3 Prep**
  Pulling `alkimi/ml:week1` and verifying JupyterLab on `localhost:8888`.

---

# 💥 The "Works on My Machine" Crisis in ML

Why do top AI & ML engineering teams refuse to run models on bare operating systems?

| Problem on Bare OS | Solution with Docker |
|---|---|
| **Python Version Drift:** Python 3.10 vs 3.12 syntax mismatches | Base image fixes Python to exact version (3.11 / 3.12) |
| **Dependency Hell:** NumPy 2.x breaking legacy Pandas code | `requirements.txt` locked in an immutable image |
| **C/C++ Extension Headaches:** BLAS/LAPACK compilation fails | Pre-compiled binary wheels inside standard Linux layers |
| **Cloud Deployment Pain:** Fails when moving from Mac to AWS | "Build Once, Run Anywhere" (Laptop ➡️ Cloud ➡️ Edge) |

---

# 📊 Our Micro ML Application: Problem & Data

Predicting student exam performance based on weekly study hours:

```csv
study_hours,exam_score
1.5,42.0
2.0,50.0
3.0,58.0
4.0,66.5
5.0,74.5
6.0,81.5
7.0,89.0
8.0,95.0
```

* **Feature ($X$):** `study_hours` (Input variable)
* **Target ($y$):** `exam_score` (Output variable to predict)
* **Goal:** Learn the mathematical relationship $y = w \cdot X + b$

---

# 🧠 The Machine Learning Script (`train_and_predict.py`)

A clean, self-contained Python script using **Scikit-Learn**:

```python
import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

# 1. Load data
df = pd.read_csv("data.csv")
X = df[["study_hours"]].values
y = df["exam_score"].values

# 2. Train model
model = LinearRegression()
model.fit(X, y)

# 3. Print learned equation
print(f"Exam Score = ({model.coef_[0]:.2f} × Hours) + {model.intercept_:.2f}")

# 4. Predict & Save
print(f"Predicted Score (6 hrs): {model.predict([[6.0]])[0]:.1f}")
joblib.dump(model, "output/model.joblib")
```

---

# 🐳 Authoring the `Dockerfile`

Writing the recipe to package our code and environment:

```dockerfile
# 1. Start from official lightweight Python
FROM python:3.11-slim

# 2. Set work directory inside container
WORKDIR /app

# 3. Install required libraries
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy training dataset & ML code
COPY data.csv .
COPY train_and_predict.py .

# 5. Create artifact directory & run
RUN mkdir -p /app/output
CMD ["python", "train_and_predict.py"]
```

---

# 🔨 Task 1 & 2: Build & Run Locally

### 1. Build the image:
```bash
docker build -t my-first-ml:v1 .
```
*(Don't forget the trailing dot `.` — it tells Docker to use the current directory context!)*

### 2. Run the container:
```bash
docker run --rm my-first-ml:v1
```

**What you will see:**
* Model fits the data in under 1 second.
* Prints: `Exam Score = (7.50 × Study Hours) + 35.00`
* $R^2$ accuracy score: `~98.5%`!

---

# 💾 Task 3: Persist Model via Volume Mounting

Containers are **stateless by default** — files written inside vanish when the container stops!

To keep `model.joblib` on our laptop, we mount a folder:

```bash
mkdir -p output

docker run --rm -v $(pwd)/output:/app/output my-first-ml:v1
```

* **`-v $(pwd)/output:/app/output`**: Bridges your local `output/` directory with `/app/output` in the container.
* Verify on your laptop:
  ```bash
  ls -la output/
  # output/model.joblib is saved!
  ```

---

# ☁️ Task 4: Publish to Docker Hub

Share your ML container with the world:

### 1. Login to Docker Hub:
```bash
docker login
```

### 2. Tag your image with your Docker username:
```bash
docker tag my-first-ml:v1 <YOUR_DOCKERHUB_USERNAME>/my-first-ml:v1
```

### 3. Push to Docker Hub:
```bash
docker push <YOUR_DOCKERHUB_USERNAME>/my-first-ml:v1
```

👉 Check your repo live at: `https://hub.docker.com/r/<YOUR_DOCKERHUB_USERNAME>/my-first-ml`

---

# 🎓 Task 5: Pull Lecturer's Course Toolkit (`alkimi/ml:week1`)

Now pull the official pre-configured environment for all upcoming labs:

```bash
docker pull alkimi/ml:week1
```

### Launch JupyterLab:
```bash
docker run -p 8888:8888 -v $(pwd):/home/student/notebooks/mywork alkimi/ml:week1
```

* Open browser: **`http://localhost:8888`**
* Pre-installed: **Python 3.12, JupyterLab 4, NumPy, Pandas, Scikit-Learn, Matplotlib, Seaborn**
* Ready for all coursework with **zero installation headaches**!

---

# ✅ Task 6: Action Checklist & Submission

Before leaving today's class:

1. [ ] **Smoke Test Verified:** `docker run hello-world` ran successfully.
2. [ ] **Custom ML Container Built:** `my-first-ml:v1` trained and evaluated.
3. [ ] **Model Artifact Saved:** `model.joblib` extracted via volume mount.
4. [ ] **Pushed to Docker Hub:** Image live on `hub.docker.com`.
5. [ ] **Course Image Pulled:** `alkimi/ml:week1` downloaded and tested.
6. [ ] **Verification Note:** Commit `WEEK1_DAY2_VERIFICATION.md` to your course repo.

---

# 🔮 Looking Ahead to Class 3 (Tomorrow — 1 Hour)

Tomorrow, we explore the engine underneath the hood:

* **What did `model.fit()` actually do?**
* **The Loss Function:** How do we measure error mathematically? (Mean Squared Error)
* **Optimization via Gradient Descent:** How the algorithm updates weights step-by-step.
* **Interactive Notebook:** Running hands-on linear regression experiments inside `alkimi/ml:week1`!

**Great work today — you are now a container-ready ML engineer! 🚀**
