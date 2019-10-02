import jsonschema
from jsonschema.validators import Draft7Validator
import simplejson as json
import os

if __name__ == '__main__':
    with open("schemas/definition.schema.json", 'r') as f:
        data = f.read()
        definition = json.loads(data)

    with open("schemas/evaluation.schema.json", 'r') as f:
        data = f.read()
        evaluation = json.loads(data)

    with open("schemas/input.schema.json", 'r') as f:
        data = f.read()
        input = json.loads(data)

    with open("schemas/preprocessing.schema.json", 'r') as f:
        data = f.read()
        preprocessing = json.loads(data)

    store = {
        "https://raw.githubusercontent.com/elastic/ml_json_schemas/master/schemas/definition.schema.json": definition,
        "https://raw.githubusercontent.com/elastic/ml_json_schemas/master/schemas/evaluation.schema.json": evaluation,
        "https://raw.githubusercontent.com/elastic/ml_json_schemas/master/schemas/input.schema.json": input,
        "https://raw.githubusercontent.com/elastic/ml_json_schemas/master/schemas/preprocessing.schema.json": preprocessing

    }

    full_path = os.path.join(os.path.dirname(__file__), "schemas")
    resolver = jsonschema.RefResolver(base_uri='file:' + full_path, referrer=None, store=store)
    validator = Draft7Validator(schema=definition, resolver=resolver)
    validator.check_schema(definition)

    with open("example.json", "r") as f:
        example_data = f.read()
    example = json.loads(example_data)

    validator.validate(example, definition)
