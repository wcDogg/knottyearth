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
CSV_THK = Path(DIR_CSV / 'thk_reference_possible.csv')

# -----------------------------------
# Converted JSON Files
# -----------------------------------
JSON_THK = Path(DIR_JSON / 'thk_reference_possible.json')

# -----------------------------------
# Converted MD Tables
# -----------------------------------
TABLE_THK = Path(DIR_TEMP / 'thk-reference-tables.md')


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