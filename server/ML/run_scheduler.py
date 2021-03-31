from apscheduler.schedulers.blocking import BlockingScheduler
from server.ML.test import exec_predictions
from server.database.queries.test import *
from server.database.database import Database

b_sched = BlockingScheduler()


def do_something():
    database = Database()
    database.create_table(CREATE_TABLE_QUERY)
    database.insert_data(ADD_QUERY, ("Hello world!!",))
    database.close_connection()


def sched():
    b_sched.add_job(do_something, 'interval', seconds=60)
    # b_sched.add_job(do_something, 'cron', day_of_week='sun', hour=2, minute=0)
    b_sched.start()
