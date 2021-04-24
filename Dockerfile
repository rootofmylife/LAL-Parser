FROM ubuntu:18.04
FROM python:3.8-buster

COPY . /home

WORKDIR /home

RUN pip3 install -r requirements.txt

RUN pip3 install torch==1.8.1+cpu torchvision==0.9.1+cpu torchaudio==0.8.1 -f https://download.pytorch.org/whl/torch_stable.html

WORKDIR /home/EVALB

RUN make

WORKDIR /home

CMD ["./best_parser_training_script.sh"]