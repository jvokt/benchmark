FROM python:3

COPY ./benchmark.py .

# > python3 benchmark.py -q 10 -t 10 https://www.google.com
# CMD [ "python", "./benchmark.py", "-q", "10", "-t", "10", "https://www.google.com" ]
ENTRYPOINT [ "python", "./benchmark.py" ]
