# ====================
# Build the base image
# ====================

FROM python:3.8-slim-buster as base

ENV DEBIAN_FRONTEND=noninteractive
RUN apt update && \
        apt dist-upgrade -y && \
        apt install -y \
            curl \
            bzip2 \
            git


# =====================
# Build the core system
# =====================
FROM base as system_setup

RUN pip install git+https://github.com/mmh352/tutorial-server.git
COPY ./binder/entrypoint.sh /usr/bin/entrypoint.sh
COPY ./binder/tutorial-server-config.ini /etc/ou_module/tutorial-server-config.ini


# ====================
# Setup the user stuff
# ====================

FROM system_setup as user_setup

ARG NB_USER
ARG NB_UID
ENV USER ${NB_USER}
ENV HOME /home/${NB_USER}

RUN groupadd \
        --gid ${NB_UID} \
        ${NB_USER} && \
    useradd \
        --comment "Default user" \
        --create-home \
        --gid ${NB_UID} \
        --no-log-init \
        --shell /bin/bash \
        --uid ${NB_UID} \
        ${NB_USER}


# =====================
# Build the final image
# =====================

FROM user_setup

ARG NB_USER
ARG NB_UID
ENV USER ${NB_USER}
ENV HOME /home/${NB_USER}

COPY --chown=${NB_UID}:${NB_UID} ./home ${HOME}

ENTRYPOINT [ "/usr/bin/entrypoint.sh" ]
CMD []
