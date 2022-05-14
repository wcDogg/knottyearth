import csv
import json
from pathlib import Path
import configure


def csv_to_json_records(input, output):
  '''Converts CSV to JSON list of dictionaries (records format).
  * `input` - File path string
  * `output` - File path string
  '''
  data = None
  print(f'File in: %s' % input)

  try: 
    with Path(input).open('r', encoding='utf-8') as source:
      reader = csv.DictReader(source)
      data = [rows for rows in reader]

    with Path(output).open('w', encoding='utf-8') as save:
      save.write(json.dumps(data, indent=4))

    print(f'File out: %s' % output)

  except Exception as e:
    print(f'File error: %s' % input)
    print(e)
    return


# --------------------------------------
# Tasks
# --------------------------------------
csv_to_json_records(configure.CSV_THK, configure.JSON_THK)
csv_to_json_records(configure.CSV_FAN_2, configure.JSON_FAN_2)
csv_to_json_records(configure.CSV_FAN_3, configure.JSON_FAN_3)
csv_to_json_records(configure.CSV_FAN_4, configure.JSON_FAN_4)
csv_to_json_records(configure.CSV_FAN_5, configure.JSON_FAN_5)

