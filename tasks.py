from invoke import task

@task(name="generate-env")
def env(ctx):
    ctx.run("python src/config/genv.py")