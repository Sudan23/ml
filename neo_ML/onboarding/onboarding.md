# 🤖 Machine Learning (UFCFAS-15-2)
## Week 0 — Student Onboarding Guide
**The British College Nepal · 2025–26**

| | |
|---|---|
| **Awarding University** | UWE Bristol (Level 5) |
| **Delivered at** | The British College Nepal |
| **Your Lecturer** | Sudan Pudasaini |

---

Welcome to **Machine Learning**. This module is about building real ML systems — not just theory. You'll write Python code, train models, evaluate them, and think critically about what they actually learn.

This year we're adding a modern layer on top: **Docker** for consistent environments, **GitHub** for submission and accountability, and **AI coding tools** to help you explore faster — but never to replace your understanding.

Before your first session on **October 5**, complete this setup. Everything is **free**.

---

## 🗺️ What You'll Be Using This Semester

| Tool | What For | Cost |
|------|----------|------|
| **Docker Desktop** | Run JupyterLab locally — no JupyterHub login issues | Free |
| **GitHub** | Submit notebooks; track your contributions to group project | Free |
| **VS Code** | Edit Python and notebooks outside Jupyter | Free |
| **GitHub Copilot** | AI autocomplete for Python/ML code | Free (student) |
| **Gemini / OpenCode** | AI for exploring ML concepts and architectures | Free |
| **Google Colab** *(optional)* | GPU access for deep learning weeks | Free |

> **Note on JupyterHub:** The UWE CSCT JupyterHub is available as a remote backup, but Docker gives you a local, always-available environment that works from anywhere — including Nepal.

---

## ✅ Step-by-Step Setup

### 1. Create Your GitHub Account

1. Go to [github.com](https://github.com) → **Sign Up**
2. Use your **college or personal email** (you will link your UWE student ID later)
3. Verify your email
4. Apply for the **[GitHub Student Developer Pack](https://education.github.com/pack)**
   - This gives you **free GitHub Copilot** — excellent for Python/ML code
   - Takes ~24 hours to approve — do this today!

---

### 2. Join GitHub Classroom (ML)

Sudan Pudasaini will share the invite link in the first class.  
Once you accept:
- A personal repo is created: `ml-2025-<your-github-username>`
- Each week, your completed notebooks go here — **all cells must be executed (outputs visible)**

> 📋 Group project teams will share a **separate group repo** — set up in Week 5.

---

### 3. Install Docker Desktop

Each week you'll pull a pre-built image with Python, JupyterLab, and all ML libraries already installed. No more `pip install` errors or version conflicts.

1. Download: [docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop/)
2. Install and launch Docker Desktop
3. Verify:
```bash
docker --version
# Expected: Docker version 27.x.x or later
```

---

### 4. Pull the ML Week 1 Image

```bash
docker pull ghcr.io/lbu-courses/ml-course:week1
```

> ⏳ ~1.2GB — pull on a good connection before class.

**Run it — this opens JupyterLab in your browser:**
```bash
docker run -p 8888:8888 -v $(pwd):/home/student/notebooks/mywork \
  ghcr.io/lbu-courses/ml-course:week1
```

Then open: **[http://localhost:8888](http://localhost:8888)**

You'll see Week 1 notebooks pre-loaded and ready to go. ✅

**What's inside the Week 1 image:**
```
✅ Python 3.12
✅ JupyterLab 4
✅ NumPy, Pandas, Matplotlib, Seaborn
✅ scikit-learn
✅ Week 1 starter notebook (linear regression)
✅ Titanic & SUV datasets pre-loaded
```

---

### 5. Install VS Code + Extensions

Useful for editing Python files and reviewing notebooks outside of Jupyter.

1. Download [code.visualstudio.com](https://code.visualstudio.com/)
2. Install:
   - **Python** by Microsoft
   - **Jupyter** by Microsoft
   - **GitHub Copilot** *(sign in with GitHub student account)*
   - **Docker** by Microsoft

---

### 6. Install OpenCode (AI Terminal Assistant)

```bash
npm install -g opencode-ai     # requires Node.js from nodejs.org
opencode --version             # verify
```

**Or use Gemini:** [aistudio.google.com](https://aistudio.google.com) — free, works in browser, no install.

---

## 📬 Week 0 Submission

In your GitHub Classroom repo, create `SETUP.md`:

```markdown
# ML Week 0 — Setup Verification

**Name:** [Your full name]
**GitHub:** [Your GitHub username]
**Student Number:** [Your UWE student number]

## Docker Verification
(Paste the output when you run: `docker run ghcr.io/lbu-courses/ml-course:week1 python3 --version`)

## Quick Python Check
Run this inside the container and paste the output:
```python
import sklearn, pandas, numpy
print(sklearn.__version__, pandas.__version__, numpy.__version__)
```

## I'm looking forward to learning...
[One sentence about what aspect of ML interests you most]
```

Commit and push:
```bash
git add SETUP.md
git commit -m "Week 0: setup complete"
git push
```

---

## 🤖 AI Usage in This Module

This module actively teaches you to use AI tools — **but also to be critical of them**. ML models (including the AI you'll use) have biases, make mistakes, and can fail silently.

| ✅ Encouraged | ❌ Not Allowed |
|---|---|
| Ask Copilot to generate model code, then evaluate it | Submit AI-written analysis as your own insights |
| Use AI to explore hyperparameter choices | Have AI write your group project proposal |
| Ask AI to explain what a confusion matrix shows | Use AI to fill in notebook markdown reflections |
| Prompt AI to suggest a different dataset to try | Copy AI code without running or understanding it |

> 🧠 **The key question to ask yourself:** *"Can I explain every line of this code and why it works?"* If not, keep digging.

**Weekly `REFLECTION.md` format** (required every week):

```markdown
## Week X — AI Reflection

**What I asked AI:** "Suggest hyperparameter values for an SVM on the Titanic dataset"
**What AI suggested:** C=1.0, kernel='rbf', gamma='scale'
**What I actually tried:** C=0.5, C=1.0, C=5.0 — compared accuracy
**Result:** C=1.0 gave best validation accuracy (83.2%)
**What I learned:** Higher C reduces regularisation — overfits when too large
```

---

## 📋 Your Assessment Reminders

| Component | Weight | Deadline |
|-----------|--------|----------|
| Group Project Proposal | **10%** | Week 7 (in lab) |
| Individual Assignment | **TBC** | Week 9 |
| Group Project | **TBC** | Week 12 hand-in |

Your GitHub repo commit history is evidence of your individual contribution to the group project. **If you don't commit, you don't get credit.**

---

## 🖥️ Deep Learning Weeks (Weeks 8–12)

From Week 8 (ANNs and CNNs), pull the **deep learning image** instead:

```bash
docker pull ghcr.io/lbu-courses/ml-course:week8-dl
docker run -p 8888:8888 ghcr.io/lbu-courses/ml-course:week8-dl
```

This adds TensorFlow and Keras to the environment.  
Google Colab is available as an alternative if you need GPU access.

---

## ❓ Help & Support

| Channel | Use For |
|---------|---------|
| **GitHub Discussions** in your course org | Technical Python/Docker questions |
| **Email Sudan Pudasaini** | Include your GitHub username + student number |
| **UWE Blackboard** | Official module announcements and assessment submissions |
| **Class sessions at TBC** | Best for hands-on debugging — bring your laptop |

---

*See you October 5! Let's build something that actually learns. 🧠*
