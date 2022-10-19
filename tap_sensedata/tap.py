import os
import json

from typing import List

from singer_sdk import Tap, Stream
from singer_sdk import typing as th 
from tap_sensedata.streams import (
    CustomersStream,
    ContractsStream,
    ContractsStatusStream,
    CustomDataStream,
    TasksTypesStream,
    TasksStatusStream,
    PlaybooksStream,
    KpisStream,
    TasksStream
)

STREAM_TYPES = {
    "Customers": CustomersStream,
    "Contracts": ContractsStream,
    "ContractsStatus": ContractsStatusStream,
    "CustomData": CustomDataStream,
    "TasksTypes": TasksTypesStream,
    "TasksStatus": TasksStatusStream,
    "Playbooks": PlaybooksStream,
    "Kpis": KpisStream,
    "Tasks": TasksStream
}


class Tapsensedata(Tap):
    """sensedata tap class."""
    name = "tap-sensedata"

    config_jsonschema = th.PropertiesList(
        th.Property(
            "auth_token",
            th.StringType,
            required=True,
            description="The token to authenticate against the API service"
        ),
        th.Property(
            "start_date",
            th.DateTimeType,
            description="The earliest record date to sync"
        ),
    ).to_dict()
    

    def get_stream_types(self) -> List[Stream]:

        stream_types = []
        select_statement = json.loads(os.environ.get("TAP_SENSEDATA__SELECT", '["*.*"]'))

        if select_statement == ["*.*"]:
            stream_types = STREAM_TYPES.values()
        else:
            stream_types = [
                STREAM_TYPES.get(s.replace(".*", "")) for s in select_statement
            ]

        return stream_types


    def discover_streams(self) -> List[Stream]:
        """Return a list of discovered streams."""

        stream_classes: List[Stream] = []

        for stream_class in self.get_stream_types():

            stream_classes.append(
                stream_class(tap=self)
            )

        return stream_classes


if __name__ == "__main__":
    Tapsensedata.cli()
