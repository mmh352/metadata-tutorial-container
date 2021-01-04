FROM jupyter/base-notebook:python-3.8.6

ARG NB_USER="jovyan"
ARG NB_UID="1000"
ARG NB_GID="100"
ARG TS_CONFIG="tutorial-server-https.ini"

# Configure environment
ENV CONDA_DIR=/opt/conda \
    SHELL=/bin/bash \
    NB_USER=$NB_USER \
    NB_UID=$NB_UID \
    NB_GID=$NB_GID \
    LC_ALL=en_US.UTF-8 \
    LANG=en_US.UTF-8 \
    LANGUAGE=en_US.UTF-8
ENV PATH=$CONDA_DIR/bin:$PATH \
    HOME=/home/$NB_USER

USER $NB_UID
WORKDIR $HOME

COPY --chown=${NB_UID}:${NB_GID} binder/jupyter_notebook_config.py $HOME/.jupyter/jupyter_notebook_config.py

RUN conda install --quiet --yes \
    jupyter-server-proxy \
    pandas \
    scipy \
    seaborn \
    && \
    pip install "tutorial-server>=0.3.1" "polymatheia>=0.3.0" &&\
    conda clean --all -f -y && \
    fix-permissions $CONDA_DIR && \
    fix-permissions /home/$NB_USER

RUN rm -rf $HOME/work && \
    mkdir $HOME/workspace

USER root

COPY binder/jupyter_notebook_config.py /etc/jupyter/jupyter_notebook_config.py
RUN mkdir /etc/tutorial-server
COPY binder/${TS_CONFIG} /etc/tutorial-server/production.ini

RUN fix-permissions /etc/jupyter/

USER $NB_UID
WORKDIR $HOME
