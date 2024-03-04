def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    result_list = list()
    for name in names:
        result_list.append(f"Hello, my name is {name}.")
    return result_list

def assign_rooms(names):
    room = 1
    result_list = list()
    for name in names:
        result_list.append(f"Hello, {name}! You'll be assigned to room {room}!")
        room+=1
    return result_list

def printer(names):
    batch_list = batch_badge_creator(names)
    room_list = assign_rooms(names)
    count_batch = 0
    count_room = 0
    for name in names:
        print(batch_list[count_batch])
        count_batch+=1
        
    for name in names:
        print(room_list[count_room])
        count_room+=1

printer(["Arel", "Carol"])