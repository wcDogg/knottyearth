from pathlib import Path

# -----------------------------------
# Project Directories
# -----------------------------------
DIR_PROJECT = Path(__file__).parent.parent
DIR_TEMP = Path(DIR_PROJECT / 'temp')
DIR_IMAGES = Path(DIR_PROJECT / 'assets')
DIR_CSV = Path(DIR_PROJECT / 'files')
DIR_JSON = Path(DIR_PROJECT / 'files')
DIR_MD_THK = Path(DIR_PROJECT / 'thk')
DIR_MD_FAN = Path(DIR_PROJECT / 'fan')
DIR_MD_PK = Path(DIR_PROJECT / 'pk')

# -----------------------------------
# CSV Source Files
# -----------------------------------
CSV_THK = Path(DIR_CSV / 'thk_reference.csv')
CSV_FAN_2 = Path(DIR_CSV / 'fan_reference_2-strand.csv')
CSV_FAN_3 = Path(DIR_CSV / 'fan_reference_3-strand.csv')
CSV_FAN_4 = Path(DIR_CSV / 'fan_reference_4-strand.csv')
CSV_FAN_5 = Path(DIR_CSV / 'fan_reference_5-strand.csv')


# -----------------------------------
# Converted JSON Files
# -----------------------------------
JSON_THK = Path(DIR_JSON / 'thk_reference.json')
JSON_FAN_2 = Path(DIR_JSON / 'fan_reference_2-strand.json')
JSON_FAN_3 = Path(DIR_JSON / 'fan_reference_3-strand.json')
JSON_FAN_4 = Path(DIR_JSON / 'fan_reference_4-strand.json')
JSON_FAN_5 = Path(DIR_JSON / 'fan_reference_5-strand.json')


# -----------------------------------
# Converted MD Tables
# -----------------------------------
MD_THK = Path(DIR_TEMP / 'thk-reference.md')
MD_FAN_2 = Path(DIR_TEMP / 'fan-reference-2-strand.md')
MD_FAN_3 = Path(DIR_TEMP / 'fan-reference-3-strand.md')
MD_FAN_4 = Path(DIR_TEMP / 'fan-reference-4-strand.md')
MD_FAN_5 = Path(DIR_TEMP / 'fan-reference-5-strand.md')



# -----------------------------------
# Test
# -----------------------------------
def print_dirs():

  print(DIR_PROJECT)
  print(DIR_IMAGES)
  print(DIR_CSV)
  print(DIR_JSON)
  print(DIR_MD_THK)
  print(DIR_MD_FAN)
  print(DIR_MD_PK)

#print_dirs()