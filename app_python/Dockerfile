FROM python:3.9.6-alpine3.14
LABEL maintainer="d.atonge@innopolis.university"

ENV VENV_PATH=/opt/venv \
    PYTHONDONTWRITEBYTECODE=1
ENV PATH="$VENV_PATH/bin:$PATH"
RUN apk add --no-cache gcc musl-dev && \
    python -m venv $VENV_PATH && \
    adduser --disabled-password app -s /bin/sh -h /home/app

WORKDIR /home/app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt 

USER app

EXPOSE 3000

COPY --chown=app:app Current_Moscow_Time/ ./Current_Moscow_Time/

CMD ["uvicorn", "Current_Moscow_Time.main:app", "--host", "0.0.0.0", "--port", "3000"]