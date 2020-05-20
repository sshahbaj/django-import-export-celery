import importlib

celery_app = importlib.import_module('ct_leads.celery').app
