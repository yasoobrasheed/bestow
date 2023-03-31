FROM python:3.10-alpine

WORKDIR /app

EXPOSE 5000
ENV FLASK_APP=app.py

COPY . /app
RUN pip install --no-cache-dir -r requirements.txt

CMD [ "flask", "run", "--host", "0.0.0.0" ]