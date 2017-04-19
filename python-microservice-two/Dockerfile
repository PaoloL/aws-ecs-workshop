FROM python:3.4-alpine
ADD /application/ /application
WORKDIR /application
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
EXPOSE 8080
