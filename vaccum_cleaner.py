def agent_clean(agent_pos,clean_status):
  if agent_pos=="A" and clean_status[0]==0:
    agent_pos="B"
    print("Agent position "+agent_pos)
    print("Moving agent to position B")
    return
  if agent_pos=="A" and clean_status[0]==1:
    clean_status[0]=0
    print("Cleaning position A")
    agent_pos="B"
    print("Moving agent to position B")
    return
  if agent_pos=="B" and clean_status[1]==0:
    agent_pos="A"
    print("Moving agent to position A")
    return
  if agent_pos=="B" and clean_status[1]==1:
    clean_status[1]=0
    print("Cleaning position B")
    agent_pos="A"
    print("Moving agent to position A")
    return

def main():
  agent_pos="A"
  clean_status=[0,0]
  userInput=1
  while userInput==1:
    print("Enter the location\n A or B")
    loc=input()
    print("Status of the above location\n 0 for Clean or 1 for Dirty")
    cln=input()
    if loc=="A":
      print("Input loc"+loc)
      clean_status[0]=int(cln)
    elif loc=="B":
      print("Input loc"+loc)
      clean_status[1]=int(cln)
    while 1 in clean_status:
      print("Agent position "+agent_pos)
      agent_clean(agent_pos,clean_status)
    print("All positions are clean")
    print("Do you want to continue? 1 for yes")
    userInput=int(input())

main()
      
    
    
