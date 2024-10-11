FROM python:3.12


RUN apt-get update && apt-get install -y build-essential

WORKDIR /app

COPY . .

RUN python -m venv venv

CMD ["source", "venv/bin/activate"]

RUN pip install --upgrade pip

RUN pip install -r req.txt

RUN python manage.py collectstatic --noinput