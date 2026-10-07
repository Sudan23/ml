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
| Docker base image | [docker/Dockerfile](docker/Dockerfile) |
| GitHub Actions checker | [github-actions/notebook-checker.yml](github-actions/notebook-checker.yml) |

---

## 🐳 Docker Image Convention

```bash
# Pull weekly image (Python + Jupyter + ML libraries)
docker pull ghcr.io/lbu-courses/ml-course:week<N>

# Run with mounted workspace
docker run -it -p 8888:8888 -v $(pwd):/workspace ghcr.io/lbu-courses/ml-course:week<N>

# Open in browser: http://localhost:8888
```
