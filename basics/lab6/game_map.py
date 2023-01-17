# This function returns the game map to be used in the game
# 
# The 'task' parameter specifies the task (or custom) the map is from
# The 'map_number' parameter specifies the map to use within the task
def getGameMap(task, map_number):
    # Return the requested map
    if task == "task0":
        return task0[map_number], None
    if task == "task1":
        return task1[map_number], None
    if task == "task2":
        return task2[map_number], None
    if task == "task3":
        return task3[map_number], None
    if task == "task4":
        return task4[map_number], None
    if task == "custom":
        return custom_map[map_number], custom_map_for_task
    else:
        # If the task is unknown, we set it to be task0
        return task0[map_number], None

#####
# You can see the map definitions from the following lists
#
# You can add custom maps in the list near the bottom of this file
#####

# Maps for task 0
task0 = [
# Map 0
"""\
BBBBBEBBBBBBBBBBBB
B                B
B    P           B
B                B
B                B
B                B
B                B
B                B
B                B
B                B
B                B
B                B
B                B
B                B
B                B
B                B
B                B
BBBBBBBBBBBBBBBBBB""",

# Map 1
"""\
BBBBBBBBBBEBBBBBBB
B                B
B                B
B                B
B         P      B
B                B
B                B
B                B
B                B
B                B
B                B
B                B
B                B
B                B
B                B
B                B
B                B
BBBBBBBBBBBBBBBBBB""",

# Map 2
"""\
BBBBBBBBBBBBBEBBBB
B                B
B                B
B                B
B                B
B                B
B                B
B                B
B                B
B                B
B                B
B                B
B                B
B            P   B
B                B
B                B
B                B
BBBBBBBBBBBBBBBBBB"""
]

# Maps for task 1
task1 = [
# Map 0
"""\
BBBBBEBBBBBBBBBBBB
B                B
B   P            B
B                B
B                B
B                B
B                B
B                B
B                B
B                B
B                B
B                B
B                B
B                B
B                B
B                B
B                B
BBBBBBBBBBBBBBBBBB""",

# Map 1
"""\
BBBBBBBBBBEBBBBBBB
B                B
B                B
B                B
B  P             B
B                B
B                B
B                B
B                B
B                B
B                B
B                B
B                B
B                B
B                B
B                B
B                B
BBBBBBBBBBBBBBBBBB""",

# Map 2
"""\
BBBBBBBBBBBBBEBBBB
B                B
B                B
B                B
B                B
B                B
B                B
B                B
B                B
B                B
B                B
B                B
B                B
B      P         B
B                B
B                B
B                B
BBBBBBBBBBBBBBBBBB"""
]

# Maps for task 2
task2 = [
# Map 0
"""\
BBBBBEBBBBBBBBBBBB
B                B
B                B
B                B
B                B
B                B
B                B
B                B
B          P     B
B                B
B                B
B                B
B                B
B                B
B                B
B                B
B                B
BBBBBBBBBBBBBBBBBB""",

# Map 1
"""\
BBBBBBBBBEBBBBBBBB
B                B
B                B
B                B
B                B
B                B
B                B
B                B
B       P        B
B                B
B                B
B                B
B                B
B                B
B                B
B                B
B                B
BBBBBBBBBBBBBBBBBB""",

# Map 2
"""\
BBBBBBBBBBBBBEBBBB
B                B
B                B
B                B
B                B
B                B
B                B
B                B
B                B
B                B
B                B
B                B
B                B
B          P     B
B                B
B                B
B                B
BBBBBBBBBBBBBBBBBB"""
]

# Maps for task 3
task3 = [
# Map 0
"""\
BBBBBEBBBBBBBBBBBB
B                B
B                B
B                B
B                B
B                B
B                B
B                B
BBBBBBBBBBBBB BBBB
B                B
B                B
B        P       B
B                B
B                B
B                B
B                B
B                B
BBBBBBBBBBBBBBBBBB""",

# Map 1
"""\
BBBBBBBBBBBBBEBBBB
B                B
B                B
BBBBBBBBBBBBB BBBB
B                B
B                B
BBBBB BBBBBBBBBBBB
B                B
B                B
BBBBBBBBBBBBB BBBB
B                B
B                B
BBBBBBB BBBBBBBBBB
B                B
B                B
B                B
B       P        B
BBBBBBBBBBBBBBBBBB""",

# Map 2
"""\
BBBBBEBBBBBBBBBBBB
B                B
B                B
BBBBBBBBBBBBB BBBB
B                B
BBBBB BBBBBBBBBBBB
B                B
B                B
BBBBBBBBBBBBB BBBB
B                B
B                B
BBBBBBB BBBBBBBBBB
B                B
BBBBBBBBB BBBBBBBB
B                B
BBBBBBBBBBBBBBBB B
B       P        B
BBBBBBBBBBBBBBBBBB"""
]

# Maps for task 4
task4 = [
# Map 0
"""\
BBBBBBBBBBBBBBBBBBB
B B       B       B
B B BBB B BBB BBBBB
B   B   B     B   B
B BBB BBB BBBBB B B
B B   B B B  P  B B
B B BBB B B BBBBB B
B B B     B B   B B
B B BBBBBBB B BBB B
B B     B   B     B
B BBBBB BBBBB BBBBB
B   B   B     B   B
BBB B B B BBBBBBB B
B B B B B B     B B
B B B BBB B BBB B B
B B B   B B   B   B
B B BBB B BBB BBB B
E     B       B   B
BBBBBBBBBBBBBBBBBBB""",

# Map 1
"""\
BBBBBBBBBBBBBBBBBBB
B       B     B   B
BBB BBB BBB B B B B
B   B B   B B   B B
B BBB BBB B BBBBB B
B   B   B B   B   B
BBB B B B BBBBB BBB
B   B B       B   B
B BBBBBBBBBBB BBB B
B   B     B B   B B
B B B BBBBB BBB B B
B B B B B     B   B
B B B B BPBBB BBB B
B B B B   B B     B
BBB B B BBB BBBBBBB
B   B B B       B B
B BBB B BBB BBB B B
B     B     B     E
BBBBBBBBBBBBBBBBBBB"""
]

custom_map_for_task = "task4"
custom_map = [ """\
BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB
B     B     B       B         B       B
B B B B B BBB B BBB BBBBB B BBB BBBBB B
B B B B B B   B B B B   B B   B     B B
BBB B B B B BBB B B B B BBBBB BBBBB B B
B   B B B   B   B B   B     B       B B
B BBB B BBBBB BBB BBBBBBBBB BBB BBBBB B
B B B B   B B B           B   B B     B
B B B BBB B B B BBBBB BBB BBB B B BBB B
B B B B   B B B     B   B   B B B B B B
B B B B BBB B BBBBBBB B BBBBB BBB B B B
B B   B     B       B B           B B B
B BBBBBBB BBBBB BBB BBBBB BBBBBBBBB B B
B         B   B   B B   B     B   B   B
BBBBBBBBBBB B BBBBB B B BBBBB B B B BBB
B   B     B B       B B     B B B B   B
B B B BBB B BBBBBBB B BBBBB BBB B BBBBB
B B   B B   B   B   B     B B   B     B
B BBBBB B BBB B BBBBB BBB B B BBBBBBB B
B   B     B   B B   B B   B B B   B   B
B B BBBBB B BBB B BBBBB BBB B B B B BBB
B B     B B   B   B   B   B   B B B B B
B BBBBB B BBB BBBBB B B B BBBBBPB B B B
B B   B B B   B     B B B   B   B   B B
B BBB B BBB BBBBBBB B BBBBB B BBBBBBB B
B B   B B   B       B       B B       B
B B BBB B BBB BBBBBBBBBBBBBBB BBEBBBB B
B B B   B B   B       B     B   B   B B
B B B BBB B BBB BBBBB B BBBBBBB B B B B
B   B   B   B   B     B       B   B B B
BBB BBB BBBBB B B BBBBB BBBBB BBBBB B B
B   B   B   B B B B   B B         B   B
B BBB B B BBB B B B B BBB BBBBBBB BBB B
B   B B   B   B B   B     B       B   B
BBBBB BBBBB BBB BBBBBBBBB BBBBB BBB BBB
B     B     B B B   B     B   B   B   B
B BBBBB BBBBB B B B BBBBBBB B BBBBBBB B
B             B   B         B         B
BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB"""
]
