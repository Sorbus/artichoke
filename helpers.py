#-----------------------------------------------------------------------
# helper modules for argparse:
#  - check if values are in a certain range, are positive, etc.
#  - https://github.com/Sorbus/artichoke
#-----------------------------------------------------------------------

def check_range(value):
  ivalue = int(value)
  if ivalue < 1 or ivalue > 3200:
   raise argparse.ArgumentTypeError("%s is not a valid positive int value" % value)
  return ivalue    

def check_positive(value):
  ivalue = int(value)
  if ivalue < 0:
   raise argparse.ArgumentTypeError("%s is not a valid positive int value" % value)
  return ivalue  