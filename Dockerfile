FROM python:3.12-slim-bookworm

WORKDIR /app

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY doi_citationfinder.py .

EXPOSE 7860

ENV GRADIO_SERVER_NAME="0.0.0.0"

CMD [ "python3", "./doi_citationfinder.py" ]
