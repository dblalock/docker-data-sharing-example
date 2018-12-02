# Use an official Python runtime as a parent image
FROM python:3.7.1-slim-stretch

RUN groupadd -g 999 appuser && \
    useradd -m -r -u 999 -g appuser appuser
USER appuser

# Install any packages specified in requirements.txt
COPY requirements.txt /home/appuser/requirements.txt
RUN pip install --user --trusted-host pypi.python.org -r \
    /home/appuser/requirements.txt

# Copy the current directory contents into the container at /app
# NOTE: we want this nearly last so only earlier layers of container get reused
COPY . /home/appuser/app
WORKDIR /home/appuser/app

USER root
RUN chown -R appuser:appuser /home/appuser/app
USER appuser

RUN mkdir -p /home/appuser/app/in
RUN mkdir -p /home/appuser/app/out

# Run main.py when the container launches
CMD ["python", "main.py"]
