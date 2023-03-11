FROM python:3.8

ENV PYTHONUNBUFFERED 1

RUN mkdir /backend
WORKDIR /backend
COPY . /backend

ADD requirements.txt /backend
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN python manage.py collectstatic --no-input

CMD ["gunicorn", "--chdir", "backend", "--bind", ":8000", "backend.wsgi:application"]