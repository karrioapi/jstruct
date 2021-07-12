#!/usr/bin/env bash

# Python virtual environment helpers

ROOT="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
BASE_DIR="${PWD##*/}"
ENV_DIR=".venv"
DIST="${ROOT:?}/.dist"

activate_env() {
  echo "Activate $BASE_DIR"
  deactivate >/dev/null 2>&1
  # shellcheck source=src/script.sh
  source "${ROOT:?}/$ENV_DIR/$BASE_DIR/bin/activate"
}

create_env() {
    echo "create $BASE_DIR Python3 env"
    deactivate || true
    rm -rf "${ROOT:?}/$ENV_DIR" || true
    mkdir -p "${ROOT:?}/$ENV_DIR"
    python3 -m venv "${ROOT:?}/$ENV_DIR/$BASE_DIR" &&
    activate_env &&
    pip install --upgrade pip
}

init() {
    create_env &&
    pip install -r requirements.dev.txt
}


alias env:new=create_env
alias env:on=activate_env
alias env:reset=init


# Project helpers

test() {
    pytest test/
}

build() {
    clean
	rm -rf "${DIST}"
	mkdir -p "${DIST}"
    python setup.py bdist_wheel &&
    backup_wheels
}

release() {
    pip install twine > /dev/null &&
	twine upload "${DIST}/*"
}

clean() {
    echo "cleaning build files..."
    find . -type d -not -path "*$ENV_DIR/*" -name dist -prune -exec rm -r '{}' \; || true
    find . -type d -not -path "*$ENV_DIR/*" -name build -prune -exec rm -r '{}' \; || true
    find . -type d -not -path "*$ENV_DIR/*" -name "*.egg-info" -prune -exec rm -r '{}' \; || true
}

backup() {
    echo "Listing submodules..."
    [[ -d "$wheels" ]] &&
    find "${DIST}" -not -path "*$ENV_DIR/*" -name \*.whl -prune -exec cp '{}' "$wheels" \; &&
    clean
}

activate_env || true
