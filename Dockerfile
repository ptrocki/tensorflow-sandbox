
FROM gcr.io/tensorflow/tensorflow:latest
COPY script.py /usr/bin/
CMD ["python", "/usr/bin/script.py"]
