# ====================
# Build the base image
# ====================

FROM python:3.8-slim-buster as base

ENV DEBIAN_FRONTEND=noninteractive
RUN apt update && \
        apt dist-upgrade -y && \
        apt install -y \
            curl \
            bzip2
