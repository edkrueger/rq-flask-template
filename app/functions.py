"""Define functions to use in redis queue."""

import time

from rq import get_current_job

from . import models
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)


def some_long_function(some_input):
    """An example function for redis queue."""
    job = get_current_job()
    time.sleep(10)

    sql_db = SessionLocal()

    result = models.Result(
        job_id=job.id,
        job_enqueued_at=job.enqueued_at,
        job_started_at=job.started_at,
        input=some_input,
        result=some_input,
    )

    sql_db.add(result)
    sql_db.commit()
    sql_db.close()

    return {
        "job_id": job.id,
        "job_enqueued_at": job.enqueued_at.isoformat(),
        "job_started_at": job.started_at.isoformat(),
        "input": some_input,
        "result": some_input,
    }
