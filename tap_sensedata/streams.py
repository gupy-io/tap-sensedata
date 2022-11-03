from pathlib import Path
import os
from datetime import date, timedelta

from tap_sensedata.client import sensedataStream

SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")


class CustomersStream(sensedataStream):
    name = "customers"
    path = "/customers"
    primary_keys = ["id"]
    replication_key = "updated_at"
    schema_filepath = SCHEMAS_DIR / "customers.json"
    records_jsonpath = "$.{}[*]".format(name)

class CustomDataStream(sensedataStream):
    name = "custom_data"
    path = "/custom_data"
    primary_keys = ["id"]
    ref_date_start = date.today() - timedelta(days=int(os.getenv("TAP_SENSEDATA_CUSTOM_DATA_REF_DATE_START")))
    query_search={
        "ref_date:start": f'{ref_date_start}',
        "limit": 1000
    }
    replication_key = "ref_date"
    schema_filepath = SCHEMAS_DIR / "custom_data.json"
    records_jsonpath = "$.{}[*]".format(name)

class ContractsStream(sensedataStream):
    name = "contracts"
    path = "/contracts"
    primary_keys = ["id"]
    replication_key = "created_at"
    schema_filepath = SCHEMAS_DIR / "contracts.json"
    records_jsonpath = "$.{}[*]".format(name)

class ContractsStatusStream(sensedataStream):
    name = "contracts_status"
    path = "/contracts_status"
    primary_keys = ["id"]
    schema_filepath = SCHEMAS_DIR / "contracts_status.json"
    records_jsonpath = "$.{}[*]".format(name)

class TasksTypesStream(sensedataStream):
    name = "tasks_types"
    path = "/tasks_types"
    primary_keys = ["id"]
    schema_filepath = SCHEMAS_DIR / "tasks_types.json"
    records_jsonpath = "$.{}[*]".format(name)

class TasksStatusStream(sensedataStream):
    name = "tasks_status"
    path = "/tasks_status"
    primary_keys = ["id"]
    schema_filepath = SCHEMAS_DIR / "tasks_status.json"
    records_jsonpath = "$.{}[*]".format(name)

class TasksStream(sensedataStream):
    name = "tasks"
    path = "/tasks"
    primary_keys = ["id"]
    replication_key = "updated_at"
    schema_filepath = SCHEMAS_DIR / "tasks.json"
    records_jsonpath = "$.{}[*]".format(name)

class PlaybooksStream(sensedataStream):
    name = "playbooks"
    path = "/playbooks"
    primary_keys = ["id"]
    replication_key = "created_on"
    schema_filepath = SCHEMAS_DIR / "playbooks.json"
    records_jsonpath = "$.{}[*]".format(name)

class KpisStream(sensedataStream):
    name = "kpis"
    path = "/kpis"
    primary_keys = ["type.name", "ref_date", "id_customer"]
    ref_date_start = date.today() - timedelta(days=int(os.getenv("TAP_SENSEDATA_KPIS_REF_DATE_START")))
    query_search={
        "ref_date:start": f'{ref_date_start}',
        "limit": 1000
    }
    replication_key = "ref_date"
    schema_filepath = SCHEMAS_DIR / "kpis.json"
    records_jsonpath = "$.{}[*]".format(name)