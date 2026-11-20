import re


def extract_tables(sql_text: str):
    pattern = r"CREATE\s+TABLE\s+(\w+)"

    tables = re.findall(
        pattern,
        sql_text,
        flags=re.IGNORECASE
    )

    return tables


def extract_schema(sql_text: str):

    table_pattern = r"CREATE\s+TABLE\s+(\w+)\s*\((.*?)\);"

    matches = re.findall(
        table_pattern,
        sql_text,
        flags=re.IGNORECASE | re.DOTALL
    )

    schema = {}

    for table_name, body in matches:

        columns = []

        for line in body.split(","):

            line = line.strip()

            if not line:
                continue

            parts = line.split()

            if len(parts) == 0:
                continue

            column_name = parts[0]

            columns.append(column_name)

        schema[table_name] = columns

    return schema
def infer_relationships(schema):

    relationships = []

    for table_name, columns in schema.items():

        for column in columns:

            if not column.endswith("_id"):
                continue

            parent_name = column[:-3]

            candidate_tables = [
                parent_name,
                parent_name + "s"
            ]

            for candidate in candidate_tables:

                if candidate in schema:

                    relationships.append(
                        {
                            "from_table": table_name,
                            "from_column": column,
                            "to_table": candidate,
                            "to_column": "id"
                        }
                    )

                    break

    return relationships