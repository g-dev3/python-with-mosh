high_income = False
good_credit = True

if high_income and good_credit:
  print("Eligible for loan")


if high_income or good_credit:
  print("Eligible for loan")

has_good_income = True
has_criminal_record = False

if has_good_income  and not has_criminal_record:
  print("Eligible for loan")