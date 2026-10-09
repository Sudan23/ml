# ML Course — Docker Image
# Python 3.12 + JupyterLab + all ML libraries
# Used for: Machine Learning (UFCFAS-15-2)

FROM python:3.12-slim-bookworm

LABEL org.opencontainers.image.title="ML Course — Week 1"
LABEL org.opencontainers.image.description="Machine Learning course, JupyterLab + sklearn environment"
LABEL org.opencontainers.image.source="https://github.com/Sudan23/ml"

# System deps
RUN apt-get update && apt-get install -y \
    git \
    curl \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install Python ML stack
RUN pip install --no-cache-dir \
    jupyterlab==4.* \
    notebook \
    numpy \
    pandas \
    matplotlib \
    seaborn \
    scikit-learn \
    scipy \
    ipywidgets \
    nbconvert \
    nbformat \
    plotly

# Create student user
RUN useradd -m -s /bin/bash student
WORKDIR /home/student/notebooks
RUN chown -R student:student /home/student

# Copy Week 1 notebooks (pre-loaded)
COPY week1/ /home/student/notebooks/week1/
RUN chown -R student:student /home/student/notebooks

USER student

# JupyterLab config — no token for local use (inside Docker, not public)
RUN mkdir -p /home/student/.jupyter && \
    echo "c.ServerApp.token = ''" >> /home/student/.jupyter/jupyter_server_config.py && \
    echo "c.ServerApp.password = ''" >> /home/student/.jupyter/jupyter_server_config.py && \
    echo "c.ServerApp.open_browser = False" >> /home/student/.jupyter/jupyter_server_config.py && \
    echo "c.ServerApp.ip = '0.0.0.0'" >> /home/student/.jupyter/jupyter_server_config.py

EXPOSE 8888

# Students run: docker run -p 8888:8888 -v $(pwd):/home/student/notebooks/mywork alkimi/ml:week1
# Then open: http://localhost:8888
CMD ["jupyter", "lab", "--notebook-dir=/home/student/notebooks"]
