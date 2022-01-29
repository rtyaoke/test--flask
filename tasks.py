from invoke import task
import os

@task
def setup(c): # 初回git clone直後に実行で、開発環境構築
  cmd1 = "python -m venv ."
  cmd2 = "pip install -r requirements.txt"
  cmd = f"{cmd1} && {cmd2}"
  result = c.run(cmd)

@task
def install(c):
  cmd = "pip install -r requirements.txt"
  result = c.run(cmd)

@task
def run(c):
  cmd = "python main.py"
  result = c.run(cmd)

@task
def test(c):
  cmd = "python -m unittest discover tests"
  result = c.run(cmd)
