from pandasdmx import Request
import pandasdmx as sdmx
from pathlib import Path

# Show http traces.
import http.client as http_client
import logging

from samples import *

http_client.HTTPConnection.debuglevel = 2
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True

log = logging.getLogger()


istat = Request("ISTAT")
res = istat.data(
    #    agency="IT1",
    resource_id="115_333",
    params={"startPeriod": "2000"},
    key={"ADJUSTMENT": ["N", "Y"]},
)


def sdmx_devel():
    df = istat.data(resource_id="122_54", params={"startPeriod": "2019-01"},)
    pdf = smdx.to_pandas(df)
    pdf = smdx.to_pandas(df)
