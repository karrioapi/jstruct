#!/usr/bin/env bash

test() {
    pytest test/
}

build() {
    rm -r ./dist || true
    python -m pip install --upgrade setuptools wheel twine
    python setup.py bdist_wheel
}

init() {
    deactivate || true
    rm -r ./venv || true
    python3 -m venv ./venv &&
    . ./venv/bin/activate &&
    pip install -r requirements.txt &&
    pip install -e .
}

release_test() {
    python -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*
}

release() {
    python -m twine upload dist/*
}
