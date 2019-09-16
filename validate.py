from jsonschema import validate
import simplejson as json

if __name__ == '__main__':
    with open("schemas/definition.schema.json", 'r') as f:
        schema_data = f.read()
    schema = json.loads(schema_data)

    with open("example.json", "r") as f:
        example_data = f.read()
    example = json.loads(example_data)

    validate(example, schema)
