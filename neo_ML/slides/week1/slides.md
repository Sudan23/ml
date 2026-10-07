---
marp: true
theme: default
paginate: true
header: "Machine Learning (UFCFAS-15-2) · Week 1"
footer: "The British College (UWE Bristol) · Sudan Pudasaini"
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
  .tag {
    display: inline-block;
    padding: 2px 8px;
    background: #0369a1;
    color: #e0f2fe;
    border-radius: 9999px;
    font-size: 0.85rem;
    font-weight: 600;
  }
---

# 🤖 Machine Learning
## Week 1: Module Welcome & Linear Regression Fundamentals
### *From Data to Decision Boundaries*

**The British College Nepal · 2026–27**  
**Awarding:** UWE Bristol · Level 6 · **Module:** `UFCFAS-15-2`  
**Lecturer:** Sudan Pudasaini  
**UWE Module Leader:** Prof. Jun Hong  

---

# 👋 Welcome to Machine Learning!

### Quick show of hands in the room:

* Who feels confident writing functions and data scripts in **Python**?
* Who has used **NumPy, Pandas, or Matplotlib** before?
* Who has experimented with **Scikit-Learn, PyTorch, or TensorFlow**?
* Who uses **GitHub Copilot, ChatGPT, or Claude** to write or debug code?

> *"Machine learning isn't magic, and it isn't just dry mathematical proofs. It is empirical software engineering: designing models that learn from data, and knowing how to evaluate them honestly."*

---

# 🧭 The 3 Core Principles of This Module

| Principle | What It Means | Why It Matters |
|---|---|---|
| **1. Grounded Intuition** | Understand *why* an algorithm works before touching the library | Eliminates black-box guessing |
| **2. Production Craft** | Write clean, vectorized, reproducible Python code with Scikit-Learn | Prepares you for real ML engineering roles |
| **3. Critical Evaluation** | Probe models for overfitting, leakage, bias, and edge-case failure | Models that look good on paper often fail in production |

---

# 🗺️ 12-Week Roadmap: Where We Are Going

* **Weeks 1–3: The Core Foundations**
  - Week 1: Linear Regression & Gradient Descent
  - Week 2: Logistic Regression & Classification Boundaries
  - Week 3: End-to-End ML Workflow, Feature Engineering & Ethics
* **Weeks 4–7: Classical & Ensemble Mastery**
  - Weeks 4–5: Support Vector Machines (SVM) & Kernels
  - Weeks 6–7: Decision Trees, Random Forests & Boosting (AdaBoost)
* **Weeks 8–12: Deep Learning & Applications**
  - Week 8: Artificial Neural Networks (ANN) & Backpropagation
  - Week 9: Convolutional Neural Networks (CNN) & Computer Vision
  - Weeks 10–12: Project Implementation, Tuning & Defense

---

# 📊 Assessment Structure & Deadlines

```
┌─────────────────────────────────────────────────────────────┐
│ 1. Group Project Proposal (10%)        Due: Week 7 (Lab)    │
│    Problem definition, dataset choice, baseline plan        │
├─────────────────────────────────────────────────────────────┤
│ 2. Individual Assignment (30%)         Due: Week 9          │
│    Compare 2 distinct ML algorithms on the same dataset     │
│    Data preparation, training, hyperparameter tuning, report│
├─────────────────────────────────────────────────────────────┤
│ 3. Group Project & Presentation (60%)  Due: Week 12         │
│    End-to-end Deep Learning system (CNN / DNN application)  │
│    Working code repository + group presentation & report    │
└─────────────────────────────────────────────────────────────┘
```

> **Accountability Note:** Git commit history in your repository is primary evidence of individual contribution. **No commits = No contribution record.**

---

# 🚀 The Modernized Delivery Stack (`neo_ML`)

To save you from "it works on my machine" and package version nightmares:

* 🐳 **Dockerized Environment:**  
  Run JupyterLab with Python 3.12, scikit-learn, and all dependencies locked in.
  ```bash
  docker pull ghcr.io/lbu-courses/ml-course:week1
  docker run -p 8888:8888 -v $(pwd):/workspace ghcr.io/lbu-courses/ml-course:week1
  ```
* 🐙 **GitHub Classroom Submissions:**  
  Automatic checks on every push verify that code executed and outputs are present.
* 🤖 **AI-Assisted Learning (Copilot / Gemini):**  
  Permitted for scaffolding & syntax exploration; paired with weekly **`REFLECTION.md`** logs.

---

# 🧠 What is Machine Learning?

Traditional Programming vs. Machine Learning:

### ⚙️ Traditional Programming
$$\text{Data} + \text{Rules (Code)} \xrightarrow{\quad} \text{Answers}$$
*You manually write every `if/else` condition and logic gate.*

### 🤖 Machine Learning
$$\text{Data} + \text{Answers (Labels)} \xrightarrow{\quad} \text{Rules (Model)}$$
*The computer optimizes internal parameters to discover the underlying mapping.*

---

# 🏷️ The Machine Learning Taxonomy

```
                          Machine Learning
            ┌───────────────────┼───────────────────┐
            │                   │                   │
    Supervised Learning   Unsupervised        Reinforcement
   (Data has labels y)   (No labels, patterns) (Reward/Penalty)
      ┌─────┴─────┐             │
      │           │             ├── Clustering (K-Means)
  Regression  Classification    └── Dimensionality Reduction (PCA)
 (Continuous)  (Discrete)
   e.g. Price   e.g. Spam/Ham
```

* **Today's focus:** Supervised Learning $\rightarrow$ **Linear Regression**.

---

# 🎯 The Supervised Learning Problem Setup

Let's define our mathematical notation:

* **Training Set:** A collection of $m$ examples: $\{(x^{(1)}, y^{(1)}), (x^{(2)}, y^{(2)}), \dots, (x^{(m)}, y^{(m)})\}$
* **$x^{(i)}$:** Input feature vector for the $i$-th training example.
* **$y^{(i)}$:** Target output (ground truth label) for the $i$-th training example.
* **$n$:** Total number of input features.
* **Hypothesis $h_\theta(x)$:** The predictor function mapping input $x$ to predicted output $\hat{y}$.

$$\hat{y} = h_\theta(x)$$

---

# 📈 Linear Regression: The Hypothesis Function

For a single feature $x_1$ (e.g., House Size $\rightarrow$ Price):
$$h_\theta(x) = \theta_0 + \theta_1 x_1$$
* $\theta_0$: Bias (intercept)
* $\theta_1$: Weight (slope)

### Generalizing to $n$ Features:
$$h_\theta(x) = \theta_0 + \theta_1 x_1 + \theta_2 x_2 + \dots + \theta_n x_n$$

With dummy feature $x_0 = 1$, we express this compactly using linear algebra:
$$h_\theta(x) = \sum_{j=0}^n \theta_j x_j = \theta^T x = X\theta$$

---

# 📉 Measuring Error: The Cost Function $J(\theta)$

How do we decide if a line is a "good fit"? We measure prediction errors!

For each example $i$, error is $(h_\theta(x^{(i)}) - y^{(i)})$.  
We square the errors (penalizes large misses heavily, removes negative signs) and average them:

### Mean Squared Error (MSE) Cost Function:
$$J(\theta) = \frac{1}{2m} \sum_{i=1}^m \left(h_\theta(x^{(i)}) - y^{(i)}\right)^2$$

* Why the factor of $\frac{1}{2}$? It cancels out nicely when we take the derivative!
* **Our Goal:** Find parameters $\theta$ that **minimize** $J(\theta)$:
$$\min_\theta J(\theta)$$

---

# 🥣 The Geometry of $J(\theta)$: Why MSE is Special

* For Linear Regression, $J(\theta)$ is a **strictly convex function** (bowl-shaped surface).
* **Crucial Implication:**
  - There are **no local minima** traps!
  - Any local minimum is guaranteed to be the **global minimum**.

```
       J(θ)
        \                   /
         \                 /
          \       *       /   <--- Global Minimum!
           \____/   \____/
             θ0, θ1
```

How do we navigate this bowl to reach the lowest point? $\rightarrow$ **Gradient Descent!**

---

# 🧗 Optimization: Gradient Descent Intuition

Imagine standing on a foggy mountainside where you can only see a few feet ahead:

1. Look in every direction around your feet to find the **steepest downhill slope**.
2. Take a step in that downhill direction.
3. Repeat until the ground beneath you is flat!

### The Mathematical Formula:
$$\theta_j := \theta_j - \alpha \frac{\partial}{\partial \theta_j} J(\theta) \quad (\text{simultaneously for all } j)$$

* $\frac{\partial}{\partial \theta_j} J(\theta)$: The gradient (direction of steepest *ascent*). The minus sign steps *downward*.
* $\alpha$ (Alpha): The **learning rate** (step size).

---

# ⚙️ The Learning Rate $\alpha$: Getting the Step Right

The learning rate is a critical **hyperparameter**:

```
        Too Small (α = 0.0001)           Too Large (α = 1.5)
         Slow convergence                 Overshoots & Diverges
        \                   /            \        /     \
         \ . . . . . . . . /              \  /\  /       \
          \_______________/                \/  \/         \
```

* **If $\alpha$ is too small:** Takes thousands of iterations; painfully slow.
* **If $\alpha$ is too large:** Can overshoot the minimum, oscillate wildly, or completely diverge to infinity.
* **Rule of thumb:** Try logarithmically spaced values: $0.001, 0.01, 0.1$.

---

# 🧮 Calculating the Gradient for Linear Regression

Let's compute the partial derivative $\frac{\partial}{\partial \theta_j} J(\theta)$:

$$\frac{\partial}{\partial \theta_j} J(\theta) = \frac{1}{m} \sum_{i=1}^m \left(h_\theta(x^{(i)}) - y^{(i)}\right) x_j^{(i)}$$

### The Complete Batch Gradient Descent Update Rule:

For $j = 0$ (intercept, since $x_0 = 1$):
$$\theta_0 := \theta_0 - \alpha \frac{1}{m} \sum_{i=1}^m \left(h_\theta(x^{(i)}) - y^{(i)}\right)$$

For $j = 1, 2, \dots, n$:
$$\theta_j := \theta_j - \alpha \frac{1}{m} \sum_{i=1}^m \left(h_\theta(x^{(i)}) - y^{(i)}\right) x_j^{(i)}$$

---

# 🔄 Gradient Descent Flavors

| Method | Data per Step | Pros | Cons |
|---|---|---|---|
| **Batch GD** | All $m$ samples | Stable, deterministic convergence | Slow on massive datasets |
| **Stochastic GD (SGD)** | 1 random sample | Fast, can jump out of plateaus | Noisy path, fluctuates |
| **Mini-batch GD** | 32–256 samples | Vectorized GPU efficiency, balanced | Need to tune batch size |

> *In today's lab, we implement Batch Gradient Descent from scratch to understand every step, then compare it with Scikit-Learn!*

---

# 💻 Python Implementation: From Scratch with NumPy

```python
import numpy as np

def gradient_descent(X, y, alpha=0.01, iterations=1000):
    m = len(y)
    # Add x0 = 1 bias column
    X_b = np.c_[np.ones((m, 1)), X]
    theta = np.zeros((X_b.shape[1], 1))
    cost_history = []
    
    for _ in range(iterations):
        gradients = (1 / m) * X_b.T.dot(X_b.dot(theta) - y)
        theta = theta - alpha * gradients
        cost = (1 / (2 * m)) * np.sum((X_b.dot(theta) - y) ** 2)
        cost_history.append(cost)
        
    return theta, cost_history
```

* Notice how matrix dot products replace slow Python `for` loops!

---

# 📦 The Production Standard: `scikit-learn`

In real production systems, we use optimized libraries:

```python
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# 1. Instantiate the model
model = LinearRegression()

# 2. Fit to training data
model.fit(X_train, y_train)

# 3. Predict & evaluate
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Weights: {model.coef_}, Intercept: {model.intercept_}")
print(f"MSE: {mse:.4f} | R² Score: {r2:.4f}")
```

---

# 🧪 Today's Lab Roadmap

Open your Jupyter environment and complete the following sequence:

1. **Setup & Verification:**
   - Launch your environment via Docker (`localhost:8888`) or VS Code.
2. **`intro-to-libraries.ipynb`:**
   - Quick refresher on NumPy broadcasting, Pandas DataFrame manipulation, and Matplotlib plotting.
3. **`linear-regression-sklearn-gradient-descent.ipynb`:**
   - Load dataset $\rightarrow$ inspect scatter plots.
   - Implement Gradient Descent manually and plot the cost reduction curve.
   - Fit `sklearn.linear_model.LinearRegression` and compare weights $\theta$.
4. **Push Work:**
   - Commit your executed notebook and initial `SETUP.md` to GitHub.

---

# 🤖 AI Coding Guidance for This Week

* ✅ **Do this:**
  - Ask Copilot: *"How do I reshape this NumPy array for scikit-learn?"*
  - Prompt Gemini: *"Explain why the MSE loss curve flattens out after 300 epochs."*
* ❌ **Don't do this:**
  - Copying full notebook solutions from generative AI without reading them.
  - Submitting unexecuted cells (the automated checker will fail your push).
* 📝 **Weekly Reflection Requirement:**
  - Add your 5-line `REFLECTION.md` describing 1 AI prompt you tested and what you learned.

---

# 🏁 Summary & Week 1 Takeaways

* **Supervised Learning:** Learning a mapping $h_\theta(x)$ from features $X$ to targets $y$.
* **Linear Regression:** Modeling predictions as linear combinations $h_\theta(x) = X\theta$.
* **MSE Cost Function $J(\theta)$:** A convex bowl measuring mean squared prediction error.
* **Gradient Descent:** Iteratively updating parameters in the opposite direction of the gradient: $\theta := \theta - \alpha \nabla J(\theta)$.
* **Next Week:** What happens when $y$ is categorical (0 or 1)?  
  $\rightarrow$ **Logistic Regression & Decision Boundaries!**

---

# ❓ Questions & Lab Time

### Grab your laptops, fire up Docker, and let's start coding!

* **Office Hours:** Sudan Pudasaini (TBC Faculty Office)
* **GitHub Classroom Link:** Distributed in today's class channel
* **Docker Image:** `ghcr.io/lbu-courses/ml-course:week1`
* **JupyterLab:** `http://localhost:8888`

Let's build models that actually learn! 🚀
