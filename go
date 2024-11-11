#!/usr/bin/env bash

set -e

function helptext {
    echo "Usage: ./go <command>"
    echo ""
    echo "Available commands are:"
    echo "    build       Build and test in dev environment"
    echo "    cov         Run coverage report and show results"
    echo "    format      Run format rules only against repository"
    echo "    int         Run integration test suite"
    echo "    lint        Run lint rules only against repository"
    echo "    test        Run unit test suite"
}

function coverage {
    validate_environment

    poetry run pytest --cov=gcal_manager --cov-report=html tests/unit
    open htmlcov/index.html
}

function format {
    validate_environment

    poetry run ruff format .
}

function lint {
    validate_environment

    poetry run ruff check .
}

function test {
    validate_environment

    poetry run pytest tests/unit
}

function integration {
    validate_environment

    poetry run pytest tests/integration
}

function validate_environment {
    command -v poetry >/dev/null 2>&1 || { echo >&2 "Please install poetry"; exit 1; }

    poetry lock --no-update
    poetry install
}

[[ $@ ]] || { helptext; exit 1; }

case "$1" in
    help) helptext
    ;;
    cov) coverage;
    ;;
    build) format;lint;test;coverage;integration;
    ;;
    format) format
    ;;
    lint) lint
    ;;
    test) test
    ;;
    int) integration
    ;;
esac
