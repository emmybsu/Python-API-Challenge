# def parrot_trouble(talking, hour):
#   if talking and hour <7 or >20:
#     return True and hour
#   else:
#     return False and hour
    

def parrot_trouble(talking, hour):
  return (talking and (hour < 7 or hour > 20))
parrot_trouble
