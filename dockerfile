FROM python:3.10-slim
ENV TOKEN="6677137414:AAF7LtdAoNCCbgyMnqhk80HNqbJ5aG3blQY"
COPY . .
RUN pip install -r req.txt
CMD python bot.py