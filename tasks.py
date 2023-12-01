import shutil
from pathlib import Path
from uuid import uuid4

from invoke import task

WORKSPACE_DIR = "workspace"


def _create_workspace() -> None:
    Path(WORKSPACE_DIR).mkdir(exist_ok=True)


def _init(target: str, suffix: str | None) -> None:
    _create_workspace()
    src = Path(f"template/{target}")
    # dst 生成の際は python/python3.10 → python3.10 にリネームしたい
    target_short = str(Path(target).name)
    while True:
        if suffix is not None:
            dst = Path(f"{WORKSPACE_DIR}/{target_short}_{suffix}")
        else:
            uuid = uuid4()
            dst = Path(f"{WORKSPACE_DIR}/{target_short}_{uuid}")
        if not dst.exists():
            break
        if suffix is not None:
            raise ValueError(
                f"{WORKSPACE_DIR}/{target_short}_{suffix} already exists. Change `{suffix}` or remove `{WORKSPACE_DIR}/{target_short}_{suffix}`."  # noqa: E501
            )
    shutil.copytree(src, dst)
    print(f"{dst} created")


@task
def init_go(_c, name=None):
    """
    Init Go workspace

    Args:
        _c (invoke.Context): invoke context
        name (str | None): workspace directory suffix (if None, uuid4 is used)
    """
    _init("go", name)


@task
def init_python310(_c, name=None):
    """
    Init Python 3.10 workspace

    Args:
        _c (invoke.Context): invoke context
        name (str | None): workspace directory suffix (if None, uuid4 is used)
    """
    _init("python/python3.10", name)


@task
def init_python311(_c, name=None):
    """
    Init Python 3.11 workspace

    Args:
        _c (invoke.Context): invoke context
        name (str | None): workspace directory suffix (if None, uuid4 is used)
    """
    _init("python/python3.11", name)


@task
def init_rust(_c, name=None):
    """
    Init Rust workspace

    Args:
        _c (invoke.Context): invoke context
        name (str | None): workspace directory suffix (if None, uuid4 is used)
    """
    _init("rust", name)


@task
def format(c):
    """
    Run black and isort for tasks.py
    """
    c.run(
        """
        poetry run black tasks.py
        poetry run isort tasks.py
    """
    )


@task(pre=[format])
def lint(c):
    """
    Run flake8 for tasks.py after format task done
    """
    c.run(
        """
        poetry run flake8 tasks.py
    """
    )


@task
def clean_workspace(c):
    """
    Remove all directories under workspace directory
    """
    # note the trailing slash
    c.run("rm -r ./workspace/*/")
