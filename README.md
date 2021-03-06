# Quantum Computing

Playing around with quantum computers IBM Q and D-Wave.
Get your account at [IBM Quantum Experience](https://quantum-computing.ibm.com) and [D-Wave Leap](https://cloud.dwavesys.com/leap/).

## Container

To build all Docker images provide your API tokens when asked by `run.sh`:

    ./run.sh

To build IBM Q image, use:

    docker-compose build --build-arg IBMQ_TOKEN=... ibmq

or D-Wave enter:

    docker-compose build --build-arg DWAVE_TOKEN=... dwave

## IBM Q

Run a shell in IBM Q Docker container:

    docker-compose exec ibmq bash

### Hello Quantum!

Please patch `hello_quantum.py` (if still neccessary) to use a Quantum chip with 5 (more than 1) qubits:

    cd /qiskit-terra/examples/python/ibmq
    patch hello_quantum.py hq_n_qubits.patch

and execute the example:

    cd /qiskit-terra/examples/python/ibmq
    python hello_quantum.py

which should show:

    BasicAer backends:  [<QasmSimulatorPy('qasm_simulator') from BasicAer()>, ...]
    {'00': 500, '11': 524}
    Remote backends:  [<IBMQBackend('ibmqx2') from IBMQ(hub='ibm-q', group='open', project='main')>, ...]
    Running on current least busy device:  ibmqx2
    Counts:  {'01': 28, '00': 481, '11': 499, '10': 16}

### Star Trek(TM)

Quantum Teleportation using IBM Q:

    cd /heisenberg
    python StarTrek.py

## D-Wave

Run a shell in D-Wave Docker container:

    docker-compose exec dwave bash

### Factoring Demo

Run the factoring demo:

    cd /dwave-demos/factoring
    pip install -r requirements.txt
    python demo.py

This should produce a result like the following:

    Enter a number to be factored:
    Input product        ( 0 <= P <= 63): 15
    Running on QPU
    {'numberOfReads': 50,
     'results': [{'a': 3,
                  'b': 5,
                  'numOfOccurrences': 2,
                  'percentageOfOccurrences': 4.0,
                  'valid': True},
                 {'a': 7,
                  'b': 1,
                  'numOfOccurrences': 4,
                  'percentageOfOccurrences': 8.0,
                  'valid': False},
                 ...],
     'timing': {'actual': {'qpuProcessTime': 25161}}}

### More Demos

To setup another demo:

    cd /dwave-demos/<another demo>
    pip install -r requirements.txt

As every demo may need other versions of software components they will be installed or replaced.
You have been warned.

### Antenna Selection Demo

Setting up Antenna Selection demo:

    cd /demos/antenna-selection
    pip install -r requirements.txt

Will install other software components and versions (done after installing Fraction demo):

    Collecting dwave-ocean-sdk==1.3.0
      Downloading dwave_ocean_sdk-1.3.0-py2.py3-none-any.whl (6.8 kB)
    Collecting matplotlib==2.2.4
      Downloading matplotlib-2.2.4-cp36-cp36m-manylinux1_x86_64.whl (12.8 MB)
    Requirement already satisfied: ...
    Collecting dwave-hybrid<0.3.0,>=0.2.0
      Downloading dwave_hybrid-0.2.1-py2.py3-none-any.whl (71 kB)
    Requirement already satisfied: ...
    Collecting pyparsing!=2.0.4,!=2.1.2,!=2.1.6,>=2.0.1
      Downloading pyparsing-2.4.6-py2.py3-none-any.whl (67 kB)
    Requirement already satisfied: ...
    Collecting pytz
      Downloading pytz-2019.3-py2.py3-none-any.whl (509 kB)
    Collecting kiwisolver>=1.0.1
      Downloading kiwisolver-1.1.0-cp36-cp36m-manylinux1_x86_64.whl (90 kB)
    Collecting cycler>=0.10
      Downloading cycler-0.10.0-py2.py3-none-any.whl (6.5 kB)
    Requirement already satisfied: ...
      Attempting uninstall: dwave-ocean-sdk
        Found existing installation: dwave-ocean-sdk 1.2.0
        Uninstalling dwave-ocean-sdk-1.2.0:
          Successfully uninstalled dwave-ocean-sdk-1.2.0
    Successfully installed cycler-0.10.0 dwave-hybrid-0.2.1 dwave-ocean-sdk-1.3.0 kiwisolver-1.1.0 matplotlib-2.2.4 pyparsing-2.4.6 pytz-2019.3

Execute demo by calling `antennas.py`:

    # python antennas.py 
    Maximum independent set size found is 3
    [2, 5, 7]
    Your plots are saved to antenna_plot_original.png and antenna_plot_solution.png

Have fun!
