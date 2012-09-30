from temboo.Library.Twitter.Search import Query
from temboo.core.session import TembooSession

def searching(string):
    session = TembooSession(
        "alexandraorth",
        "myFirstApp",
        "d7be0cc1-7cdc-42c9-8"
        )
    choreo = Query(session)
    inputs = choreo.new_input_set()
    inputs.set_SinceId(249672500605222913)
    inputs.set_Query(string+" have my babies")
    results = choreo.execute_with_results(inputs)
    str = results.get_Response().encode('utf-8')
    num = str.count('statuses')
    return num