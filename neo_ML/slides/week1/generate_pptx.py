import collections.abc
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

def create_class1_deck():
    prs = Presentation()
    # 16:9 widescreen
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)

    blank_layout = prs.slide_layouts[6]

    # Theme Colors
    COLOR_BG = RGBColor(15, 23, 42)          # Slate 900
    COLOR_CARD = RGBColor(30, 41, 59)        # Slate 800
    COLOR_CARD_BORDER = RGBColor(51, 65, 85) # Slate 700
    COLOR_CYAN = RGBColor(56, 189, 248)      # Sky 400
    COLOR_INDIGO = RGBColor(129, 140, 248)   # Indigo 400
    COLOR_WHITE = RGBColor(248, 250, 252)    # Slate 50
    COLOR_MUTED = RGBColor(148, 163, 184)    # Slate 400
    COLOR_ACCENT = RGBColor(250, 204, 21)    # Amber 400
    COLOR_EMERALD = RGBColor(52, 211, 153)   # Emerald 400

    def add_bg(slide):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(7.5))
        bg.fill.solid()
        bg.fill.fore_color.rgb = COLOR_BG
        bg.line.fill.background()
        return bg

    def add_header(slide, title_text, category_text="MACHINE LEARNING (UFCFAS-15-2) · WEEK 1 · CLASS 1"):
        cat_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.45), Inches(11.7), Inches(0.35))
        tf_cat = cat_box.text_frame
        tf_cat.word_wrap = True
        p_cat = tf_cat.paragraphs[0]
        p_cat.text = category_text.upper()
        p_cat.font.name = 'Helvetica'
        p_cat.font.size = Pt(11)
        p_cat.font.bold = True
        p_cat.font.color.rgb = COLOR_CYAN

        t_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.75), Inches(11.7), Inches(0.8))
        tf_t = t_box.text_frame
        tf_t.word_wrap = True
        p_t = tf_t.paragraphs[0]
        p_t.text = title_text
        p_t.font.name = 'Helvetica'
        p_t.font.size = Pt(26)
        p_t.font.bold = True
        p_t.font.color.rgb = COLOR_WHITE

        line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.6), Inches(11.733), Inches(0.02))
        line.fill.solid()
        line.fill.fore_color.rgb = COLOR_CARD_BORDER
        line.line.fill.background()

    def add_card(slide, left, top, width, height, title, items, badge=""):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = COLOR_CARD
        card.line.color.rgb = COLOR_CARD_BORDER
        card.line.width = Pt(1.5)

        tf = card.text_frame
        tf.word_wrap = True
        tf.margin_left = Inches(0.28)
        tf.margin_right = Inches(0.28)
        tf.margin_top = Inches(0.28)
        tf.margin_bottom = Inches(0.28)

        if badge:
            p_badge = tf.paragraphs[0]
            p_badge.text = badge.upper()
            p_badge.font.name = 'Helvetica'
            p_badge.font.size = Pt(10)
            p_badge.font.bold = True
            p_badge.font.color.rgb = COLOR_CYAN
            p_title = tf.add_paragraph()
        else:
            p_title = tf.paragraphs[0]

        p_title.text = title
        p_title.font.name = 'Helvetica'
        p_title.font.size = Pt(18)
        p_title.font.bold = True
        p_title.font.color.rgb = COLOR_INDIGO
        p_title.space_after = Pt(10)

        for item in items:
            p_item = tf.add_paragraph()
            p_item.text = f"•  {item}"
            p_item.font.name = 'Helvetica'
            p_item.font.size = Pt(12)
            p_item.font.color.rgb = COLOR_WHITE
            p_item.space_after = Pt(6)

    # ------------------ SLIDE 1: TITLE ------------------
    s1 = prs.slides.add_slide(blank_layout)
    add_bg(s1)

    bar = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.5), Inches(0.15), Inches(4.5))
    bar.fill.solid()
    bar.fill.fore_color.rgb = COLOR_CYAN
    bar.line.fill.background()

    tb1 = s1.shapes.add_textbox(Inches(1.2), Inches(1.5), Inches(11.0), Inches(4.5))
    tf1 = tb1.text_frame
    tf1.word_wrap = True

    p0 = tf1.paragraphs[0]
    p0.text = "THE BRITISH COLLEGE NEPAL · UWE BRISTOL"
    p0.font.name = 'Helvetica'
    p0.font.size = Pt(13)
    p0.font.bold = True
    p0.font.color.rgb = COLOR_CYAN
    p0.space_after = Pt(14)

    p1 = tf1.add_paragraph()
    p1.text = "Machine Learning (UFCFAS-15-2)"
    p1.font.name = 'Helvetica'
    p1.font.size = Pt(42)
    p1.font.bold = True
    p1.font.color.rgb = COLOR_WHITE

    p2 = tf1.add_paragraph()
    p2.text = "Week 1 · Class 1: Course Orientation & Overview"
    p2.font.name = 'Helvetica'
    p2.font.size = Pt(22)
    p2.font.color.rgb = COLOR_INDIGO
    p2.space_after = Pt(24)

    p3 = tf1.add_paragraph()
    p3.text = "Lecturer: Sudan Pudasaini · Module Leader (UWE): Prof. Jun Hong\nWelcome, Expectations, Roadmap & Modern Delivery Architecture"
    p3.font.name = 'Helvetica'
    p3.font.size = Pt(14)
    p3.font.color.rgb = COLOR_MUTED

    # ------------------ SLIDE 2: THE ROOM & ICEBREAKER ------------------
    s2 = prs.slides.add_slide(blank_layout)
    add_bg(s2)
    add_header(s2, "Welcome & Reading the Room")
    add_card(s2, Inches(0.8), Inches(2.0), Inches(5.6), Inches(4.8),
             "Show of Hands & Background",
             [
                 "Who feels confident writing functions and data scripts in Python?",
                 "Who has manipulated data with NumPy, Pandas, or Matplotlib?",
                 "Who has previously trained a model in Scikit-Learn or PyTorch?",
                 "Who uses GitHub Copilot, ChatGPT, or Claude in their daily workflow?",
                 "Our goal: Bridge the gap from novice scripter to ML engineer."
             ],
             "Icebreaker")
    add_card(s2, Inches(6.9), Inches(2.0), Inches(5.6), Inches(4.8),
             "The Level 6 Mindset",
             [
                 "Machine Learning is NOT black-box memorization.",
                 "It is NOT just dry mathematical proofs either.",
                 "It IS empirical software engineering.",
                 "Designing systems that learn from data.",
                 "Knowing how to benchmark and evaluate them honestly."
             ],
             "Philosophy")

    # ------------------ SLIDE 3: PARTNERSHIP & IDENTITY ------------------
    s3 = prs.slides.add_slide(blank_layout)
    add_bg(s3)
    add_header(s3, "Academic Partnership & Module Identity")
    add_card(s3, Inches(0.8), Inches(2.0), Inches(5.6), Inches(4.8),
             "Institution & Award",
             [
                 "Awarding University: UWE Bristol (UK).",
                 "Delivered at: The British College (TBC), Kathmandu, Nepal.",
                 "Module Code: UFCFAS-15-2 (15 UK Credits).",
                 "Level: Level 6 (Final Year Computing).",
                 "All assessments and moderation adhere to UWE Bristol standards."
             ],
             "Partnership")
    add_card(s3, Inches(6.9), Inches(2.0), Inches(5.6), Inches(4.8),
             "Teaching & Module Team",
             [
                 "Local Delivery Lead: Sudan Pudasaini (Lectures, Labs, Mentorship).",
                 "UWE Module Leader: Prof. Jun Hong (Jun.Hong@uwe.ac.uk).",
                 "UWE Module Tutors: Dr. Nathan Duran, Dr. Muhammad Khan.",
                 "Office Hours: Available at TBC Faculty Office & GitHub Discussions.",
                 "Email & Issue Tracking: Dedicated channels for all queries."
             ],
             "Team")

    # ------------------ SLIDE 4: 3-CLASS-PER-WEEK MODEL ------------------
    s4 = prs.slides.add_slide(blank_layout)
    add_bg(s4)
    add_header(s4, "Our 3-Class-Per-Week Delivery Rhythm")
    add_card(s4, Inches(0.8), Inches(2.0), Inches(3.6), Inches(4.8),
             "Class 1 (Today)",
             [
                 "Concept & Orientation.",
                 "Big-picture architectural intuition.",
                 "Trade-offs & algorithmic choices.",
                 "Real-world application context.",
                 "Connecting theory to industry."
             ],
             "Session 1")
    add_card(s4, Inches(4.85), Inches(2.0), Inches(3.6), Inches(4.8),
             "Class 2 (Tomorrow)",
             [
                 "Technical Deep Dive.",
                 "Mathematical foundations without dry proofs.",
                 "Algorithm mechanics & optimization.",
                 "Vectorized formulas & notation.",
                 "Code walkthroughs & edge cases."
             ],
             "Session 2")
    add_card(s4, Inches(8.9), Inches(2.0), Inches(3.6), Inches(4.8),
             "Class 3 (Lab)",
             [
                 "Hands-on Coding Lab.",
                 "Building from scratch in NumPy first.",
                 "Fitting production Scikit-Learn models.",
                 "Executing Jupyter notebooks in Docker.",
                 "GitHub Classroom push & validation."
             ],
             "Session 3")

    # ------------------ SLIDE 5: HOW WE ARE GOING TO LEARN ------------------
    s5 = prs.slides.add_slide(blank_layout)
    add_bg(s5)
    add_header(s5, "How We Are Going to Learn: The 3 Core Pillars")
    add_card(s5, Inches(0.8), Inches(2.0), Inches(3.6), Inches(4.8),
             "1. Grounded Intuition",
             [
                 "Understand why an algorithm optimizes.",
                 "Visualize geometric loss landscapes.",
                 "Why does gradient descent find the bowl bottom?",
                 "Mental models before library calls."
             ],
             "Pillar 1")
    add_card(s5, Inches(4.85), Inches(2.0), Inches(3.6), Inches(4.8),
             "2. Production Craft",
             [
                 "NumPy vectorization first.",
                 "Then master Scikit-Learn pipelines.",
                 "Reproducible experiments via Docker.",
                 "High-performance, clean Python code."
             ],
             "Pillar 2")
    add_card(s5, Inches(8.9), Inches(2.0), Inches(3.6), Inches(4.8),
             "3. Critical Evaluation",
             [
                 "High training accuracy is often an illusion.",
                 "Audit models for overfitting and data leakage.",
                 "Diagnose dataset bias and failure modes.",
                 "Evaluate honestly on held-out test splits."
             ],
             "Pillar 3")

    # ------------------ SLIDE 6: UNIVERSITY EXPECTATIONS ------------------
    s6 = prs.slides.add_slide(blank_layout)
    add_bg(s6)
    add_header(s6, "University Expectations (Level 6 Academic Rigor)")
    add_card(s6, Inches(0.8), Inches(2.0), Inches(5.6), Inches(4.8),
             "Intellectual Ownership & Independence",
             [
                 "You are the architect of your models and experiments.",
                 "Passive attendance will not yield working systems.",
                 "Take initiative in testing hyperparameters and datasets.",
                 "Engage actively in question-and-answer discussions.",
                 "Read supplementary documentation and papers."
             ],
             "Ownership")
    add_card(s6, Inches(6.9), Inches(2.0), Inches(5.6), Inches(4.8),
             "Empirical Evidence & Scientific Method",
             [
                 "Never say 'my model works' without empirical justification.",
                 "Report metrics: Loss curves, Confusion Matrices, F1, MSE.",
                 "Compare performance against a trivial baseline model.",
                 "Code must be fully reproducible end-to-end.",
                 "Cite academic sources and methodology clearly."
             ],
             "Empirical Rigor")

    # ------------------ SLIDE 7: MUST-DO'S ------------------
    s7 = prs.slides.add_slide(blank_layout)
    add_bg(s7)
    add_header(s7, "The Non-Negotiable 'Must-Do's'")
    add_card(s7, Inches(0.8), Inches(2.0), Inches(5.6), Inches(4.8),
             "Setup & Execution Rules",
             [
                 "1. Environment Setup Complete by Tomorrow:",
                 "Docker Desktop and GitHub accounts verified.",
                 "2. Notebooks MUST Have Executed Cell Outputs:",
                 "Submitting blank code cells with no outputs = zero mark.",
                 "Outputs prove your models actually trained and ran.",
                 "Automated CI/CD checks for output cells on every push."
             ],
             "Environment & Code")
    add_card(s7, Inches(6.9), Inches(2.0), Inches(5.6), Inches(4.8),
             "Commit Cadence & Team Ethics",
             [
                 "3. Consistent Git Commit History:",
                 "Commit incrementally as you build. No mass uploads 5 min before deadline.",
                 "4. Zero Team Ghosting:",
                 "Group project scores are weighted by individual Git commit blame.",
                 "No commits = No individual contribution mark.",
                 "Respect your peers and communicate early."
             ],
             "Accountability")

    # ------------------ SLIDE 8: 12-WEEK ROADMAP ------------------
    s8 = prs.slides.add_slide(blank_layout)
    add_bg(s8)
    add_header(s8, "12-Week Semester Content Roadmap")
    add_card(s8, Inches(0.8), Inches(2.0), Inches(3.6), Inches(4.8),
             "Weeks 1–3: Foundations",
             [
                 "W1: Linear Regression & Gradient Descent.",
                 "W2: Logistic Regression & Decision Boundaries.",
                 "W3: End-to-End ML Workflow, Feature Engineering & Ethics.",
                 "Datasets: Titanic & SUV with Scikit-Learn."
             ],
             "Phase 1")
    add_card(s8, Inches(4.85), Inches(2.0), Inches(3.6), Inches(4.8),
             "Weeks 4–7: Classical & Ensembles",
             [
                 "W4–5: Support Vector Machines (SVM) & Kernels.",
                 "W6: Decision Trees & Random Forests (Bagging).",
                 "W7: Boosting & AdaBoost.",
                 "Milestone: Group Project Proposal Due (10%)."
             ],
             "Phase 2")
    add_card(s8, Inches(8.9), Inches(2.0), Inches(3.6), Inches(4.8),
             "Weeks 8–12: Deep Learning",
             [
                 "W8: Artificial Neural Networks (ANN).",
                 "W9: Convolutional Neural Networks (CNN).",
                 "Milestone: Individual Assignment Due (30%).",
                 "W10–12: Deep Learning Group Project (60%)."
             ],
             "Phase 3")

    # ------------------ SLIDE 9: ASSESSMENTS ------------------
    s9 = prs.slides.add_slide(blank_layout)
    add_bg(s9)
    add_header(s9, "Assessment Structure & Grade Breakdown")
    add_card(s9, Inches(0.8), Inches(2.0), Inches(3.6), Inches(4.8),
             "Group Proposal (10%)",
             [
                 "Due: Week 7 in lab.",
                 "Form teams of 3–4 members.",
                 "Define problem statement and real dataset.",
                 "Propose baseline model & deep learning approach."
             ],
             "Assessment 1")
    add_card(s9, Inches(4.85), Inches(2.0), Inches(3.6), Inches(4.8),
             "Individual Assignment (30%)",
             [
                 "Due: Week 9.",
                 "Select 1 dataset, implement 2 distinct ML algorithms.",
                 "Perform data cleaning, validation, tuning.",
                 "Compare performance metrics in a written report."
             ],
             "Assessment 2")
    add_card(s9, Inches(8.9), Inches(2.0), Inches(3.6), Inches(4.8),
             "Group Project (60%)",
             [
                 "Due: Week 12 Final Hand-in.",
                 "End-to-end Deep Learning system (CNN / DNN).",
                 "Live team presentation & code defense.",
                 "Git commit history verifies individual effort!"
             ],
             "Assessment 3")

    # ------------------ SLIDE 10: MODERN DELIVERY STACK ------------------
    s10 = prs.slides.add_slide(blank_layout)
    add_bg(s10)
    add_header(s10, "The Modernized Delivery Tooling (neo_ML)")
    add_card(s10, Inches(0.8), Inches(2.0), Inches(3.6), Inches(4.8),
             "Docker Containers",
             [
                 "Eliminates 'it works on my machine'.",
                 "Python 3.12, JupyterLab 4, Scikit-Learn locked in.",
                 "Zero package collision across Mac, Win, Linux.",
                 "Runs completely locally without server lag."
             ],
             "Environment")
    add_card(s10, Inches(4.85), Inches(2.0), Inches(3.6), Inches(4.8),
             "GitHub Classroom",
             [
                 "Personal repo for every student.",
                 "Automated CI/CD runner tests every push.",
                 "Checks code execution & cell outputs.",
                 "Commit log is your portfolio."
             ],
             "CI / CD")
    add_card(s10, Inches(8.9), Inches(2.0), Inches(3.6), Inches(4.8),
             "Modern IDE & Notebooks",
             [
                 "VS Code + Python & Jupyter extensions.",
                 "Interactive debugging in notebooks.",
                 "Seamless Git integration in editor.",
                 "Industry-standard toolchain."
             ],
             "Tooling")

    # ------------------ SLIDE 11: AI CODING POLICY ------------------
    s11 = prs.slides.add_slide(blank_layout)
    add_bg(s11)
    add_header(s11, "AI Coding Policy: 'Co-Pilot, Never Auto-Pilot'")
    add_card(s11, Inches(0.8), Inches(2.0), Inches(5.6), Inches(4.8),
             "Allowed & Encouraged",
             [
                 "Asking AI to explain cryptic error stack traces.",
                 "Querying syntax or library documentation.",
                 "Brainstorming hyperparameter search ranges.",
                 "Generating unit tests and plotting boilerplate.",
                 "Asking AI to explain mathematical intuitions."
             ],
             "Green Light")
    add_card(s11, Inches(6.9), Inches(2.0), Inches(5.6), Inches(4.8),
             "Strictly Prohibited",
             [
                 "Copying blocks of code you cannot explain line-by-line.",
                 "Having AI write your individual assignment report.",
                 "Generating group project proposals via generative AI.",
                 "Submitting unverified, unexecuted AI hallucinated code.",
                 "Rule: Weekly REFLECTION.md log required with every push!"
             ],
             "Red Light")

    # ------------------ SLIDE 12: RESOURCES ------------------
    s12 = prs.slides.add_slide(blank_layout)
    add_bg(s12)
    add_header(s12, "Recommended Books & Learning Resources")
    add_card(s12, Inches(0.8), Inches(2.0), Inches(5.6), Inches(4.8),
             "Primary Textbooks",
             [
                 "Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow",
                 "By Aurélien Géron (3rd Edition, O'Reilly) - The practical bible.",
                 "Artificial Intelligence: A Modern Approach (4th Ed.)",
                 "By Stuart Russell and Peter Norvig - Theoretical foundations.",
                 "Neural Networks and Deep Learning by Michael Nielsen",
                 "Free online textbook: neuralnetworksanddeeplearning.com"
             ],
             "Literature")
    add_card(s12, Inches(6.9), Inches(2.0), Inches(5.6), Inches(4.8),
             "Documentation & Online Tools",
             [
                 "Scikit-Learn Official User Guide (scikit-learn.org).",
                 "NumPy & Pandas Documentation for vector operations.",
                 "Google Colab (for free GPU acceleration during deep learning).",
                 "GitHub Discussions in our course organization for technical Q&A."
             ],
             "Documentation")

    # ------------------ SLIDE 13: ACTION CHECKLIST ------------------
    s13 = prs.slides.add_slide(blank_layout)
    add_bg(s13)
    add_header(s13, "Your Action Checklist Before Class 2")
    add_card(s13, Inches(0.8), Inches(2.0), Inches(3.6), Inches(4.8),
             "1. GitHub Account",
             [
                 "Join GitHub Classroom via invite link.",
                 "Apply for GitHub Student Developer Pack.",
                 "Activate free GitHub Copilot.",
                 "Link your student email address."
             ],
             "Action 1")
    add_card(s13, Inches(4.85), Inches(2.0), Inches(3.6), Inches(4.8),
             "2. Docker Setup",
             [
                 "Install Docker Desktop on your machine.",
                 "Verify via: docker --version",
                 "Pull Week 1 image:",
                 "docker pull ghcr.io/lbu-courses/ml-course:week1",
                 "Test opening http://localhost:8888."
             ],
             "Action 2")
    add_card(s13, Inches(8.9), Inches(2.0), Inches(3.6), Inches(4.8),
             "3. Onboarding Guide",
             [
                 "Read neo_ML/onboarding/onboarding.md.",
                 "Review the course syllabus and schedule.",
                 "Form initial connections with prospective group peers.",
                 "Come ready to dive into ML theory tomorrow!"
             ],
             "Action 3")

    # ------------------ SLIDE 14: LOOKING AHEAD & DISCUSSION ------------------
    s14 = prs.slides.add_slide(blank_layout)
    add_bg(s14)
    add_header(s14, "Looking Ahead to Class 2 & Open Floor")
    add_card(s14, Inches(0.8), Inches(2.0), Inches(5.6), Inches(4.8),
             "Coming Up in Class 2 (Tomorrow)",
             [
                 "The Learning Problem: What makes ML work?",
                 "Supervised Learning: Features X, Labels y, Hypothesis h_theta(x).",
                 "Linear Regression: Univariate and Multivariate modeling.",
                 "Mean Squared Error (MSE): The geometry of convex cost.",
                 "Gradient Descent: Walking down the foggy mountain valley."
             ],
             "Next Session")
    add_card(s14, Inches(6.9), Inches(2.0), Inches(5.6), Inches(4.8),
             "Open Floor: Questions & Discussion",
             [
                 "Questions on syllabus, deadlines, or credit breakdown?",
                 "Questions on Docker or GitHub Classroom workflow?",
                 "Questions on assessment criteria or group allocations?",
                 "Lecturer: Sudan Pudasaini",
                 "Let's build systems that actually learn! 🚀"
             ],
             "Discussion")

    output_path = "neo_ML/slides/week1/Week_1_Class_1_Course_Introduction_and_Overview.pptx"
    prs.save(output_path)
    print(f"Presentation successfully saved to: {output_path}")

if __name__ == '__main__':
    create_class1_deck()
