FROM python:3.8-alpine

RUN pip install --upgrade pip

WORKDIR /usr/src/app/

ENV PATH="/venv/bin:$PATH"

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python3", "server.py"]