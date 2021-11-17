from invoke import task


@task
def start(ctx):
    # for item in ctx:
    #     print(item)
    # print("CTX:\n", ctx["tasks"])
    # print("\n••••••\n")
    ctx.run("python3 src/main.py")


@task
def test(ctx):
    ctx.run("pytest src")


@task
def lint(ctx):
    ctx.run("pylint src")


@task
def format(ctx):
    ctx.run("autopep8 --in-place --recursive src")


@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src")


@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html")
