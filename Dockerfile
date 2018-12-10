From python:2.7.13-alpine

RUN apk update &&\
    apk add git

RUN git clone https://github.com/shivamgupta01/bitcoin_transaction_analysis.git
WORKDIR /bitcoin_transaction_analysis
RUN chmod +x sniffer.py
RUN pip install boto3 &&\
    pip install base58 &&\
    pip install arrow &&\
    pip install sqlalchemy &&\
    pip install flask &&\
    pip install requests

ENTRYPOINT python app.py


# Docker Run command:
# docker run --rm -it -e AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID -e AWS_SECRET_ACCESS_KE$AWS_SECRET_ACCESS_KEY -p 4000:4000 a238be455008
