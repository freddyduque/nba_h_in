import json, requests

def sort_by_key(list):
  return list['h_in']

def get_pairs():
  response1 = requests.get("https://mach-eight.uc.r.appspot.com/") # get json from API
  if response1.status_code != 200:
    print(f"Error: {response1.status_code}: {response1.reason}")
    return
  
  # Testing Scenarios:
  json_data1 = json.loads(response1.text)["values"] # load text to json
  #json_data1 = [{"first_name":"Alex","h_in":"77","h_meters":"1.96","last_name":"Acker"},{"first_name":"Hassan","h_in":"76","h_meters":"1.93","last_name":"Adams"},{"first_name":"Arron","h_in":"77","h_meters":"1.96","last_name":"Afflalo"},{"first_name":"Maurice","h_in":"77","h_meters":"1.96","last_name":"Ager"},{"first_name":"Alexis","h_in":"84","h_meters":"2.13","last_name":"Ajinca"},{"first_name":"LaMarcus","h_in":"83","h_meters":"2.11","last_name":"Aldridge"},{"first_name":"Joe","h_in":"80","h_meters":"2.03","last_name":"Alexander"},{"first_name":"Malik","h_in":"82","h_meters":"2.08","last_name":"Allen"},{"first_name":"Ray","h_in":"77","h_meters":"1.96","last_name":"Allen"},{"first_name":"Tony","h_in":"76","h_meters":"1.93","last_name":"Allen"},{"first_name":"Morris","h_in":"78","h_meters":"1.98","last_name":"Almond"},{"first_name":"Rafer","h_in":"74","h_meters":"1.88","last_name":"Alston"},{"first_name":"Louis","h_in":"81","h_meters":"2.06","last_name":"Amundson"},{"first_name":"Chris","h_in":"82","h_meters":"2.08","last_name":"Andersen"},{"first_name":"Ryan","h_in":"82","h_meters":"2.08","last_name":"Anderson"}]
  #json_data1 = [{"first_name":"Alex","h_in":"77","h_meters":"1.96","last_name":"Acker"},{"first_name":"Hassan","h_in":"76","h_meters":"1.93","last_name":"Adams"}]
  #json_data1 = [{"first_name":"Alex","h_in":"77","h_meters":"1.96","last_name":"Acker"}]
  #json_data1 = []

  if len(json_data1) == 0:
    print("No players in the list, can't perform operation, please try again later when list is updated with NBA players")
    return
  elif len(json_data1) == 1:
    print("Only 1 player in the list, can't perform operation, please try again later when list is updated with more NBA players")
    return
  else:
    again = True
    # sort dictionary
    sorted_list = (sorted(json_data1 , key = sort_by_key))

    if len(json_data1) == 2:
      min_val = min_val = int(sorted_list[0]["h_in"])+int(sorted_list[1]["h_in"])    
    else:
      # calc max and min
      min_val = int(sorted_list[0]["h_in"])+int(sorted_list[1]["h_in"])
      max_val = int(sorted_list[-1]["h_in"])+int(sorted_list[-2]["h_in"])

  while again: # Loop and ask if want to check again or not
    check = True
    try:
      value = int(input(f"Please input the height that adds up to 2 players (MIN: {min_val}; MAX: {max_val}): "))
    except ValueError:
      print("INT values only, try again")
      check = False

    if check:
      found = False
      if value >= min_val and value <= max_val: # Check border values
        length = len(sorted_list)
        for index1 in range(0,length): # traverse 1 by 1
          h_in1 = int(sorted_list[index1]['h_in'])
          expecting_in = value - h_in1
          if h_in1 > expecting_in: # because it's sorted, if current inch is higher that the expecting value, that means there's no other available value, then break
            break
          for index2 in range(index1+1,length):
            h_in2 = int(sorted_list[index2]['h_in'])
            if h_in2 > expecting_in or expecting_in > int(sorted_list[-1]["h_in"]): # because it's sorted, if current inch is higher that the expecting value, that means there's no other available value, then break
              break
            elif expecting_in == h_in2:
              # print(f"{h_in1}:{sorted_list[index1]['first_name']} {sorted_list[index1]['last_name']}\t{h_in2}:{sorted_list[index2]['first_name']} {sorted_list[index2]['last_name']} = {h_in1 + expecting_in}") # Testing output
              print(f"- {sorted_list[index1]['first_name']} {sorted_list[index1]['last_name']} ({h_in1}in)\t\t{sorted_list[index2]['first_name']} {sorted_list[index2]['last_name']} ({h_in2}in)")
              found = True
      if not found:
        print("No matches found")

      if input("Want to try again? exit(N): ").upper() == "N":
        again = False

get_pairs()