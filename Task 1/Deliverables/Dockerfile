FROM alpine:latest

WORKDIR /code

COPY ./ /code/

RUN apk add --no-cache python3 py-pip &&\
    pip install -r /code/requirements.txt &&\
    mkdir output

CMD ["python", "main.py", "--config", "config.yaml", "--output", "output", "--debug"]