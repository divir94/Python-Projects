from jsonschema import validate
import json
from pprint import pprint

true, false, null = True, False, None

json_data=open('json_data')

data = json.load(json_data)
pprint(data)

json_data.close()


#print validate(config, schema)
