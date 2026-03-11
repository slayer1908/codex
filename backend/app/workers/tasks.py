from app.workers.celery_app import celery_app


@celery_app.task
def run_optimization_task(campaign_id: int) -> dict:
    return {"campaign_id": campaign_id, "status": "optimization_executed"}
