FROM alpine:edge

RUN apk add --update py3-pip

COPY requirements.txt .
RUN pip install --no-cache-dir -r ./requirements.txt

COPY app.py .
COPY steganography.py .
COPY README.md .

ADD static ./static
ADD templates ./templates

EXPOSE 5000

CMD ["python3", "app.py"]