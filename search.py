from temboo.Library.Twitter.Search import Query
from temboo.core.session import TembooSession

session = TembooSession(
        "alexandraorth",
        "myFirstApp",
        "d7be0cc1-7cdc-42c9-8"
    )


# Instantiate the choreography, using a previously instantiated TembooSession object, eg:
# session = TembooSession('ACCOUNT_NAME', 'APP_KEY_NAME', 'APP_KEY_VALUE')
choreo = Query(session)

# Get an InputSet object for the choreo
inputs = choreo.new_input_set()

# Set inputs
inputs.set_Query("Justin Bieber have my babies")

# Execute choreo
results = choreo.execute_with_results(inputs)

print results.get_Response().encode('utf-8')
