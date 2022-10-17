from pathlib import Path
from typing import Any, Dict, List

from tap_sensedata.client import sensedataStream

SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")

class CustomersStream(sensedataStream):
    name = "customers"
    path = "/customers"
    primary_keys = ["id"]
    schema_filepath = SCHEMAS_DIR / "customers.json"
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

class CustomDataStream(sensedataStream):
    name = "custom_data"
    path = "/custom_data"
    primary_keys = ["id"]
    schema_filepath = SCHEMAS_DIR / "custom_data.json"
    records_jsonpath = "$.{}[*]".format(name)

class CustomTasksTypes(sensedataStream):
    name = "tasks_types"
    path = "/tasks_types"
    primary_keys = ["id"]
    schema_filepath = SCHEMAS_DIR / "tasks_types.json"
    records_jsonpath = "$.{}[*]".format(name)

class CustomTasksStatus(sensedataStream):
    name = "tasks_status"
    path = "/tasks_status"
    primary_keys = ["id"]
    schema_filepath = SCHEMAS_DIR / "tasks_status.json"
    records_jsonpath = "$.{}[*]".format(name)

class CustomTasks(sensedataStream):
    name = "tasks"
    path = "/tasks"
    primary_keys = ["id"]
    replication_key = "updated_at"
    schema_filepath = SCHEMAS_DIR / "tasks.json"
    records_jsonpath = "$.{}[*]".format(name)

class CustomPlaybooks(sensedataStream):
    name = "playbooks"
    path = "/playbooks"
    primary_keys = ["id"]
    replication_key = "created_on"
    schema_filepath = SCHEMAS_DIR / "playbooks.json"
    records_jsonpath = "$.{}[*]".format(name)

class CustomKpis(sensedataStream):
    name = "kpis"
    path = "/kpis"
    primary_keys = ["type", "ref_date", "id_customer"]
    replication_key = "ref_date"
    schema_filepath = SCHEMAS_DIR / "kpis.json"
    records_jsonpath = "$.{}[*]".format(name)