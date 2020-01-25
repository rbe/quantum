#!/bin/sh

if [ -z "${IBMQ_TOKEN}" ]
then
    echo "Please enter your IBM Q API token (press enter to skip): "
    read IBMQ_TOKEN
fi
if [ -n "${IBMQ_TOKEN}" ]
then
    cd ibmq
    [ ! -d qiskit-terra ] && git clone https://github.com/Qiskit/qiskit-terra.git
    cd ..
    docker-compose build --build-arg IBMQ_TOKEN=${IBMQ_TOKEN} ibmq
else
    echo "Skipping generation of IBM Q image"
fi

if [ -z "${DWAVE_TOKEN}" ]
then
    echo ""
    echo ""
    echo "Please enter your D-Wave Leap API token (press enter to skip): "
    read DWAVE_TOKEN
fi
if [ -n "${DWAVE_TOKEN}" ]
then
    cd dwave
    [ ! -d dwave-demos ] && git clone --recursive https://github.com/dwavesystems/demos.git dwave-demos
    cd ..
    docker-compose build --build-arg DWAVE_TOKEN=${DWAVE_TOKEN} dwave
else
    echo "Skipping generation of D-Wave image"
fi

if [ $? -eq 0 ]
then
    echo ""
    echo ""
    echo "Start containers by:"
    echo "   docker-compose up -d"
    echo ""
    echo "and enter a container:"
    echo "   docker-compose exec ibmq bash"
    echo "   docker-compose exec dwave bash"
    exit 0
else
    echo $?
fi

