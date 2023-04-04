FROM python:3.10-alpine

WORKDIR /places_app

EXPOSE 5000
ENV FLASK_APP=places_app.py

COPY . /places_app
RUN pip install --no-cache-dir -r requirements.txt

CMD [ "flask", "run", "--host", "0.0.0.0" ]