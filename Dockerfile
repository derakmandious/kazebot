FROM python:3.10.8

WORKDIR /kaze

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .

CMD ["python3", "kaze_bot.py"]