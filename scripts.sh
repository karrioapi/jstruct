#!/usr/bin/env bash

test() {
    pytest test/
}

build() {
    python setup.py sdist bdist_wheel
}

init() {
    rm -r ./venv
    python3 -m venv ./venv &&
    . ./venv/bin/activate &&
    pip install -r requirements.txt &&
    pip install -e .
}
