from datetime import date, timedelta
from typing import Any, Dict, Iterable, Optional

import requests
from singer_sdk.authenticators import BearerTokenAuthenticator
from singer_sdk.helpers.jsonpath import extract_jsonpath
from singer_sdk.streams import RESTStream


class sensedataStream(RESTStream):
    """sensedata stream class."""

    url_base = "https://api.sensedata.io/v2"
    next_page_token_jsonpath = "$.next_page"
    query_search = {}
    days_to_decrease_config_name = ""

    @property
    def authenticator(self) -> BearerTokenAuthenticator:
        """Return a new authenticator object."""
        return BearerTokenAuthenticator.create_for_stream(
            self, token=self.config.get("auth_token")
        )

    @property
    def http_headers(self) -> dict:
        """Return the http headers needed."""
        headers = {}
        if "user_agent" in self.config:
            headers["User-Agent"] = self.config.get("user_agent")
        return headers

    def parse_response(self, response: requests.Response) -> Iterable[dict]:
        """Parse the response and return an iterator of result rows."""
        # TODO: Parse response body and return a set of records.
        yield from extract_jsonpath(self.records_jsonpath, input=response.json())

    def post_process(self, row: dict, context: Optional[dict]) -> dict:
        """As needed, append or transform raw data to match expected structure."""
        # TODO: Delete this method if not needed.
        return row

    def get_url_params(
        self, context: Optional[dict], next_page_token: Optional[Any]
    ) -> Dict[str, Any]:
        """Return a dictionary of values to be used in URL parameterization."""
        params: dict = self._prepare_query_search()
        if next_page_token:
            params["page"] = next_page_token
        if self.replication_key:
            params["sort"] = "asc"
            params["order_by"] = self.replication_key
        return params

    def _prepare_query_search(self) -> dict:
        """Return a dictionary with query params"""
        query_search = {}

        config_params = {
            "days_to_decrease_custom_data": "ref_date:start",
            "days_to_decrease_tasks": "updated_at:start",
            "days_to_decrease_kpis": "ref_date:start",
        }

        if self.days_to_decrease_config_name:
            params = config_params[self.days_to_decrease_config_name]
            query_search[params] = str(
                date.today()
                - timedelta(
                    days=int(self.config.get(self.days_to_decrease_config_name))
                )
            )
            query_search["limit"] = 10000
        return query_search
