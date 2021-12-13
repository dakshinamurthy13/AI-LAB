def agent_clean(agent_pos, clean_status):
    if agent_pos == "A" and clean_status[0] == 0:
        # agent_pos="B"
        print("A is clean")
        print("Moving agent to position B")
        return "B"
    if agent_pos == "A" and clean_status[0] == 1:
        clean_status[0] = 0
        print("Cleaning position A")
        # agent_pos="B"
        print("Moving agent to position B")
        return "B"
    if agent_pos == "B" and clean_status[1] == 0:
        # agent_pos="A"
        print("B is clean")
        print("Moving agent to position A")
        return "A"
    if agent_pos == "B" and clean_status[1] == 1:
        clean_status[1] = 0
        print("Cleaning position B")
        # agent_pos="A"
        print("Moving agent to position A")
        return "A"


def main():
    agent_pos = "A"
    clean_status = [0, 0]
    userInput = 1
    while userInput == 1:
        i = 2
        print("Enter the location\nA or B")
        loc = input()
        print("Status of the above location\n0 for Clean or 1 for Dirty")
        cln = input()
        if loc == "A":
            # print("Input loc"+loc)
            clean_status[0] = int(cln)
        elif loc == "B":
            # print("Input loc"+loc)
            clean_status[1] = int(cln)
        while i > 0:
            print("Agent position " + agent_pos)
            agent_pos = agent_clean(agent_pos, clean_status)
            i -= 1
        print("All positions are clean")
        print("Do you want to continue? 1 for yes")
        userInput = int(input())


main()
