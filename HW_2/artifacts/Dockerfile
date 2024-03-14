FROM alpine:latest

RUN apk add --no-cache texlive py3-pip python3-dev build-base
RUN python3 -m venv /app/venv

RUN source /app/venv/bin/activate && \
    pip3 install --upgrade pip && \
    pip3 install latex_kelonmyosa

WORKDIR /app

COPY generate_pdf.py /app

CMD ["/app/venv/bin/python3", "generate_pdf.py"]
