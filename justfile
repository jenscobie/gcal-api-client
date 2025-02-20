set working-directory := 'src'

default:
    @just --list

build: clean test int

clean:
  uv lock
  uv sync
  rm -f tests/data/account/valid-token/token.json

coverage:
    uv run pytest --cov=. --cov-report=html ../tests/unit

format:
    ruff format .

[no-cd]
int:
    uv run pytest --color=yes tests/integration

lint:
    ruff check .

[no-cd]
test:
    uv run pytest tests/unit
