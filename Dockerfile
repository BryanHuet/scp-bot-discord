FROM python

COPY requirements.txt /usr/app/
RUN pip install --upgrade pip && pip install -r /usr/app/requirements.txt

WORKDIR /usr/app