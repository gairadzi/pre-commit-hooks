import yaml
from jsonschema import validate
from jsonschema.exceptions import ValidationError


def main(argv):
    retval = 0
    with open('k8s/webservers.yaml') as file:
        obj = yaml.safe_load(file)

    with open('k8s/webservers_schema.yaml') as file:
        schema = yaml.safe_load(file)

    try:
        validate(obj, schema=schema)
    except ValidationError as err:
        print(f"Failed to validate '{obj}'")
        print(f"  message: {err.message}")
        print(f"  cause: {err.cause}")
        print(f"  instance: {err.instance}")
        print(f"  path: {err.path}")
        print(f"  issue: {err.path[-1]}")
        print(f"  schema_path: {err.schema_path}")
        retval = 1

    return retval


if __name__ == '__main__':
    raise SystemExit(main())
