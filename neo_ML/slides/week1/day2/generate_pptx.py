"""
UFCFAS-15-2 Machine Learning — Week 1 Day 2 Presentation Deck Generator
Topic: Hands-On Containerized ML: Build, Train, Push & Pull with Docker
Lecturer: Sudan Pudasaini · The British College Nepal
Outputs: Week_1_Class_2_HandsOn_Docker_ML.pptx (16:9 Widescreen)
"""

import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

def create_deck():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)

    # Palette
    C_BG = RGBColor(10, 14, 23)        # #0A0E17
    C_CARD = RGBColor(17, 24, 39)      # #111827
    C_CARD_BORDER = RGBColor(30, 41, 59) # #1E293B
    C_BLUE = RGBColor(56, 189, 248)    # #38BDF8
    C_CYAN = RGBColor(6, 182, 212)     # #06B6D4
    C_EMERALD = RGBColor(16, 185, 129) # #10B981
    C_AMBER = RGBColor(245, 158, 11)   # #F59E0B
    C_WHITE = RGBColor(255, 255, 255)
    C_MUTED = RGBColor(148, 163, 184)  # #94A3B8
    C_CODE_BG = RGBColor(3, 7, 18)     # #030712
    C_CODE_TXT = RGBColor(126, 231, 135) # #7EE787

    def set_bg(slide):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), prs.slide_width, prs.slide_height)
        bg.fill.solid()
        bg.fill.fore_color.rgb = C_BG
        bg.line.fill.background()
        return bg

    def add_header(slide, tag_text, title_text, subtitle_text=""):
        tb = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.7), Inches(1.3))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0

        p0 = tf.paragraphs[0]
        p0.text = tag_text.upper()
        p0.font.size = Pt(11)
        p0.font.bold = True
        p0.font.color.rgb = C_CYAN

        p1 = tf.add_paragraph()
        p1.text = title_text
        p1.font.size = Pt(26)
        p1.font.bold = True
        p1.font.color.rgb = C_WHITE
        p1.space_before = Pt(4)

        if subtitle_text:
            p2 = tf.add_paragraph()
            p2.text = subtitle_text
            p2.font.size = Pt(13)
            p2.font.color.rgb = C_MUTED
            p2.space_before = Pt(3)

    def add_card(slide, left, top, width, height, title, items, tag=""):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = C_CARD
        card.line.color.rgb = C_CARD_BORDER
        card.line.width = Pt(1)

        tb = slide.shapes.add_textbox(left + Inches(0.25), top + Inches(0.2), width - Inches(0.5), height - Inches(0.4))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0

        p_idx = 0
        if tag:
            p = tf.paragraphs[0]
            p.text = tag.upper()
            p.font.size = Pt(10)
            p.font.bold = True
            p.font.color.rgb = C_BLUE
            p_idx += 1

        if p_idx == 0:
            p_title = tf.paragraphs[0]
        else:
            p_title = tf.add_paragraph()
        p_title.text = title
        p_title.font.size = Pt(15)
        p_title.font.bold = True
        p_title.font.color.rgb = C_WHITE
        p_title.space_before = Pt(3)

        for item in items:
            p = tf.add_paragraph()
            p.text = f"• {item}"
            p.font.size = Pt(12)
            p.font.color.rgb = C_MUTED
            p.space_before = Pt(4)

    def add_code_card(slide, left, top, width, height, title, code_lines):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = C_CODE_BG
        card.line.color.rgb = C_CARD_BORDER
        card.line.width = Pt(1)

        tb = slide.shapes.add_textbox(left + Inches(0.25), top + Inches(0.2), width - Inches(0.5), height - Inches(0.4))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0

        p0 = tf.paragraphs[0]
        p0.text = title
        p0.font.size = Pt(13)
        p0.font.bold = True
        p0.font.color.rgb = C_BLUE

        for line in code_lines:
            p = tf.add_paragraph()
            p.text = line
            p.font.size = Pt(11)
            p.font.color.rgb = C_CODE_TXT
            p.font.name = "Courier New"
            p.space_before = Pt(2)

    blank_layout = prs.slide_layouts[6]

    # -------------------------------------------------------------
    # SLIDE 1: Title
    # -------------------------------------------------------------
    s1 = prs.slides.add_slide(blank_layout)
    set_bg(s1)

    tb = s1.shapes.add_textbox(Inches(1.0), Inches(1.2), Inches(11.3), Inches(2.2))
    tf = tb.text_frame
    tf.word_wrap = True

    p = tf.paragraphs[0]
    p.text = "THE BRITISH COLLEGE NEPAL · UWE BRISTOL"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = C_CYAN

    p = tf.add_paragraph()
    p.text = "Hands-On Containerized ML"
    p.font.size = Pt(40)
    p.font.bold = True
    p.font.color.rgb = C_WHITE
    p.space_before = Pt(8)

    p = tf.add_paragraph()
    p.text = "Build, Train, Push & Pull with Docker · Class 2 of 3"
    p.font.size = Pt(20)
    p.font.color.rgb = C_BLUE
    p.space_before = Pt(6)

    # 3 info cards
    add_card(s1, Inches(1.0), Inches(3.8), Inches(3.5), Inches(2.2),
             "1.5-Hour Workshop",
             ["Light, interactive & confidence-building.", "Every student authors their own container.", "Zero bare OS installation headaches."],
             "Session Type")

    add_card(s1, Inches(4.9), Inches(3.8), Inches(3.5), Inches(2.2),
             "Real ML Pipeline",
             ["Dataset: Study hours vs exam score.", "Algorithm: Scikit-Learn Linear Regression.", "Output: Exportable model.joblib artifact."],
             "Practical Focus")

    add_card(s1, Inches(8.8), Inches(3.8), Inches(3.5), Inches(2.2),
             "Cloud Registry",
             ["Publish custom image to personal Docker Hub.", "Pull lecturer's official alkimi/ml:week1.", "Launch JupyterLab for Class 3 readiness."],
             "Deliverable")

    tb_foot = s1.shapes.add_textbox(Inches(1.0), Inches(6.4), Inches(11.3), Inches(0.6))
    tf_f = tb_foot.text_frame
    p = tf_f.paragraphs[0]
    p.text = "Lecturer: Sudan Pudasaini · Module: UFCFAS-15-2 Machine Learning (Level 5 · 15 Credits)"
    p.font.size = Pt(12)
    p.font.color.rgb = C_MUTED
    s1.notes_slide.notes_text_frame.text = "Welcome class! Today is Day 2. We keep it light, practical, and fun. Every student will build, train, push, and pull a container today."

    # -------------------------------------------------------------
    # SLIDE 2: 90-Minute Flight Plan
    # -------------------------------------------------------------
    s2 = prs.slides.add_slide(blank_layout)
    set_bg(s2)
    add_header(s2, "Session Roadmap", "Today's 90-Minute Flight Plan", "Five structured milestones designed to get everyone cloud-ready.")

    steps = [
        ("Part 1 · 15m", "Why Docker for ML?", ["ML reproducibility crisis.", "Smoke test: docker run hello-world."]),
        ("Part 2 · 20m", "Micro ML App", ["data.csv + train_and_predict.py.", "Authoring the Dockerfile."]),
        ("Part 3 · 15m", "Local Execution", ["docker build & docker run.", "Volume mount: persist model.joblib."]),
        ("Part 4 · 20m", "Docker Hub Push", ["Tag with <user>/my-first-ml:v1.", "docker push to public cloud registry."]),
        ("Part 5 · 20m", "Course Toolkit", ["Pull alkimi/ml:week1 from Docker Hub.", "Launch JupyterLab on localhost:8888."])
    ]
    for i, (tag, title, items) in enumerate(steps):
        add_card(s2, Inches(0.8 + i * 2.4), Inches(2.0), Inches(2.25), Inches(4.5), title, items, tag)
    s2.notes_slide.notes_text_frame.text = "Walk through the 5 stages. Reassure students that today is interactive and we will make sure no one is left behind."

    # -------------------------------------------------------------
    # SLIDE 3: The Crisis
    # -------------------------------------------------------------
    s3 = prs.slides.add_slide(blank_layout)
    set_bg(s3)
    add_header(s3, "Motivation", "The 'Works on My Machine' Crisis in Machine Learning", "Why professional data scientists never run models on bare operating systems.")

    add_card(s3, Inches(0.8), Inches(2.0), Inches(5.6), Inches(4.8),
             "Bare Operating System Hazards",
             [
                 "Python Version Drift: Student A has 3.10, Student B has 3.12.",
                 "Dependency Hell: NumPy 2.x breaking legacy Scikit-Learn code.",
                 "C-Extension Failures: BLAS/LAPACK compilation fails on M-series Mac or Windows.",
                 "Environment Pollution: Installing one package breaks another project.",
                 "Cloud Failure: 'It works on my MacBook' but crashes when deployed to AWS."
             ],
             "The Problem")

    add_card(s3, Inches(6.8), Inches(2.0), Inches(5.6), Inches(4.8),
             "Containerized Machine Learning",
             [
                 "Immutable Environment: Python version is locked inside the container.",
                 "Frozen Dependencies: requirements.txt is baked into isolated Linux layers.",
                 "Zero Compilation Hassles: Pre-compiled binary Linux wheels inside Debian/Ubuntu.",
                 "Clean Host System: Your laptop stays completely untouched and pristine.",
                 "Build Once, Run Anywhere: Same container runs on laptop, server, or cloud cluster."
             ],
             "The Solution")
    s3.notes_slide.notes_text_frame.text = "Ask the class: Who has wasted hours trying to install Python packages? Docker solves this forever."

    # -------------------------------------------------------------
    # SLIDE 4: Data & Problem
    # -------------------------------------------------------------
    s4 = prs.slides.add_slide(blank_layout)
    set_bg(s4)
    add_header(s4, "Problem Formulation", "Our Micro ML Task: Study Hours vs Exam Score", "A clear, intuitive linear relationship to demonstrate containerization.")

    add_code_card(s4, Inches(0.8), Inches(2.0), Inches(4.5), Inches(4.8),
                  "Dataset: data.csv",
                  [
                      "study_hours,exam_score",
                      "1.5,42.0",
                      "2.0,50.0",
                      "2.5,53.5",
                      "3.0,58.0",
                      "3.5,62.0",
                      "4.0,66.5",
                      "5.0,74.5",
                      "6.0,81.5",
                      "7.0,89.0",
                      "8.0,95.0",
                      "9.0,98.5"
                  ])

    add_card(s4, Inches(5.7), Inches(2.0), Inches(6.8), Inches(4.8),
             "Linear Regression Concept",
             [
                 "Feature (X): Study Hours per week (Input variable).",
                 "Target (y): Exam Score from 0 to 100 (Continuous output).",
                 "Equation of Line: y = w · X + b",
                 "w (Weight / Slope): Exam points gained for each additional hour studied.",
                 "b (Bias / Intercept): Base baseline exam score with zero study hours.",
                 "Algorithm Goal: Find the best w and b minimizing prediction error!"
             ],
             "Mathematical Formulation")
    s4.notes_slide.notes_text_frame.text = "Introduce the data simply: study hours vs exam scores. The goal is to fit y = wx + b."

    # -------------------------------------------------------------
    # SLIDE 5: Python ML Script
    # -------------------------------------------------------------
    s5 = prs.slides.add_slide(blank_layout)
    set_bg(s5)
    add_header(s5, "Application Code", "The ML Script: train_and_predict.py", "Loading data, fitting the model with Scikit-Learn, and saving artifacts.")

    add_code_card(s5, Inches(0.8), Inches(2.0), Inches(11.7), Inches(4.8),
                  "train_and_predict.py",
                  [
                      "import pandas as pd",
                      "from sklearn.linear_model import LinearRegression",
                      "from sklearn.metrics import mean_squared_error, r2_score",
                      "import joblib",
                      "",
                      "# 1. Load dataset & prepare feature matrix X and target vector y",
                      "df = pd.read_csv('data.csv')",
                      "X, y = df[['study_hours']].values, df['exam_score'].values",
                      "",
                      "# 2. Initialize and fit Scikit-Learn Linear Regression model",
                      "model = LinearRegression().fit(X, y)",
                      "print(f'Learned: Exam Score = ({model.coef_[0]:.2f} × Hours) + {model.intercept_:.2f}')",
                      "",
                      "# 3. Run sample prediction for 6.0 study hours",
                      "pred = model.predict([[6.0]])[0]",
                      "print(f'Predicted score for 6.0 hours: {pred:.1f} / 100')",
                      "",
                      "# 4. Persist trained model artifact to output folder",
                      "joblib.dump(model, 'output/model.joblib')"
                  ])
    s5.notes_slide.notes_text_frame.text = "Walk through the code. Show how Scikit-Learn makes fitting and predicting concise. Emphasize saving the model to output/."

    # -------------------------------------------------------------
    # SLIDE 6: Dockerfile Anatomy
    # -------------------------------------------------------------
    s6 = prs.slides.add_slide(blank_layout)
    set_bg(s6)
    add_header(s6, "Container Specification", "Authoring the Dockerfile", "Packaging Python, dependencies, code, and data into reproducible layers.")

    add_code_card(s6, Inches(0.8), Inches(2.0), Inches(6.0), Inches(4.8),
                  "Dockerfile",
                  [
                      "# 1. Minimal official Python runtime",
                      "FROM python:3.11-slim",
                      "",
                      "# 2. Set work directory inside container",
                      "WORKDIR /app",
                      "",
                      "# 3. Install requirements with layer caching",
                      "COPY requirements.txt .",
                      "RUN pip install --no-cache-dir -r requirements.txt",
                      "",
                      "# 4. Copy training data and Python script",
                      "COPY data.csv .",
                      "COPY train_and_predict.py .",
                      "",
                      "# 5. Create artifact output directory",
                      "RUN mkdir -p /app/output",
                      "",
                      "# 6. Default execution entrypoint",
                      "CMD [\"python\", \"train_and_predict.py\"]"
                  ])

    add_card(s6, Inches(7.2), Inches(2.0), Inches(5.3), Inches(4.8),
             "Layer-by-Layer Breakdown",
             [
                 "FROM python:3.11-slim: Ultra-lightweight Debian base (~50MB).",
                 "WORKDIR /app: Sets context so all relative paths resolve to /app.",
                 "COPY requirements.txt: Copies dependency list first.",
                 "RUN pip install: Caches downloaded libraries in a reusable layer.",
                 "COPY data.csv & script: Adds code layers on top of dependencies.",
                 "CMD [\"python\", ...]: Tells container what to run on startup."
             ],
             "Docker Directives")
    s6.notes_slide.notes_text_frame.text = "Explain the 6 directives. Emphasize why requirements.txt is copied before code (Docker layer caching)."

    # -------------------------------------------------------------
    # SLIDE 7: Build & Run Locally
    # -------------------------------------------------------------
    s7 = prs.slides.add_slide(blank_layout)
    set_bg(s7)
    add_header(s7, "Hands-On Tasks 1 & 2", "Building & Executing Your ML Container", "Running the complete training lifecycle inside an isolated container.")

    add_code_card(s7, Inches(0.8), Inches(2.0), Inches(5.6), Inches(4.8),
                  "Step 1: Build Image",
                  [
                      "# Ensure you are in ~/ml-labs/week1/docker-ml",
                      "docker build -t my-first-ml:v1 .",
                      "",
                      "# ⚠️ Note: Do not forget the trailing dot '.'",
                      "# It specifies current directory as build context.",
                      "",
                      "# Verify image creation:",
                      "docker images",
                      "# You should see my-first-ml:v1 in the list!"
                  ])

    add_code_card(s7, Inches(6.8), Inches(2.0), Inches(5.6), Inches(4.8),
                  "Step 2: Run Container",
                  [
                      "# Execute training inside container:",
                      "docker run --rm my-first-ml:v1",
                      "",
                      "# Expected Output:",
                      "# ========================================",
                      "# 🚀 Training Linear Regression model...",
                      "# Learned: Score = (7.50 × Hours) + 35.00",
                      "# R² Score: 0.9850 (98.5%)",
                      "# Studying 6.0 hrs ➡️ Predicted: 80.0 / 100",
                      "# Model saved to: 'output/model.joblib'",
                      "# ========================================"
                  ])
    s7.notes_slide.notes_text_frame.text = "Give students 10 minutes to run build and run. Walk around to check that everyone sees the training output."

    # -------------------------------------------------------------
    # SLIDE 8: Volume Mounting & Model Persistence
    # -------------------------------------------------------------
    s8 = prs.slides.add_slide(blank_layout)
    set_bg(s8)
    add_header(s8, "Hands-On Task 3", "Model Persistence: Volume Mounting", "Extracting the trained model artifact (model.joblib) onto your host laptop.")

    add_card(s8, Inches(0.8), Inches(2.0), Inches(5.6), Inches(4.8),
             "The Stateless Container Problem",
             [
                 "Containers are temporary execution sandboxes.",
                 "When a container terminates, its internal files disappear.",
                 "If your ML pipeline trains a model for 10 hours, where does the model go?",
                 "Solution: Volume Mount (-v).",
                 "A volume mounts a folder from your laptop filesystem directly into /app/output inside the container!"
             ],
             "Why Volumes Matter")

    add_code_card(s8, Inches(6.8), Inches(2.0), Inches(5.6), Inches(4.8),
                  "Volume Mounting Command",
                  [
                      "# 1. Create local output directory on your laptop",
                      "mkdir -p output",
                      "",
                      "# 2. Mount local output into /app/output",
                      "docker run --rm \\",
                      "  -v $(pwd)/output:/app/output \\",
                      "  my-first-ml:v1",
                      "",
                      "# 3. Verify artifact saved locally on host:",
                      "ls -la output/",
                      "# Output: model.joblib is right on your laptop!"
                  ])
    s8.notes_slide.notes_text_frame.text = "Explain the magic of volume mounts: bridging the container's output directly to the host filesystem."

    # -------------------------------------------------------------
    # SLIDE 9: Docker Hub Push
    # -------------------------------------------------------------
    s9 = prs.slides.add_slide(blank_layout)
    set_bg(s9)
    add_header(s9, "Hands-On Task 4", "Publishing to Docker Hub", "Sharing your custom ML container with the global developer cloud.")

    add_code_card(s9, Inches(0.8), Inches(2.0), Inches(3.7), Inches(4.8),
                  "1. Authenticate",
                  [
                      "# Login from terminal:",
                      "docker login",
                      "",
                      "# Enter username & token",
                      "# Login Succeeded!"
                  ])

    add_code_card(s9, Inches(4.8), Inches(2.0), Inches(3.7), Inches(4.8),
                  "2. Tag Image",
                  [
                      "# Format: <user>/<repo>:<tag>",
                      "docker tag my-first-ml:v1 \\",
                      "  <YOUR_USER>/my-first-ml:v1",
                      "",
                      "# Example:",
                      "# docker tag my-first-ml:v1 \\",
                      "#   studentjohn/my-first-ml:v1"
                  ])

    add_code_card(s9, Inches(8.8), Inches(2.0), Inches(3.7), Inches(4.8),
                  "3. Push to Cloud",
                  [
                      "# Push to public registry:",
                      "docker push \\",
                      "  <YOUR_USER>/my-first-ml:v1",
                      "",
                      "# Check live at:",
                      "# hub.docker.com/r/<user>/..."
                  ])
    s9.notes_slide.notes_text_frame.text = "Celebrate this moment! Every student has now published a real containerized ML service to the cloud."

    # -------------------------------------------------------------
    # SLIDE 10: Course Toolkit
    # -------------------------------------------------------------
    s10 = prs.slides.add_slide(blank_layout)
    set_bg(s10)
    add_header(s10, "Hands-On Task 5", "Pull Lecturer's Official Course Toolkit", "Downloading alkimi/ml:week1 for UFCFAS-15-2 coursework and labs.")

    add_code_card(s10, Inches(0.8), Inches(2.0), Inches(11.7), Inches(2.2),
                  "Pull the Official Image from Docker Hub",
                  [
                      "# Pull pre-built course toolkit (Python 3.12, JupyterLab 4, Scikit-Learn, Pandas, NumPy, Seaborn):",
                      "docker pull alkimi/ml:week1"
                  ])

    add_code_card(s10, Inches(0.8), Inches(4.5), Inches(11.7), Inches(2.3),
                  "Launch JupyterLab with Port Forwarding",
                  [
                      "# Run container exposing port 8888 and mounting your local notebooks workspace:",
                      "docker run -p 8888:8888 -v $(pwd):/home/student/notebooks/mywork alkimi/ml:week1",
                      "",
                      "# Open in browser: http://localhost:8888"
                  ])
    s10.notes_slide.notes_text_frame.text = "Have everyone pull alkimi/ml:week1. Show that when they open localhost:8888, JupyterLab is running instantly."

    # -------------------------------------------------------------
    # SLIDE 11: Verification Checklist
    # -------------------------------------------------------------
    s11 = prs.slides.add_slide(blank_layout)
    set_bg(s11)
    add_header(s11, "Accountability", "Class 2 Exit Checklist", "Verify your deliverables before dismissing today's workshop.")

    add_card(s11, Inches(0.8), Inches(2.0), Inches(5.6), Inches(4.8),
             "Today's Completed Checklist",
             [
                 "[ ] Docker Desktop smoke test passed (hello-world).",
                 "[ ] Custom ML image built locally (my-first-ml:v1).",
                 "[ ] Training script ran & evaluated R² score (~98.5%).",
                 "[ ] Model artifact (model.joblib) saved via volume mount.",
                 "[ ] Tagged and pushed image to your Docker Hub profile.",
                 "[ ] Pulled official course image: alkimi/ml:week1.",
                 "[ ] Verified JupyterLab opens on http://localhost:8888."
             ],
             "Student Checklist")

    add_code_card(s11, Inches(6.8), Inches(2.0), Inches(5.6), Inches(4.8),
                  "Verification File: WEEK1_DAY2_VERIFICATION.md",
                  [
                      "# Commit this file to your Course GitHub Repo:",
                      "",
                      "# Week 1 · Day 2: Docker ML Lab Verification",
                      "**Student Name:** [Your Name]",
                      "**Student ID:** [Your Student ID]",
                      "**Docker Hub URL:** https://hub.docker.com/r/<user>/my-first-ml",
                      "",
                      "## Local Training Proof:",
                      "- Learned Equation: Score = (7.50 × Hours) + 35.00",
                      "- R² Score: 0.9850",
                      "- Saved model.joblib via volume mount",
                      "- alkimi/ml:week1 pulled & JupyterLab verified"
                  ])
    s11.notes_slide.notes_text_frame.text = "Ensure each student commits this verification file to their personal repository under the course organization."

    # -------------------------------------------------------------
    # SLIDE 12: Next Session Preview
    # -------------------------------------------------------------
    s12 = prs.slides.add_slide(blank_layout)
    set_bg(s12)
    add_header(s12, "Tomorrow's Session", "Looking Forward to Class 3 (1 Hour)", "Machine Learning Fundamentals: Linear Regression from Scratch.")

    add_card(s12, Inches(0.8), Inches(2.0), Inches(3.7), Inches(4.5),
             "1. The Math Engine",
             [
                 "What did model.fit() do under the hood?",
                 "Closed-form Ordinary Least Squares (OLS).",
                 "Finding optimal slope w and intercept b."
             ],
             "Theory")

    add_card(s12, Inches(4.8), Inches(2.0), Inches(3.7), Inches(4.5),
             "2. Loss & Error",
             [
                 "Cost Function: Mean Squared Error (MSE).",
                 "Quantifying how far off our line is from the dots.",
                 "Visualizing the error surface bowl."
             ],
             "Loss Function")

    add_card(s12, Inches(8.8), Inches(2.0), Inches(3.7), Inches(4.5),
             "3. Gradient Descent",
             [
                 "Walking down the loss surface bowl.",
                 "Learning rate hyperparameter (alpha).",
                 "Hands-on interactive Jupyter practical."
             ],
             "Optimization")
    s12.notes_slide.notes_text_frame.text = "Tease Class 3. Tomorrow is a 1-hour session diving directly into the mathematics and code of Gradient Descent."

    output_path = "neo_ML/slides/week1/day2/Week_1_Class_2_HandsOn_Docker_ML.pptx"
    prs.save(output_path)
    print(f"Presentation successfully saved to: {output_path}")

if __name__ == "__main__":
    create_deck()
