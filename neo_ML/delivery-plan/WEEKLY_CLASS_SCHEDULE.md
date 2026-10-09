# 📅 UFCFAS-15-2 Machine Learning · Weekly Class Delivery Schedule
**Module:** Machine Learning (Level 5 · 15 UK Credits / 7.5 ECTS)  
**Institution:** The British College Nepal · Partnered with UWE Bristol  
**Lecturer:** Sudan Pudasaini  

---

## ⏰ Weekly Teaching Format (4 Hours / Week)
Each week comprises **3 distinct class sessions**:

| Session | Duration | Format | Primary Objective |
|---|---|---|---|
| **Class 1** | **1.5 Hours (90m)** | Interactive Lecture & Strategy | Core theoretical concepts, intuition, architectural principles, and module expectations. |
| **Class 2** | **1.5 Hours (90m)** | Hands-On Workshop / Lab | Tooling, coding implementations, container workflows, and practical experiments. |
| **Class 3** | **1.0 Hour (60m)** | Deep Dive / Practical Synthesis | Algorithmic mathematics, gradient descent drills, code analysis, and Q&A. |

---

## 🗓️ Week 1: Module Orientation & Machine Learning Setup

### Class 1 (1.5 Hours): Course Introduction, Workflow & Industry Standards
* **Academic Level:** Level 5 (15 UK Credits).
* **Assessment Model:** 100% Individual Project (Software codebase + 6-page report via Orbund).
* **Platforms:** Orbund (official grades & submissions) + Course GitHub Organization (repositories & CI/CD).
* **AI Policy:** "Co-Pilot, Never Auto-Pilot" (Reflection logs required).
* **Deliverable:** [Week 1 Class 1 Slides & Materials](file:///Users/sudan/Teaching/Current/ML/neo_ML/slides/week1/)

### Class 2 (1.5 Hours): Hands-On Containerized ML Workshop (Today)
* **Theme:** Light, interactive, practical confidence-building.
* **Problem & Data:** Student study hours vs exam scores (`data.csv`).
* **ML Application:** Python script training `scikit-learn` Linear Regression (`train_and_predict.py`).
* **Containerization:** Authoring a custom `Dockerfile` and building `my-first-ml:v1`.
* **Persistence:** Volume mounting host folder to save `output/model.joblib`.
* **Publishing:** Pushing to student's personal Docker Hub account (`<username>/my-first-ml:v1`).
* **Course Toolkit:** Pulling lecturer's official image (`docker pull alkimi/ml:week1`) and launching JupyterLab on `http://localhost:8888`.
* **Deliverables:**
  - [Slide Deck (`.pptx`)](file:///Users/sudan/Teaching/Current/ML/neo_ML/slides/week1/day2/Week_1_Class_2_HandsOn_Docker_ML.pptx)
  - [Interactive Web Deck](file:///Users/sudan/Teaching/Current/ML/neo_ML/slides/week1/day2/slides.html)
  - [Lab Task Guide](file:///Users/sudan/Teaching/Current/ML/neo_ML/slides/week1/day2/DAY_2_LAB_TASK_GUIDE.md)
  - [Lecturer Walkthrough](file:///Users/sudan/Teaching/Current/ML/neo_ML/slides/week1/day2/DAY_2_LECTURER_WALKTHROUGH.md)
  - [Starter Lab Code](file:///Users/sudan/Teaching/Current/ML/neo_ML/labs/week1/docker-ml/)

### Class 3 (1.0 Hour): Machine Learning Fundamentals & Linear Regression Math
* **Core Topics:**
  - Formulating the linear model: $y = w \cdot x + b$.
  - Measuring error: Mean Squared Error (MSE) cost function $J(w, b)$.
  - Optimization: Gradient Descent algorithm and learning rate $\alpha$.
  - Hands-on Jupyter notebook practical using pre-configured `alkimi/ml:week1`.
