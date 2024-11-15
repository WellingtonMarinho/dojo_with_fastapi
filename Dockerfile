FROM python:3.13

WORKDIR /src

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8000
