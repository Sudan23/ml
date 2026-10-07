import collections.abc
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

def create_deck():
    prs = Presentation()
    # 16:9 widescreen
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)

    blank_layout = prs.slide_layouts[6]

    # Color Palette: Modern Dark Mode
    COLOR_BG = RGBColor(15, 23, 42)       # Slate 900
    COLOR_CARD = RGBColor(30, 41, 59)     # Slate 800
    COLOR_CARD_BORDER = RGBColor(51, 65, 85) # Slate 700
    COLOR_CYAN = RGBColor(56, 189, 248)   # Sky 400
    COLOR_INDIGO = RGBColor(129, 140, 248)# Indigo 400
    COLOR_WHITE = RGBColor(248, 250, 252) # Slate 50
    COLOR_MUTED = RGBColor(148, 163, 184) # Slate 400
    COLOR_ACCENT = RGBColor(250, 204, 21) # Yellow 400

    def add_bg(slide):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(7.5))
        bg.fill.solid()
        bg.fill.fore_color.rgb = COLOR_BG
        bg.line.fill.background()
        return bg

    def add_header(slide, title_text, category_text="MACHINE LEARNING (UFCFAS-15-2) · WEEK 1"):
        # Category tag
        cat_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.45), Inches(11.7), Inches(0.35))
        tf_cat = cat_box.text_frame
        tf_cat.word_wrap = True
        p_cat = tf_cat.paragraphs[0]
        p_cat.text = category_text.upper()
        p_cat.font.name = 'Helvetica'
        p_cat.font.size = Pt(11)
        p_cat.font.bold = True
        p_cat.font.color.rgb = COLOR_CYAN

        # Title
        t_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.75), Inches(11.7), Inches(0.8))
        tf_t = t_box.text_frame
        tf_t.word_wrap = True
        p_t = tf_t.paragraphs[0]
        p_t.text = title_text
        p_t.font.name = 'Helvetica'
        p_t.font.size = Pt(26)
        p_t.font.bold = True
        p_t.font.color.rgb = COLOR_WHITE

        # Divider line
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
        tf.margin_left = Inches(0.3)
        tf.margin_right = Inches(0.3)
        tf.margin_top = Inches(0.3)
        tf.margin_bottom = Inches(0.3)

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
        p_title.space_after = Pt(12)

        for item in items:
            p_item = tf.add_paragraph()
            p_item.text = f"•  {item}"
            p_item.font.name = 'Helvetica'
            p_item.font.size = Pt(13)
            p_item.font.color.rgb = COLOR_WHITE
            p_item.space_after = Pt(8)

    # ==================== SLIDE 1: TITLE SLIDE ====================
    s1 = prs.slides.add_slide(blank_layout)
    add_bg(s1)

    # Accent decorative bar
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
    p1.text = "Machine Learning"
    p1.font.name = 'Helvetica'
    p1.font.size = Pt(44)
    p1.font.bold = True
    p1.font.color.rgb = COLOR_WHITE

    p2 = tf1.add_paragraph()
    p2.text = "Week 1: Module Welcome & Linear Regression Fundamentals"
    p2.font.name = 'Helvetica'
    p2.font.size = Pt(22)
    p2.font.color.rgb = COLOR_INDIGO
    p2.space_after = Pt(24)

    p3 = tf1.add_paragraph()
    p3.text = "Module: UFCFAS-15-2 · Level 6\nLecturer: Sudan Pudasaini · Module Leader (UWE): Prof. Jun Hong"
    p3.font.name = 'Helvetica'
    p3.font.size = Pt(14)
    p3.font.color.rgb = COLOR_MUTED

    # ==================== SLIDE 2: WELCOME & PRINCIPLES ====================
    s2 = prs.slides.add_slide(blank_layout)
    add_bg(s2)
    add_header(s2, "Welcome & The 3 Core Principles of This Module")

    add_card(s2, Inches(0.8), Inches(2.0), Inches(3.6), Inches(4.8), 
             "1. Grounded Intuition", 
             [
                 "No black-box memorization.",
                 "Understand the geometry and math behind algorithms.",
                 "Why does gradient descent move downhill?",
                 "Why does MSE have a single global minimum?"
             ], 
             "Theory")

    add_card(s2, Inches(4.85), Inches(2.0), Inches(3.6), Inches(4.8), 
             "2. Production Craft", 
             [
                 "From scratch in NumPy first.",
                 "Then master Scikit-Learn pipelines.",
                 "Reproducible experiments with Docker.",
                 "Write vectorised, performant Python."
             ], 
             "Engineering")

    add_card(s2, Inches(8.9), Inches(2.0), Inches(3.6), Inches(4.8), 
             "3. Critical Evaluation", 
             [
                 "Never trust a high training score.",
                 "Test for overfitting, data leakage & bias.",
                 "Diagnose real-world edge case failures.",
                 "Measure honestly with test splits."
             ], 
             "Rigor")

    # ==================== SLIDE 3: 12-WEEK ROADMAP ====================
    s3 = prs.slides.add_slide(blank_layout)
    add_bg(s3)
    add_header(s3, "Module Architecture: The 12-Week Roadmap")

    add_card(s3, Inches(0.8), Inches(2.0), Inches(3.6), Inches(4.8), 
             "Weeks 1–3: Foundations", 
             [
                 "W1: Linear Regression & Gradient Descent",
                 "W2: Logistic Regression & Decision Boundaries",
                 "W3: ML Workflow, Feature Engineering & Ethics",
                 "Datasets: Titanic, SUV data with Scikit-Learn"
             ], 
             "Phase 1")

    add_card(s3, Inches(4.85), Inches(2.0), Inches(3.6), Inches(4.8), 
             "Weeks 4–7: Classical & Ensembles", 
             [
                 "W4–5: Support Vector Machines (SVM) & Kernels",
                 "W6: Decision Trees & Random Forests (Bagging)",
                 "W7: Boosting & AdaBoost Algorithms",
                 "Milestone: Group Proposal Due (10%)"
             ], 
             "Phase 2")

    add_card(s3, Inches(8.9), Inches(2.0), Inches(3.6), Inches(4.8), 
             "Weeks 8–12: Deep Learning", 
             [
                 "W8: Artificial Neural Networks (ANN)",
                 "W9: Convolutional Neural Networks (CNN)",
                 "Milestone: Individual Assignment Due (30%)",
                 "W10–12: Deep Learning Group Project (60%)"
             ], 
             "Phase 3")

    # ==================== SLIDE 4: ASSESSMENTS ====================
    s4 = prs.slides.add_slide(blank_layout)
    add_bg(s4)
    add_header(s4, "Assessment Structure & Key Deliverables")

    add_card(s4, Inches(0.8), Inches(2.0), Inches(3.6), Inches(4.8), 
             "Group Proposal (10%)", 
             [
                 "Deadline: Week 7 (in lab).",
                 "Form teams of 3–4 students.",
                 "Define problem statement and real dataset.",
                 "Propose baseline model & deep learning approach."
             ], 
             "Milestone 1")

    add_card(s4, Inches(4.85), Inches(2.0), Inches(3.6), Inches(4.8), 
             "Individual Assignment (30%)", 
             [
                 "Deadline: Week 9.",
                 "Select 1 dataset, implement 2 distinct ML algorithms.",
                 "Perform data cleaning, validation, tuning.",
                 "Compare performance metrics in a written report."
             ], 
             "Milestone 2")

    add_card(s4, Inches(8.9), Inches(2.0), Inches(3.6), Inches(4.8), 
             "Group Project (60%)", 
             [
                 "Deadline: Week 12 Final Hand-in.",
                 "End-to-end Deep Learning system (CNN / DNN).",
                 "Live team presentation & code repository defense.",
                 "Git commits track individual contribution!"
             ], 
             "Milestone 3")

    # ==================== SLIDE 5: MODERN DELIVERY STACK ====================
    s5 = prs.slides.add_slide(blank_layout)
    add_bg(s5)
    add_header(s5, "The Modernized Delivery Tooling (neo_ML)")

    add_card(s5, Inches(0.8), Inches(2.0), Inches(3.6), Inches(4.8), 
             "Docker Environment", 
             [
                 "One command to launch JupyterLab 4.",
                 "Python 3.12, scikit-learn, NumPy pre-installed.",
                 "Zero version conflicts across Mac, Windows, Linux.",
                 "Runs locally without relying on external servers."
             ], 
             "Docker")

    add_card(s5, Inches(4.85), Inches(2.0), Inches(3.6), Inches(4.8), 
             "GitHub Classroom", 
             [
                 "Personal student repositories for weekly labs.",
                 "Automated CI/CD checks on every push.",
                 "Checks code execution (cell outputs must exist!).",
                 "Git commit history = proof of teamwork."
             ], 
             "GitHub")

    add_card(s5, Inches(8.9), Inches(2.0), Inches(3.6), Inches(4.8), 
             "AI Policy with Rigor", 
             [
                 "GitHub Copilot & Gemini encouraged for syntax.",
                 "Never blindly copy unexecuted solutions.",
                 "Weekly REFLECTION.md required with every push.",
                 "Rule: You must be able to explain every line."
             ], 
             "AI Pairing")

    # ==================== SLIDE 6: WHAT IS ML ====================
    s6 = prs.slides.add_slide(blank_layout)
    add_bg(s6)
    add_header(s6, "Conceptual Paradigm: Traditional Code vs Machine Learning")

    add_card(s6, Inches(0.8), Inches(2.0), Inches(5.6), Inches(4.8), 
             "Traditional Programming", 
             [
                 "Input: Data + Explicit Rules (Code).",
                 "Output: Answers / Predictions.",
                 "Engineer manually specifies every logic condition.",
                 "Example: Hundreds of regex rules to detect spam.",
                 "Fails when rules become complex or non-linear."
             ], 
             "Explicit Logic")

    add_card(s6, Inches(6.9), Inches(2.0), Inches(5.6), Inches(4.8), 
             "Machine Learning", 
             [
                 "Input: Data + Answers (Ground Truth Labels).",
                 "Output: Learned Rules (Model Parameters).",
                 "Algorithm optimizes internal weights theta from data.",
                 "Example: Model learns spam patterns automatically.",
                 "Adapts and generalizes to previously unseen examples."
             ], 
             "Learned Parameters")

    # ==================== SLIDE 7: LINEAR REGRESSION HYPOTHESIS ====================
    s7 = prs.slides.add_slide(blank_layout)
    add_bg(s7)
    add_header(s7, "Linear Regression: The Hypothesis Function")

    add_card(s7, Inches(0.8), Inches(2.0), Inches(5.6), Inches(4.8), 
             "Single Feature (1D)", 
             [
                 "Predict target y from one feature x1:",
                 "h_theta(x) = theta_0 + theta_1 * x_1",
                 "theta_0 = Intercept (Bias)",
                 "theta_1 = Slope (Weight / Coefficient)",
                 "Geometrically: A straight line through 2D space."
             ], 
             "Univariate")

    add_card(s7, Inches(6.9), Inches(2.0), Inches(5.6), Inches(4.8), 
             "Multiple Features (Matrix Form)", 
             [
                 "Generalize to n features with dummy x0 = 1:",
                 "h_theta(x) = theta_0*x_0 + theta_1*x_1 + ... + theta_n*x_n",
                 "Vector form: h_theta(x) = theta^T * x",
                 "Dataset matrix form: y_pred = X * theta",
                 "Where X is (m x (n+1)) and theta is ((n+1) x 1)."
             ], 
             "Multivariate")

    # ==================== SLIDE 8: COST FUNCTION ====================
    s8 = prs.slides.add_slide(blank_layout)
    add_bg(s8)
    add_header(s8, "Measuring Error: Mean Squared Error (MSE) Cost")

    add_card(s8, Inches(0.8), Inches(2.0), Inches(5.6), Inches(4.8), 
             "The MSE Cost Formula", 
             [
                 "J(theta) = (1 / 2m) * sum((h_theta(x^(i)) - y^(i))^2)",
                 "Residual: Difference between predicted and actual.",
                 "Squaring errors: Heavily penalizes large misses.",
                 "Factor of 1/2: Conveniently cancels out in derivatives.",
                 "Goal: Find theta that minimizes J(theta)."
             ], 
             "Mathematical Loss")

    add_card(s8, Inches(6.9), Inches(2.0), Inches(5.6), Inches(4.8), 
             "Why Convexity Matters", 
             [
                 "MSE for linear regression is strictly CONVEX.",
                 "Visual representation: A smooth, symmetric bowl.",
                 "There are ZERO local minima traps!",
                 "Every local minimum is guaranteed to be global.",
                 "Guarantees that gradient descent will find the optimum."
             ], 
             "Optimization Geometry")

    # ==================== SLIDE 9: GRADIENT DESCENT ====================
    s9 = prs.slides.add_slide(blank_layout)
    add_bg(s9)
    add_header(s9, "Optimization: Gradient Descent Algorithm")

    add_card(s9, Inches(0.8), Inches(2.0), Inches(5.6), Inches(4.8), 
             "The Descent Intuition", 
             [
                 "Foggy mountain: You cannot see the lowest valley.",
                 "Feel the ground: Identify the steepest uphill slope.",
                 "Take a step in the exact opposite direction (downhill).",
                 "Repeat iteratively until the slope is zero (flat ground).",
                 "Slope is computed via partial derivatives."
             ], 
             "Intuition")

    add_card(s9, Inches(6.9), Inches(2.0), Inches(5.6), Inches(4.8), 
             "The Parameter Update Rule", 
             [
                 "theta_j := theta_j - alpha * (d/d theta_j) J(theta)",
                 "alpha = Learning Rate (step size hyperparameter).",
                 "Partial derivative: (1/m) * sum((h_theta(x) - y) * x_j)",
                 "All parameters theta_0, ..., theta_n updated simultaneously.",
                 "Terminates when cost change is smaller than epsilon."
             ], 
             "Update Formula")

    # ==================== SLIDE 10: LEARNING RATE ====================
    s10 = prs.slides.add_slide(blank_layout)
    add_bg(s10)
    add_header(s10, "Hyperparameter Tuning: The Learning Rate (Alpha)")

    add_card(s10, Inches(0.8), Inches(2.0), Inches(3.6), Inches(4.8), 
             "Alpha Too Small", 
             [
                 "e.g., alpha = 0.00001",
                 "Steps are microscopic.",
                 "Requires tens of thousands of iterations to converge.",
                 "Wastes computing time and energy."
             ], 
             "Understepping")

    add_card(s10, Inches(4.85), Inches(2.0), Inches(3.6), Inches(4.8), 
             "Alpha Just Right", 
             [
                 "e.g., alpha = 0.01 / 0.1",
                 "Takes confident downhill strides.",
                 "Steps automatically shrink as slope flattens.",
                 "Converges smoothly to the minimum."
             ], 
             "Optimal Step")

    add_card(s10, Inches(8.9), Inches(2.0), Inches(3.6), Inches(4.8), 
             "Alpha Too Large", 
             [
                 "e.g., alpha = 2.0",
                 "Overshoots the bottom of the bowl.",
                 "Bounces up opposite walls.",
                 "Cost explodes towards infinity (diverges)!"
             ], 
             "Divergence")

    # ==================== SLIDE 11: IMPLEMENTATION COMPARISON ====================
    s11 = prs.slides.add_slide(blank_layout)
    add_bg(s11)
    add_header(s11, "From Theory to Code: Scratch vs Scikit-Learn")

    add_card(s11, Inches(0.8), Inches(2.0), Inches(5.6), Inches(4.8), 
             "From Scratch (NumPy Vectorization)", 
             [
                 "X_b = np.c_[np.ones((m, 1)), X]",
                 "gradients = (1/m) * X_b.T.dot(X_b.dot(theta) - y)",
                 "theta = theta - alpha * gradients",
                 "Reveals exactly how linear algebra powers ML.",
                 "Essential foundation for neural networks later."
             ], 
             "Under the Hood")

    add_card(s11, Inches(6.9), Inches(2.0), Inches(5.6), Inches(4.8), 
             "Production (Scikit-Learn)", 
             [
                 "from sklearn.linear_model import LinearRegression",
                 "model = LinearRegression()",
                 "model.fit(X_train, y_train)",
                 "y_pred = model.predict(X_test)",
                 "Highly optimized LAPACK solver; industry standard."
             ], 
             "Production Standard")

    # ==================== SLIDE 12: TODAY'S LAB & ACTION ====================
    s12 = prs.slides.add_slide(blank_layout)
    add_bg(s12)
    add_header(s12, "Today's Lab Workflow & Immediate Action Items")

    add_card(s12, Inches(0.8), Inches(2.0), Inches(3.6), Inches(4.8), 
             "1. Environment Launch", 
             [
                 "Pull docker image or start JupyterLab.",
                 "Verify Python 3.12, sklearn, pandas.",
                 "Ensure datasets and notebooks are visible.",
                 "URL: http://localhost:8888"
             ], 
             "Step 1")

    add_card(s12, Inches(4.85), Inches(2.0), Inches(3.6), Inches(4.8), 
             "2. Complete Practical 1", 
             [
                 "Open linear-regression-sklearn-gradient-descent.ipynb.",
                 "Code Gradient Descent manually in NumPy.",
                 "Plot the cost reduction curve J(theta).",
                 "Verify weights match Scikit-Learn."
             ], 
             "Step 2")

    add_card(s12, Inches(8.9), Inches(2.0), Inches(3.6), Inches(4.8), 
             "3. Commit & Reflect", 
             [
                 "Run all notebook cells (outputs visible).",
                 "Create your SETUP.md & REFLECTION.md.",
                 "git add, commit, and git push.",
                 "Automated GitHub Action validates submission!"
             ], 
             "Step 3")

    output_path = "neo_ML/slides/week1/Week_1_ML_Introduction_and_Linear_Regression.pptx"
    prs.save(output_path)
    print(f"Presentation successfully saved to: {output_path}")

if __name__ == '__main__':
    create_deck()
