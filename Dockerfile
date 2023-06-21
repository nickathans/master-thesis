FROM nvidia/cuda:11.1.1-cudnn8-runtime-ubuntu18.04
ENV TZ=Europe/Madrid

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update && apt-get install -y --no-install-recommends \
    python3-pip \
    libopencv-dev \
    python3-opencv && \
    rm -rf /var/lib/apt/lists/*

RUN pip3 install --upgrade pip
RUN pip install jupyter
RUN pip install torch==1.10.0+cu111 torchvision==0.11.1+cu111 -f https://download.pytorch.org/whl/cu111/torch_stable.html
RUN pip install matplotlib
RUN pip install nibabel
RUN pip install monai
RUN pip install scikit-image
RUN pip install scikit-learn
RUN pip install pandas
RUN pip install pynvml
RUN pip install tensorflow
RUN pip install --upgrade numpy

EXPOSE 8888

WORKDIR /notebooks

CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]

