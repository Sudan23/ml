# 🐳 Quickstart: Containerized Machine Learning (Week 1 · Day 2)

This folder contains the complete, self-contained starter project for **Week 1 · Day 2: Hands-On Containerized Machine Learning**.

---

## 🚀 Quick Commands

### 1. Build the Docker Image
```bash
docker build -t my-first-ml:v1 .
```

### 2. Run the Container
```bash
docker run --rm my-first-ml:v1
```

### 3. Run with Volume Mount to Save the Trained Model Locally
```bash
mkdir -p output
docker run --rm -v $(pwd)/output:/app/output my-first-ml:v1
```
Check that `output/model.joblib` is saved on your laptop.

### 4. Tag & Push to Docker Hub
```bash
docker login
docker tag my-first-ml:v1 <YOUR_DOCKERHUB_USERNAME>/my-first-ml:v1
docker push <YOUR_DOCKERHUB_USERNAME>/my-first-ml:v1
```

### 5. Pull the Lecturer's Official Course Toolkit
```bash
docker pull alkimi/ml:week1
docker run -p 8888:8888 -v $(pwd):/home/student/notebooks/mywork alkimi/ml:week1
```
Open **[http://localhost:8888](http://localhost:8888)** in your browser!
