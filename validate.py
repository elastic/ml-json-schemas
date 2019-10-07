import jsonschema
from jsonschema.validators import Draft4Validator
import simplejson as json
import os

if __name__ == '__main__':
    with open("schemas/definition.schema.json", 'r') as f:
        data = f.read()
        definition = json.loads(data)

    with open("schemas/trained_model.schema.json", 'r') as f:
        data = f.read()
        trained_model = json.loads(data)

    with open("schemas/input.schema.json", 'r') as f:
        data = f.read()
        input = json.loads(data)

    with open("schemas/preprocessors.schema.json", 'r') as f:
        data = f.read()
        preprocessors = json.loads(data)

    store = {
        "https://raw.githubusercontent.com/elastic/ml_json_schemas/master/schemas/definition.schema.json": definition,
        "https://raw.githubusercontent.com/elastic/ml_json_schemas/master/schemas/trained_model.schema.json": trained_model,
        "https://raw.githubusercontent.com/elastic/ml_json_schemas/master/schemas/input.schema.json": input,
        "https://raw.githubusercontent.com/elastic/ml_json_schemas/master/schemas/preprocessors.schema.json": preprocessors

    }

    full_path = os.path.join(os.path.dirname(__file__), "schemas")
    resolver = jsonschema.RefResolver(base_uri='file:' + full_path, referrer=None, store=store)
    validator = Draft4Validator(schema=definition, resolver=resolver)
    validator.check_schema(definition)
    validator.check_schema(input)
    validator.check_schema(preprocessors)
    validator.check_schema(trained_model)

    with open("examples/ensemble_example.json", "r") as f:
        example_data = f.read()
    ensemble_example = json.loads(example_data)
    validator.validate(ensemble_example, definition)

    with open("examples/tree_example.json", "r") as f:
        example_data = f.read()
    tree_example = json.loads(example_data)
    validator.validate(tree_example, definition)
