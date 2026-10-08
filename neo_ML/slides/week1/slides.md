---
marp: true
theme: default
paginate: true
header: "Machine Learning (UFCFAS-15-2) · Week 1 · Class 1"
footer: "The British College Nepal (UWE Bristol) · Sudan Pudasaini"
style: |
  section {
    font-family: 'Inter', system-ui, -apple-system, sans-serif;
    background-color: #0f172a;
    color: #f8fafc;
    padding: 40px 60px;
  }
  h1 {
    color: #38bdf8;
    font-size: 2.2rem;
  }
  h2 {
    color: #818cf8;
    font-size: 1.7rem;
  }
  h3 {
    color: #38bdf8;
    font-size: 1.3rem;
  }
  p, li {
    font-size: 1.15rem;
    line-height: 1.6;
    color: #cbd5e1;
  }
  strong {
    color: #f1f5f9;
  }
  code {
    background-color: #1e293b;
    color: #38bdf8;
    padding: 2px 6px;
    border-radius: 4px;
    font-family: 'JetBrains Mono', monospace;
  }
  pre {
    background-color: #1e293b;
    border: 1px solid #334155;
    border-radius: 8px;
    padding: 16px;
  }
  pre code {
    background-color: transparent;
    padding: 0;
  }
  blockquote {
    border-left: 4px solid #38bdf8;
    background: #1e293b;
    padding: 12px 20px;
    border-radius: 0 8px 8px 0;
    color: #e2e8f0;
  }
  table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 15px;
    font-size: 1rem;
  }
  th {
    background-color: #1e293b;
    color: #38bdf8;
    padding: 10px;
    border: 1px solid #334155;
    text-align: left;
  }
  td {
    padding: 10px;
    border: 1px solid #334155;
  }
  .highlight {
    color: #facc15;
    font-weight: 600;
  }
---

# 🤖 Machine Learning (UFCFAS-15-2)
## Week 1 · Class 1: Course Orientation & Overview
### *Welcome, Expectations, Roadmap & Delivery*

**The British College Nepal · Academic Year 2026–27**  
**Awarding:** UWE Bristol · Level 6  
**Lecturer & Module Lead (TBC):** Sudan Pudasaini  
**Module Leader (UWE Bristol):** Prof. Jun Hong  

---

# 👋 First: Welcome & Let's Read the Room

### A quick show of hands:

* Who feels confident writing clean, object-oriented or functional **Python**?
* Who has used **NumPy, Pandas, or Matplotlib** for data manipulation?
* Who has previously trained a model with **Scikit-Learn, PyTorch, or TensorFlow**?
* Who uses **GitHub Copilot, Gemini, or Claude** in daily development?

> *"Machine learning at Level 6 is not about blindly copying library calls or memorizing math proofs. It is about understanding the mechanics of learning systems, writing production-grade code, and evaluating results honestly."*

---

# 🏛️ Course Identity & Academic Partnership

| | Details |
|---|---|
| **Module Title** | Machine Learning (`UFCFAS-15-2`) |
| **Level & Credits** | Level 6 · 15 UK Credits |
| **Awarding University** | **UWE Bristol** (University of the West of England) |
| **Delivery Institution** | **The British College (TBC)**, Kathmandu, Nepal |
| **Local Module Lead** | **Sudan Pudasaini** (Lectures, Labs, Mentorship) |
| **UWE Module Leader** | **Prof. Jun Hong** (Curriculum Architect & Quality Oversight) |
| **Module Tutors (UWE)** | Dr. Nathan Duran, Dr. Muhammad Khan |

---

# 🗓️ Our 3-Class-Per-Week Delivery Rhythm

We meet **three times every week**. Each session has a distinct, purposeful role:

```
┌─────────────────────────┬─────────────────────────┬─────────────────────────┐
│     CLASS 1 (Today)     │         CLASS 2         │         CLASS 3         │
│  Concept & Orientation  │   Technical Deep Dive   │  Hands-on Lab & Code    │
├─────────────────────────┼─────────────────────────┼─────────────────────────┤
│ • Conceptual foundation │ • Mathematical intuition│ • Practical coding lab  │
│ • Architecture & trade- │ • Algorithm mechanics   │ • Vectorized NumPy /    │
│   offs                  │ • Code walkthroughs     │   Scikit-Learn pipelines│
│ • Real-world relevance  │ • Edge cases & pitfalls │ • GitHub Org & Orbund   │
└─────────────────────────┴─────────────────────────┴─────────────────────────┘
```

> **Why this model?** You are never expected to go from abstract theory straight into assessment without guided code walkthroughs and dedicated in-class lab support.

---

# 🧭 How We Are Going to Learn: The 3 Core Pillars

| Pillar | What We Do | Real-World Value |
|---|---|---|
| **1. Grounded Intuition** | Understand *why* an algorithm optimizes before running it | Eliminates "black-box" guessing in debugging |
| **2. Production Craft** | Build from scratch in NumPy first, then master Scikit-Learn | Teaches you real ML engineering, not just scripting |
| **3. Critical Evaluation** | Probe models for overfitting, leakage, bias, and edge failure | Models that look perfect in Jupyter often fail in production |

---

# 🎓 University Expectations (UWE Level 6 Rigor)

As final-year / Level 6 computing students, university standards require:

1. **Active Ownership:** You are the author and architect of your work. Passive attendance will not build working models.
2. **Empirical Rigor:** You don't just say *"my model works"* — you justify it with confusion matrices, cross-validation, loss curves, and baseline comparisons.
3. **Reproducibility:** Code must execute end-to-end without hidden local state or manual interventions.
4. **Professional Communication:** Technical reports must follow academic standards (clear methodology, cited references, and critical analysis).

---

# ⚠️ The Non-Negotiable "Must-Do's"

* 🔑 **1. Week 0 Environment Setup by Tomorrow:**  
  Docker and GitHub accounts must be operational before Class 2. No exceptions.
* 📦 **2. Visible Cell Execution on Submissions:**  
  Notebooks pushed to the **course GitHub Organization** and submitted via **Orbund** must have executed cell outputs. Blank cells = zero grade.
* 🌿 **3. Genuine Git Commit Cadence:**  
  Work incrementally with descriptive commit messages. A single mass-upload 10 minutes before the deadline is a major academic red flag.
* 🤝 **4. Zero Team Ghosting:**  
  Group project contributions are audited via Git commit blame. **No commits = No contribution mark.**

---

# 🗺️ 12-Week Semester Roadmap: What We Will Learn

* **Weeks 1–3: The Core Foundations**
  - Week 1: Linear Regression & Gradient Descent Optimization
  - Week 2: Logistic Regression, Probability & Decision Boundaries
  - Week 3: End-to-End ML Workflow, Feature Engineering & Ethical AI
* **Weeks 4–7: Classical & Ensemble Mastery**
  - Weeks 4–5: Support Vector Machines (SVM), Margins & Kernel Tricks
  - Weeks 6–7: Decision Trees, Random Forests (Bagging) & AdaBoost (Boosting)
* **Weeks 8–12: Deep Learning & Computer Vision**
  - Week 8: Artificial Neural Networks (ANN), Forward/Backpropagation
  - Week 9: Convolutional Neural Networks (CNN) & Image Classification
  - Weeks 10–12: Deep Learning Group Project Implementation & Defense

---

# 📊 Assessment Structure & Deadlines

```
┌─────────────────────────────────────────────────────────────┐
│ 1. Group Project Proposal (10%)        Due: Week 7 (Lab)    │
│    Problem definition, dataset choice, baseline architecture│
├─────────────────────────────────────────────────────────────┤
│ 2. Individual Assignment (30%)         Due: Week 9 (Orbund) │
│    Comparative study: 2 distinct ML algorithms on 1 dataset │
│    Data pipeline, hyperparameter tuning, written report     │
├─────────────────────────────────────────────────────────────┤
│ 3. Group Project & Defense (60%)       Due: Week 12 (Orbund)│
│    End-to-end Deep Learning system (CNN / DNN application)  │
│    Full GitHub repo + working demo + team presentation      │
└─────────────────────────────────────────────────────────────┘
```

---

# 🚀 The Modernized Delivery Stack (`neo_ML`)

To ensure a smooth, industry-aligned experience, we've layered `neo_ML` on top:

* 🐳 **Dockerized Labs (No Environment Collisions):**
  Pre-built container with Python 3.12, JupyterLab 4, Scikit-Learn, Pandas, NumPy, and Seaborn.
  ```bash
  docker pull ghcr.io/sudan23/ml:week1
  docker run -it -p 8888:8888 -v $(pwd):/workspace ghcr.io/sudan23/ml:week1
  ```
* 🐙 **GitHub Organization & Orbund:**
  Code lives in student repositories under the **course GitHub Organization** with CI/CD checks; official grading and assessment submissions are managed through **Orbund**.
* 💻 **VS Code & Local Tooling:**
  Use VS Code with the Python & Jupyter extensions or your preferred IDE.

---

# 🤖 AI Coding Policy: "Co-Pilot, Never Auto-Pilot"

Generative AI (GitHub Copilot, Gemini, Claude) is part of modern engineering.  
We encourage you to use it — **with strict rules of engagement**:

| ✅ Allowed & Encouraged | ❌ Strictly Prohibited |
|---|---|
| Asking AI to explain error stack traces | Copying code blocks you cannot explain line-by-line |
| Querying syntax or library documentation | Generating assignment report text or conclusions |
| Exploring hyperparameter combinations | Having AI write your group project proposal |
| Generating unit tests & data visualizations | Blindly submitting unverified AI code |

> **Weekly Requirement:** Every push requires a 5-line `REFLECTION.md` documenting what you asked AI, what it suggested, what you verified, and what you learned.

---

# 📚 Essential Books & Learning Resources

* **Core Textbook:**
  * *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow* (3rd Edition) by Aurélien Géron. *(The gold standard practical guide)*
* **Reference Texts:**
  * *Artificial Intelligence: A Modern Approach* (4th Edition) by Stuart Russell & Peter Norvig.
  * *Neural Networks and Deep Learning* by Michael Nielsen *(free online: neuralnetworksanddeeplearning.com)*.
* **Official Documentation:**
  * [scikit-learn.org](https://scikit-learn.org) — Best-in-class documentation and user guides.

---

# ✅ Your Action Checklist Before Class 2

Complete these **before our next session**:

1. [ ] **Join Course GitHub Org & Access Orbund:** Accept the GitHub Org invite and ensure your Orbund course access is verified.
2. [ ] **Apply for GitHub Student Developer Pack:** Get free GitHub Copilot access ([education.github.com/pack](https://education.github.com/pack)).
3. [ ] **Install Docker Desktop:** Verify by running `docker --version`.
4. [ ] **Pull the Week 1 Image:**  
   `docker pull ghcr.io/sudan23/ml:week1`
5. [ ] **Read the Onboarding Guide:**  
   Check [`neo_ML/onboarding/onboarding.md`](file:///Users/sudan/Teaching/Current/ML/neo_ML/onboarding/onboarding.md) in the course repository.

---

# 🔮 Looking Ahead to Class 2 & Class 3

* **Class 2 (Tomorrow):**
  * What is a learning problem?
  * Supervised Learning formulation: Features $X$, Labels $y$, Hypothesis $h_\theta(x)$
  * **Linear Regression:** From intuition to the Mean Squared Error (MSE) loss bowl
  * **Gradient Descent:** Walking down the foggy mountain
* **Class 3 (Lab Session):**
  * Vectorized Gradient Descent from scratch in NumPy
  * Fitting models with `sklearn.linear_model.LinearRegression`
  * First repository push to GitHub Org and setup verification on Orbund!

---

# 💬 Questions & Discussion

### Let's open the floor!

* Questions on the syllabus, schedule, or assessments?
* Questions on Docker, GitHub Organization, or Orbund?
* Questions on AI policies or team allocations?

**Lecturer:** Sudan Pudasaini  
**Email & Support:** Available via TBC Faculty & GitHub Discussions  

*Welcome aboard — let's build systems that actually learn! 🚀*
