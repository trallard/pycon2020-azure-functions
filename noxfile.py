import nox


@nox.session(python=False)
def docs(session):
    """Build the documentation, note this uses Poetry"""
    session.chdir("docs")
    session.run("rm", "-rf", "_build/", external=True)
    session.run("poetry", "shell")
    session.run("poetry", "install")
    sphinx_args = ["-b", "html", "-W", "-d", "_build/doctrees", ".", "_build/html"]

    if "serve" in session.posargs:
        sphinx_cmd = "sphinx-autobuild"
        sphinx_args.insert(0, "--open-browser")
    else:
        sphinx_cmd = "sphinx-build"

    session.run(sphinx_cmd, *sphinx_args)


@nox.session(python="3.8")
def blacken(session):
    """Run black code formater."""
    session.install("black==19.3b0", "isort==4.3.21")
    files = ["**/*.py"]
    session.run("black", *files)
    session.run("isort", "--recursive", *files)
