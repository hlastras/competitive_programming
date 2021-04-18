import sys
import re

lines = sys.stdin.read().strip().split("\n\n")

def parse_passport(line):
  line = line.replace("\n", " ")
  result = {}
  for kv in line.split(" "):
    key, value = kv.split(":")
    result[key] = value
  return result

def validate_passport(passport):
  valid = True
  valid &= validate_birth_year(passport)
  valid &= validate_issue_year(passport)
  valid &= validate_expiration_year(passport)
  valid &= validate_height(passport)
  valid &= validate_hair_colour(passport)
  valid &= validate_eye_colour(passport)
  valid &= validate_passport_id(passport)
  return valid

def is_integer(s):
  try: 
    int(s)
    return True
  except ValueError:
    return False

def is_integer_between_values(string, minimum, maximum):
  if is_integer(string):
    value = int(string)
    if value >= minimum and value <= maximum:
      return True
  return False

def validate_birth_year(passport):
  if "byr" in passport:
    return is_integer_between_values(passport["byr"], 1920, 2002)
  return False

def validate_issue_year(passport):
  if "iyr" in passport:
    return is_integer_between_values(passport["iyr"], 2010, 2020)
  return False

def validate_expiration_year(passport):
  if "eyr" in passport:
    return is_integer_between_values(passport["eyr"], 2020, 2030)
  return False

def validate_height(passport):
  if "hgt" in passport:
    hgt = passport["hgt"]
    if hgt.endswith("cm"):
      value = int(hgt[:-2])
      if value >= 150 and value <= 193:
        return True
    elif hgt.endswith("in"):
      value = int(hgt[:-2])
      if value >= 59 and value <= 76:
        return True
  return False

def validate_hair_colour(passport):
  if "hcl" in passport:
    match = re.search(r'^#[0-9a-fA-F]{6}$', passport["hcl"])
    if match:                      
      return True
  return False

def validate_eye_colour(passport):
  valid_colours = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
  if "ecl" in passport:
    if passport["ecl"] in valid_colours:
      return True
  return False

def validate_passport_id(passport):
  if "pid" in passport:
    match = re.search(r'^[0-9]{9}$', passport["pid"])
    if match:                      
      return True
  return False


total = 0
for line in lines:
  passport = parse_passport(line)
  is_valid = validate_passport(passport)
  if is_valid:
    total += 1

print(total)