import nox

nox.options.default_venv_backend = "uv"
nox.options.sessions = ["lint", "type_check"]


@nox.session()
def lint(session: nox.Session) -> None:
    session.run_install(
        "uv",
        "sync",
        "--locked",
        "--only-group=lint",
        env={"UV_PROJECT_ENVIRONMENT": session.virtualenv.location},
    )
    session.run("ruff", "check")
    session.run("ruff", "format", "--check")


@nox.session()
def format(session: nox.Session) -> None:
    session.run_install(
        "uv",
        "sync",
        "--locked",
        "--only-group=lint",
        env={"UV_PROJECT_ENVIRONMENT": session.virtualenv.location},
    )
    session.run("ruff", "check", "--fix")
    session.run("ruff", "format")


@nox.session()
def type_check(session: nox.Session) -> None:
    session.run_install(
        "uv",
        "sync",
        "--locked",
        "--no-default-groups",
        "--group=nox",
        "--group=type-check",
        env={"UV_PROJECT_ENVIRONMENT": session.virtualenv.location},
    )
    session.run("pyright")
