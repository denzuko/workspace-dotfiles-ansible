#! /usr/bin/env python3

from invoke import Collection, task

@task(default=True)
def run_playbook(context):
    context.run(f"ansible-playbook -K $HOME/.local/etc/config.yml")

@task
def report(context):
    context.run(f"monit summary")

namespace = Collection(run_playbook, report)
