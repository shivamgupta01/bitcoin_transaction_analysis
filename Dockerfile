From sabbir1cse/ubuntu-python-pip-supervisor
RUN apt-get update &&\
    apt-get install curl -y &&\
    apt-get install git -y &&\
    apt-get install python2.7 -y &&\
    curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py" &&\
    python get-pip.py &&\
    pip3 install --upgrade pip
RUN pip install boto3 &&\
    pip install base58 &&\
    pip install arrow &&\
    pip install sqlalchemy &&\
    pip install flask
RUN git clone https://github.com/shivamgupta01/bitcoin_transaction_analysis.git
RUN ./sniffer.py
ENTRYPOINT python app.py
