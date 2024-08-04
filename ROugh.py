# # Assignment - 2
# # Name -
# # Roll No -
import json

# '''
# - This is the skeleton code, wherein you have to write the logic for each of the
# functions defined below.

# - DO NOT modify/delete the given functions.

# - DO NOT import any python libraries, except for the ones already included.

# - DO NOT create any global variables in this module.

# - DO NOT add print statements anywhere in this module.

# - Make sure to return value as specified in the function description.

# - Remove the pass statement from the functions when you implement them.
# '''


def read_data_from_file(file_path="ASSIGNMENT 2\data.json"):
    '''
    **** DO NOT modify this function ****
    Description: Reads the data.json file, and converts it into a dictionary.

    Parameters:
    - file_path (STRING): The path to the file (with .json extension) which contains the initial database. You can pass the file_path parameter as "data.json".

    Returns:
    - A dictionary containing the data read from the file
    '''

    with open(file_path, 'r') as data:
        records = json.load(data)

    return records


# def is_related(records, person_id_1, person_id_2):
#     '''
#     **** BONUS QUESTION ****
#     Description: Check if 2 persons are friends

#     Parameters:
#     - records (LIST): A list of person records (each of which is a dictionary)
#     - person_id_1 (INTEGER): first person ID
#     - person_id_2 (INTEGER): second person ID

#     Returns:
#     - A BOOLEAN denoting if the persons are friends of each other, directly or indirectly (if A knows B, B knows C and C knows D, then A knows B, C and D).
#     '''
#     boolean = ''
#     ls = []

#     for data in records:

#         if person_id_1 == data['id']:
#             if person_id_2 in data['friend_ids']:
#                 boolean = True

#         if person_id_2 == data['id']:
#             if person_id_1 in data['friend_ids']:
#                 boolean = True

#         elif person_id_1 == data['id']:
#             for x in data['friend_ids']:

#                 if data['id'] == x:
#                     print('True')
#                     print(data['friend_ids'])
#                     if person_id_2 in data['friend_ids']:
#                         boolean = True
#                     else:
#                         is_related(records, x, person_id_2)

#     return boolean


# is_related(read_data_from_file(), 0, 7)


def find_topper_of_each_institute(records):
    '''
    Description: Find topper of each institute

    Parameters:
    - records (LIST): A list of person records (each of which is a dictionary)

    Returns:
    - A DICTIONARY with the institute name (STRING) as the keys and the ID (INTEGER) of the topper of that institute.

    Note: If there are `N` distinct institutes in records, the dictionary will contain `N` key-value pairs. The ongoing status does NOT matter. It is guaranteed that each institute will have exactly one topper.
    '''
    dic = {}
    tp1 = []
    tp2 = []

    for data in records:

        for inst in (data['education']):
            if inst['ongoing'] == False:

                tp1.append([inst['institute'], data['id'], inst['percentage']])
                tp2.append([inst['institute'], data['id'], inst['percentage']])

    for j in tp1:

        for i in tp2:
            if i[0] == j[0] and i[2] > j[2]:
                if i[2] < j[2]:
                    i[2] = j[2]

                    dic.update({i[0]: i[1]})

            # if i[0] == j[0] and j[2] > i[2]:

            #     dic.update({i[0]: i[1]})
    print(dic)


find_topper_of_each_institute(read_data_from_file())
