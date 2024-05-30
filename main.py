import datetime

try:
  f = open("log.txt","a")
  try:
    TimeNow = datetime.datetime.now()
    f.write(f"\n{TimeNow}")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")