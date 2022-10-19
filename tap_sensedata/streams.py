from pathlib import Path
from typing import Any, Dict, List

from tap_sensedata.client import sensedataStream

SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")


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
    primary_keys = ["type", "ref_date", "id_customer"]
    replication_key = "ref_date"
    schema_filepath = SCHEMAS_DIR / "kpis.json"
    records_jsonpath = "$.{}[*]".format(name)