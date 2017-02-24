from __future__ import absolute_import, unicode_literals
from .__main__ import app
from celery import Task


class DebugTask(Task):
    def __call__(self, *args, **kwargs):
        print('TASK STARTING: {0.name}[{0.request.id}]'.format(self))
        return super(DebugTask, self).__call__(*args, **kwargs)

@app.task(base=DebugTask)
def add(x, y):
    return x + y

@app.task(base=DebugTask)
def submit_task(f):
    return f()