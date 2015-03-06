#!/usr/bin/env python

import time

from tinflask.web import Application


def dummy_func():
	time.sleep(3)

app = Application()
app.add_status_job("dummy", 5, dummy_func)
app.run()
