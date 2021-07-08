FROM tiangolo/uvicorn-gunicorn:python3.8-slim

COPY app/ .
WORKDIR /app
COPY poetry.lock pyproject.toml .

# poetry config virtualenvs.create falseをすることで、直にインストールする
RUN pip install poetry && poetry config virtualenvs.create false && poetry install

# hostを"0.0.0.0"にしないとうまくいかなかった
EXPOSE 80
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80", "--reload"]

# 参考
# https://fastapi.tiangolo.com/ja/deployment/docker/
# https://medium.com/analytics-vidhya/serve-a-machine-learning-model-using-sklearn-fastapi-and-docker-85aabf96729b