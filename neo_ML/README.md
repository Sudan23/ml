# 🤖 neo_ML — Modern Delivery: Machine Learning
**The British College Nepal · Sudan Pudasaini · 2026–27**
**Awarding: UWE Bristol · Level 6 · Module: UFCFAS-15-2**

> Original university slides and notebooks remain in:
> `../uni_ML/` ← **do not modify**
> This folder contains everything we add on top of the official delivery.

---

## 📁 Folder Structure

```
neo_ML/
├── README.md                        ← You are here
│
├── onboarding/
│   └── onboarding.md                ← Student Week 0 setup guide (TBC-specific)
│
├── delivery-plan/
│   └── ML-delivery-plan.md          ← Aligned delivery plan with modern extras
│
├── docker/
│   ├── Dockerfile                   ← Base image (Python 3.11, Jupyter, sklearn, etc.)
│   └── week-images/                 ← Per-week images with starter notebooks
│       ├── week1/
│       ├── week2/
│       └── ...
│
└── github-actions/
    └── notebook-checker.yml         ← Runs notebooks on student push, checks outputs
```

---

## 🔗 Quick Links

| Document | Path |
|---|---|
| Student onboarding | [onboarding/onboarding.md](onboarding/onboarding.md) |
| Delivery plan | [delivery-plan/ML-delivery-plan.md](delivery-plan/ML-delivery-plan.md) |
| Class 1 Slides (Marp) | [slides/week1/slides.md](slides/week1/slides.md) |
| Class 1 Slides (HTML) | [slides/week1/slides.html](slides/week1/slides.html) |
| Class 1 Slides (PPTX) | [slides/week1/Week_1_Class_1_Course_Introduction_and_Overview.pptx](slides/week1/Week_1_Class_1_Course_Introduction_and_Overview.pptx) |
| Docker base image | [docker/Dockerfile](docker/Dockerfile) |
| GitHub Actions checker | [github-actions/notebook-checker.yml](github-actions/notebook-checker.yml) |

---

## 🐳 Docker Image Convention

```bash
# Pull weekly image (Python + Jupyter + ML libraries)
docker pull ghcr.io/sudan23/ml:week<N>

# Run with mounted workspace
docker run -it -p 8888:8888 -v $(pwd):/workspace ghcr.io/sudan23/ml:week<N>

# Open in browser: http://localhost:8888
```
