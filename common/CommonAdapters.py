
from adapters.TfidfAdapter import TfidfAdapter

def get_exit_adapter(threshold: float):
    return TfidfAdapter.with_single_response(threshold, exit, set(["exit"]))