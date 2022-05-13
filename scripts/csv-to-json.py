import json
import csv
from pathlib import Path
import configure


def csv_to_list_of_dicts(input,output):
  '''Converts CSV to JSON list of dictionaries.
  '''
  data = []

  try: 
    with Path(input).open('r', encoding='utf-8') as source:
      reader = csv.DictReader(source)

      for rows in reader:
        data.append(rows)

    with Path(output).open('w', encoding='utf-8') as save:
      save.write(json.dumps(data, indent=4))

  except Exception as e:
    print(f'Oops!: %s' % e)


# -----------------------------------
# Tasks
# -----------------------------------   
csv_to_list_of_dicts(configure.CSV_THK, configure.JSON_THK)


