# python3.11

## Install

```shellscript
$ poetry install
```

## Run

```shellscript
poetry run python -m src
```

## Format

```shellscript
poetry run black . && poetry run isort .
```

## Invoke tasks

```
$ poetry run invoke --list
Available tasks:

  format   Format the code
  run      Run the main function
```
