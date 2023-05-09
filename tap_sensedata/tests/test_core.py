"""Tests standard tap features using the built-in SDK tests library."""

from os import environ as env

from singer_sdk.testing import get_standard_tap_tests

from tap_sensedata.tap import Tapsensedata

SAMPLE_CONFIG = {
    "start_date": env["TAP_SENSEDATA_START_DATE"],
    "auth_token": env["TAP_SENSEDATA_AUTH_TOKEN"],
}


def test_standard_tap_tests():
    """Run standard tap tests from the SDK."""
    tests = get_standard_tap_tests(Tapsensedata, config=SAMPLE_CONFIG)

    for test in tests:
        test()
