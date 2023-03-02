import random as rd

def with_absent_num():
    try:
        size = int(input("\nThe total number of objects: "))
        group_member = int(input("Number of objects/group: "))

        if(group_member > size):
            print("Too few objects!!!\n")
            with_absent_num()

    except ValueError:
        print("Please enter a number!!!")
        with_absent_num()
    else:
        members = [x for x in range(1,size+1)]
        member_size = len(members)

    total_group = round(member_size/group_member)
    print("\nThe total number of groups:",total_group,"\n")

    group = []
    choosed = []

    def manage_data(group, choosen, choosed):
        group.append(choosen)  
        choosed.append(choosen) 
        members.remove(choosen)
        
    for x in range(1,total_group):
        enough = False
        while not enough:
            choosen = rd.choice(members)
            if len(members) >= group_member:
                if choosen not in choosed:
                    manage_data(group=group,choosen=choosen,choosed=choosed)             
                if len(group) == group_member:
                    enough = True
            else:
                manage_data(group=group,choosen=choosen,choosed=choosed)
                enough = True

        print(f"Group {x}\t= {group} - {len(group)} members")
        # Reset the group
        group = []
    print(f"Last Group: {members} - {len(members)} members")

is_on = True
while is_on:
    with_absent_num()
    stay = input("\nn/N for exit: ").lower()
    if stay == "n":
        is_on = False