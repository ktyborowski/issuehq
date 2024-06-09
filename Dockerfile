FROM python:3.10

RUN pip install pipenv

ENV PROJECT_DIR /app


COPY ./Pipfile ${PROJECT_DIR}/Pipfile
COPY ./Pipfile.lock ${PROJECT_DIR}/Pipfile.lock

COPY ./issuehq ${PROJECT_DIR}/issuehq

WORKDIR ${PROJECT_DIR}

RUN pipenv install --system --deploy

CMD ["gunicorn", "--graceful-timeout", "5", "--chdir", "issuehq", "app:app",  "-w", "4", "-b", "0.0.0.0:8081"]