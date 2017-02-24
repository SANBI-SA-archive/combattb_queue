from __future__ import absolute_import, unicode_literals
from .celery import app
from celery import Task
import subprocess,os


class DebugTask(Task):
    def __call__(self, *args, **kwargs):
        print('TASK STARTING: {0.name}[{0.request.id}]'.format(self))
        return super(DebugTask, self).__call__(*args, **kwargs)

@app.task(base=DebugTask)
def run_tree_2_neo(history_id):
    try:
        p = subprocess.Popen(['tree2neo', "init", "-D", "{}".format(str(os.getcwd()) + "/data/"),
                                "{}".format(history_id)], stdout=subprocess.PIPE)
        out, err = p.communicate()
    except(OSError, ValueError) as e:
        print(e)
    return out, err