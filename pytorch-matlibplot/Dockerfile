FROM pytorch/pytorch:2.0.1-cuda11.7-cudnn8-devel
LABEL authors="patrick-srv"

RUN /opt/conda/bin/python -mpip install matplotlib
RUN mkdir /code
RUN mkdir /code/cifar
RUN mkdir /data
RUN mkdir /weights
ENTRYPOINT ["python", "/code/cifar/main.py"]