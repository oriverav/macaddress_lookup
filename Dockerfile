FROM python:3
ADD macaddress_lookup.py /
RUN pip install requests
RUN pip install tabulate
ENTRYPOINT [ "python", "./macaddress_lookup.py"]