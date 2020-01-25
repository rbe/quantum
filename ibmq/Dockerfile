FROM python:3.7.6-slim-buster AS python
RUN apt-get update
RUN apt-get -y install \
            vim \
            git
RUN apt-get -y install \
            gcc g++ cmake
RUN pip install --upgrade pip \
    && pip install --upgrade setuptools

FROM python AS qiskit
RUN pip install cython
RUN pip install qiskit
#RUN pip install qiskit-aer
#RUN pip install qiskit-ibmq-provider

FROM qiskit
# Use volume from docker-compose
#RUN git clone https://github.com/Qiskit/qiskit-terra.git
ARG IBMQ_TOKEN=
RUN python -c "import qiskit; qiskit.IBMQ.save_account(token='${IBMQ_TOKEN}')"
COPY hq_n_qubits.patch /ibmq/qiskit-terra/examples/python/ibmq
# Do not patch by default
#RUN patch hello_quantum.py hq_n_qubits.patch
WORKDIR /ibmq
CMD ["tail", "-f", "/dev/null"]
