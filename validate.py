import jsonschema
from jsonschema.validators import Draft4Validator
import simplejson as json
import os

if __name__ == '__main__':
    with open("schemas/model_definition.schema.json", 'r') as f:
        data = f.read()
        definition = json.loads(data)

    validator = Draft4Validator(schema=definition)
    validator.check_schema(definition)

    with open("examples/ensemble_example.json", "r") as f:
        example_data = f.read()
    ensemble_example = json.loads(example_data)
    validator.validate(ensemble_example, definition)

    with open("examples/tree_example.json", "r") as f:
        example_data = f.read()
    tree_example = json.loads(example_data)
    validator.validate(tree_example, definition)
