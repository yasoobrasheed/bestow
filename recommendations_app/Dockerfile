FROM python:3.10-alpine

WORKDIR /recommendations_app

EXPOSE 5001
ENV FLASK_APP=recommendations_app.py

COPY . /recommendations_app
RUN pip install --no-cache-dir -r requirements.txt

CMD [ "flask", "run", "--host", "0.0.0.0" ]