from apscheduler.schedulers.blocking import BlockingScheduler

from server.ML.ML_main import build_ml_models

b_sched = BlockingScheduler()

# b_sched.add_job(do_something, 'interval', seconds=10)

# Run a scheduled task - once a week in 2AM (make sure that the model reflects the updated data)
b_sched.add_job(build_ml_models, 'cron', day_of_week='sun', hour=2, minute=0)
b_sched.start()
