FROM python:3.7
WORKDIR /app-fastapi

COPY requirements.txt requirements.txt

COPY app.py .
COPY pytest.ini pytest.ini

RUN pip3 install --no-cache-dir -r requirements.txt

RUN mkdir -p config controllers entities models tests

COPY config/ config/
COPY controllers/ controllers/
COPY entities/ entities/
COPY models/ models/
COPY tests/ tests/

RUN chmod -R a+rwx config controllers entities models tests
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]
