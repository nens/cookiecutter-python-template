FROM python:3.13

# Install GDAL dependencies
RUN apt-get update && apt-get install -y \
    libgdal-dev \
    libsqlite3-mod-spatialite
# Set the environment variables for GDAL
ENV CPLUS_INCLUDE_PATH=/usr/include/gdal
ENV C_INCLUDE_PATH=/usr/include/gdal

# uv installation
COPY --from=ghcr.io/astral-sh/uv:0.8.17 /uv /usr/local/bin/uv
ENV UV_LINK_MODE=copy \
    UV_PYTHON_DOWNLOADS=never \
    UV_PYTHON=python3.13

WORKDIR /code
COPY pyproject.toml uv.lock  /code/
RUN uv sync --no-install-project

# We only need to copy the src/ dir. This ensures the /code/staticfiles (filled below)
# is totally left alone.
COPY src src
RUN uv sync
ENV PATH="/code/.venv/bin:$PATH"

RUN python src/manage.py collectstatic --noinput --clear
