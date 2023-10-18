FROM python:3.10-slim
ENV TOKEN="YOUR_TOKEN"
COPY . .
RUN pip install -r req.txt
CMD python bot.py