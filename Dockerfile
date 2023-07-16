FROM python:3.10.6
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
ENV DB_HOST=localhost
ENV DB_USER=python
ENV DB_PASSWORD=python
ENV DB_DATABASE=database
CMD ["python","app.py"]
