# 🧑‍🏫 UFCFAS-15-2 Machine Learning · Week 1 · Day 2 Lecturer Walkthrough
## Instructor Delivery Plan: Hands-On Containerized ML Workshop
**Module:** Machine Learning (Level 5 · 15 Credits · UFCFAS-15-2)  
**Lecturer:** Sudan Pudasaini · The British College Nepal  
**Class Duration:** 1.5 Hours (90 Minutes)  
**Tone:** Light, hands-on, high-engagement, building confidence.

---

## 🧭 Lesson Architecture (90 Minutes)

| Segment | Time | Pedagogical Objective | Instructor Activity |
|---|---|---|---|
| **1. Hook & Recap** | 00–10m (10m) | Demystify Docker for ML | Explain the "Works on my machine" crisis in ML (NumPy C-extensions, Python versions, CUDA drivers). |
| **2. Smoke Test** | 10–20m (10m) | Baseline verification | Have every student run `docker run hello-world` in terminal. TAs/lecturer catch WSL/Docker Desktop issues early. |
| **3. Live Code: ML App** | 20–40m (20m) | Code understanding | Walk through `data.csv`, `train_and_predict.py`, and `Dockerfile` on the projector. Keep it simple and intuitive ($y = mx + c$). |
| **4. Build & Local Run** | 40–55m (15m) | Container lifecycle | Students run `docker build -t my-first-ml:v1 .` and `docker run --rm -v $(pwd)/output:/app/output my-first-ml:v1`. Inspect `model.joblib`. |
| **5. Docker Hub Push** | 55–70m (15m) | Professional cloud publishing | Students tag with `<username>/my-first-ml:v1` and push to Docker Hub. Show live repos on the big screen! |
| **6. Course Image Pull** | 70–85m (15m) | Toolkit readiness | Students pull `docker pull alkimi/ml:week1` and spin up JupyterLab on `http://localhost:8888`. |
| **7. Wrap-up & Class 3** | 85–90m (05m) | Anticipation for Class 3 | Connect today's model to tomorrow's 1-hour session on Gradient Descent and Cost Functions. |

---

## 🎯 Key Pedagogical Hooks & Talking Points

### Hook 1: Why Not Just Run `pip install`?
> *"Who here has spent 3 hours debugging a Python installation where Pandas was 1.x, NumPy was 2.x, and Scikit-Learn crashed with a C-extension compilation error? In industry, Machine Learning engineers NEVER run models directly on bare operating systems. Everything is containerized."*

### Hook 2: The Model is Just an Artifact
> *"Notice that after training, our container writes `model.joblib`. That file IS the machine learning model. In Week 2 and beyond, when you build recommendation systems or classifiers, that `.joblib` file is what gets deployed to cloud servers."*

### Hook 3: The Lecturer's Image (`alkimi/ml:week1`)
> *"Just like in our CCD module where you pulled the cloud tools, here you pull `alkimi/ml:week1`. It contains our curated, university-approved stack: Python 3.12, JupyterLab 4, Scikit-Learn, Pandas, NumPy, Matplotlib, and Seaborn. You'll use this for all upcoming labs."*

---

## ⚠️ Common Pitfalls & Quick Fixes

| Student Problem | Root Cause | Instant Fix |
|---|---|---|
| `docker: command not found` | Docker Desktop not running or terminal opened before install | Start Docker Desktop, wait for whale icon to be steady, open fresh terminal window. |
| Windows WSL error | WSL2 virtualization not enabled in BIOS or Docker settings | In Docker Desktop Settings → General → Check "Use the WSL 2 based engine". |
| `Cannot connect to the Docker daemon` | Docker daemon service sleeping | Run Docker Desktop app from Applications / Start Menu. |
| Trailing dot forgotten on build | Ran `docker build -t my-first-ml:v1` | Remind students that `.` specifies the build context (current directory). |
| Docker push `denied: requested access to the resource is denied` | Tagged with `my-first-ml` without Docker Hub username | Must tag as `<YOUR_DOCKERHUB_USERNAME>/my-first-ml:v1` after running `docker login`. |
| Port 8888 already in use | Another Jupyter or Docker container running | Run `docker ps` and `docker stop <id>`, or map port `8889:8888`. |

---

## 📋 End of Class 2 Checkpoint
Before dismissing the class, verify:
- [ ] Every student has pushed their image to Docker Hub.
- [ ] Every student has pulled `alkimi/ml:week1` onto their laptop.
- [ ] Students know that Class 3 (1 hour) will dive into the mathematics of Linear Regression inside JupyterLab!
