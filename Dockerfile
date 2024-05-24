FROM python

COPY requirements.txt /usr/
RUN pip install --upgrade pip && pip install -r /usr/requirements.txt

WORKDIR /usr/