# Use an official Python runtime as a base image
FROM python:3.9-slim
# Set the working directory in the container
WORKDIR /app
# Copy the requirements.txt file (if you have one for dependencies)
COPY requirements.txt .
# Alse copy every file
COPY . .
# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir jupyter 
RUN pip install --no-cache-dir -r requirements.txt
# Expose port 8888 to access Jupyter Notebook
EXPOSE 8888
# Set the default command to start Jupyter Notebook
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--allow-root"]

# build: docker build -t mt-hf-notebook .
# run: docker run -it -p 8888:8888 mt-hf-notebook



