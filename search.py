from temboo.Library.Twitter.Search.SearchFilter import SearchFilter
from temboo.core.session import TembooSession

session = TembooSession(
        "alexandraorth",
        "myFirstApp",
        "d7be0cc1-7cdc-42c9-8"
    )

twitterSearch = SearchFilter(session)
inputs = twitterSearch.new_input_set()
inputs.set_SearchString("Justin Bieber have my babies")
inputs.set_Filter("Costello")
inputs.set_ResultsPerPage(10)
results = twitterSearch.execute_with_results(inputs)
print results.get_Response().encode('utf-8')
