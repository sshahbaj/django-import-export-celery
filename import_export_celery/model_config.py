from django.apps import apps
from import_export.resources import modelresource_factory
from celery.utils.log import get_task_logger
from leads.resource import get_lead_resource

log = get_task_logger(__name__)


class ModelConfig:
    def __init__(self, app_label=None, model_name=None, resource=None):
        self.model = apps.get_model(app_label=app_label, model_name=model_name)
        log.debug(resource)
        self.resource = get_lead_resource()
