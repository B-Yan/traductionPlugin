FROM 3.11.0a1-alpine3.14
WORKDIR /usr/src/app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
CMD [ "python", "./endpoint.py" ]