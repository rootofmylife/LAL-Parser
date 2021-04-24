FROM ubuntu:18.04
FROM python:3.8-buster

COPY . /home

WORKDIR /home

RUN pip3 install -r requirements.txt

WORKDIR /home/EVALB

RUN make

WORKDIR /home

CMD ["./best_parser_training_script.sh"]