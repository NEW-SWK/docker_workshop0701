FROM python:3.14-rc-bookworm

WORKDIR /

RUN pip install flask

COPY . /

CMD [ "python", "app.py" ]

