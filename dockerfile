#docker build -t google-images-classifier .
#docker run -it -p 9696:9696 google-images-classifier
FROM python:3.9-slim-buster

WORKDIR /app

COPY Pipfile Pipfile.lock requirements.txt main.py ./
COPY application ./application
COPY models ./models

RUN pip install pipenv --upgrade
RUN pipenv install --system --deploy

#COPY ["predict.py", "model_C=1.0.bin", "./"]

EXPOSE 9797

ENTRYPOINT ["uvicorn", "main:app", "--host","0.0.0.0","--port","9797"]
