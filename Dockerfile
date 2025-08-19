
FROM python:3.12-slim
WORKDIR /DEVOPS_PROJECT
COPY dependencies.txt .
RUN pip install --no-cache-dir -r dependencies.txt
COPY . .

CMD ["bash", "-c", "python test.py && python main.py"]