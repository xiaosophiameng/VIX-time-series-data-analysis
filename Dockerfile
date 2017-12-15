FROM python:3

RUN apt-get update --fix-missing && apt-get install -y wget bzip2 ca-certificates \
    libglib2.0-0 libxext6 libsm6 libxrender1 \
    git mercurial subversion

RUN echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh && \
    wget --quiet https://repo.continuum.io/archive/Anaconda3-5.0.1-Linux-x86_64.sh -O ~/anaconda.sh && \
    /bin/bash ~/anaconda.sh -b -p /opt/conda && \
    rm ~/anaconda.sh

RUN apt-get install -y curl grep sed dpkg && \
    TINI_VERSION=`curl https://github.com/krallin/tini/releases/latest | grep -o "/v.*\"" | sed 's:^..\(.*\).$:\1:'` && \
    curl -L "https://github.com/krallin/tini/releases/download/v${TINI_VERSION}/tini_${TINI_VERSION}.deb" > tini.deb && \
    dpkg -i tini.deb && \
    rm tini.deb && \
    apt-get clean

ENV PATH /opt/conda/bin:$PATH

ENTRYPOINT [ "/usr/bin/tini", "--" ]
CMD [ "/bin/bash" ]

# Environment
RUN conda create -n docker-test python=3.6
RUN /bin/bash -c "source activate docker-test"
# Install packages
RUN conda install anaconda numpy
# RUN conda install anaconda argparse
RUN conda install -c conda-forge matplotlib

RUN mkdir docker-test
ADD . /docker-test
#ADD src/get_vix_to_local.py /docker-test
#ADD src/vix_analysis.py /docker-test
#ADD src/plot_vix_analysis.py /docker-test
#ADD Makefile /docker-test
WORKDIR "docker-test"
#RUN mkdir data
#RUN pip install numpy
#RUN pip install argparse
#RUN pip install matplotlib
# COPY data/ /data/
# CMD [ "python", "src/get_vix_to_local.py", "data/vix_data.csv"]
# RUN python src/get_vix_to_local.py data/vix_data.csv
CMD [ "make", "all"]
# CMD [ "make", "data/vix_data.csv" ]
# RUN make -f data/vix_data.csv

RUN /bin/bash -c "source deactivate"
