from typing import List

from singer_sdk import Tap, Stream
from singer_sdk import typing as th 
from tap_sensedata.streams import (
    ContractsStream,
    ContractsStatusStream,
    TasksTypesStream,
    TasksStatusStream,
    PlaybooksStream,
    KpisStream,
    CustomersStream,
    CustomDataStream,
    TasksStream
)

STREAM_TYPES = [
    ContractsStream,
    ContractsStatusStream,
    TasksTypesStream,
    TasksStatusStream,
    PlaybooksStream,
    KpisStream,
    CustomersStream,
    CustomDataStream,
    TasksStream
]


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


    def discover_streams(self) -> List[Stream]:
        """Return a list of discovered streams."""
        return [stream_class(tap=self) for stream_class in STREAM_TYPES]


if __name__ == "__main__":
    Tapsensedata.cli()
