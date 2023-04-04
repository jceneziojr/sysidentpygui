FROM python:3.10-slim

EXPOSE 8501

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

ENTRYPOINT ["streamlit", "run"]

CMD ["1_🔎_SysIdentPyGUI.py"]