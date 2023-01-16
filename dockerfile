#docker build -t google-images-classifier .
#docker run -it -p 9797:9797 google-images-classifier
FROM python:3.9-slim-buster

WORKDIR /app

COPY Pipfile Pipfile.lock requirements.txt main.py ./
COPY application ./application
COPY models ./models

RUN pip install pipenv --upgrade
RUN pipenv install --system --deploy


EXPOSE 9797

ENTRYPOINT ["uvicorn", "main:app", "--host","0.0.0.0","--port","9797"]
