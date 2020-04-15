import nox


@nox.session(python=False)
def docs(session):
    session.chdir("docs")
    session.run("rm", "-rf", "_build/", external=True)
    session.run("poetry", "shell")
    session.run("poetry", "install")
    sphinx_args = ["-W", ".", "_build/html"]

    if "serve" in session.posargs:
        session.run("sphinx-autobuild", *sphinx_args)
    else:
        session.run("sphinx-build", *sphinx_args)
