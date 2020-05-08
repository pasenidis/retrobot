FROM python:3
ADD src /
RUN pip install discord.py
CMD [ "python", "./bot.py" ]
