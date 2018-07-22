 from pandas.io.json import json_normalize
 import json
 
 
 def jsonToDf():
    response = fetch_json() # e.g - from a web service call
    json_response = json.loads(response.text)
    response_df = pd.read_json(json.dumps(json_response))
    
 def complexJsonToDf():
    response = fetch_json() # e.g - from a web service call
    json_response = json.loads(response.text)
    response_df = json_normalize(json_response)
 
