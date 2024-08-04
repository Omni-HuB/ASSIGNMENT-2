# Assignment - 2
# Name - MOHAMMAD SHARIQ
# Roll No - 2020220

import json

'''
- This is the skeleton code, wherein you have to write the logic for each of the
functions defined below.

- DO NOT modify/delete the given functions.

- DO NOT import any python libraries, except for the ones already included.

- DO NOT create any global variables in this module.

- DO NOT add print statements anywhere in this module.

- Make sure to return value as specified in the function description.

- Remove the pass statement from the functions when you implement them.
'''


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


def filter_by_first_name(records, first_name):
    '''
    Description: Searches the records to find all persons with the given first name (case-insensitive)

    Parameters:
    - records (LIST): A list of person records (each of which is a dictionary)
    - first_name (STRING): The first name

    Returns:
    - A list of INTEGERS denoting the IDs of the persons with the given first name
            Case 1: No person found => Returns an empty list
            Case 2: At least one person found => Returns a list containing the IDs of all the persons found
    '''
    ls0 = []
    for data in records:
        f = first_name[0].upper()+first_name[1:]
        if data['first_name'] == f:
            ls0.append(data.get('id'))
        else:
            list()

    return(ls0)


def filter_by_last_name(records, last_name):
    '''
    Description: Searches the records to find all persons with the given last name (case-insensitive)

    Parameters:
    - records (LIST): A list of person records (each of which is a dictionary)
    - last_name (STRING): The last name

    Returns:
    - A list of INTEGERS denoting the IDs of the persons with the given last name
            Case 1: No person found => Returns an empty list
            Case 2: At least one person found => Returns a list containing the IDs of all the persons found
    '''
    ls1 = []
    for data in records:
        l = last_name[0].upper()+last_name[1:]
        if data['last_name'] == l:
            ls1.append(data.get('id'))
        else:
            list()
    return(ls1)


def filter_by_full_name(records, full_name):
    '''
    Description: Searches the records to find all persons with the given full name (case-insensitive)

    Parameters:
    - records (LIST): A list of person records (each of which is a dictionary)
    - full_name (STRING): The full name (a single string with 2 space-separated words, the first name and the last name respectively)

    Returns:
    - A list of INTEGERS denoting the IDs of the persons with the given full name
            Case 1: No person found => Returns an empty list
            Case 2: At least one person found => Returns a list containing the IDs of all the persons found
    '''

    ls2 = []
    fn = full_name.split(' ')
    fin = fn[0]
    fin = fin[0].upper()+fin[1:]
    lin = fn[1]
    lin = lin[0].upper()+lin[1:]
    fullname = fin+' '+lin

    for data in records:

        if (data['first_name']+' '+data['last_name']) == fullname:
            ls2.append(data.get('id'))
        else:
            list()

    return ls2


def filter_by_age_range(records, min_age, max_age):
    '''
    Description: Searches the records to find all persons whose age lies in the given age range [min_age, max_age]

    Parameters:
    - records (LIST): A list of person records (each of which is a dictionary)
    - min_age (INTEGER): The minimum age (inclusive)
    - max_age (INTEGER): The maximum age (inclusive)

    Note: 0 < min_age <= max_age

    Returns:
    - A list of INTEGERS denoting the IDs of the persons with the given full name
            Case 1: No person found => Returns an empty list
            Case 2: At least one person found => Returns a list containing the IDs of all the persons found
    '''
    ls3 = []
    for data in records:
        if data['age'] in range(min_age, max_age+1):
            ls3.append(data.get('id'))
        else:
            list()

    return(ls3)


def count_by_gender(records):
    '''
    Description: Counts the number of males and females

    Parameters:
    - records (LIST): A list of person records (each of which is a dictionary)

    Returns:
    - A dictionary with the following two key-value pairs:
            KEY        VALUE
            "male"     No of males (INTEGER)
            "female"   No of females (INTEGER)
    '''
    countm = 0
    countf = 0
    dic = {}
    for data in records:
        if data['gender'] == 'male':
            countm += 1

        elif data['gender'] == 'female':
            countf += 1

    dic.update({"male": countm})
    dic.update({'female': countf})

    return(dic)


def filter_by_address(records, address):
    '''
    Description: Filters the person records whose address matches the given address.

    Parameters:
    - records (LIST): A list of person records (each of which is a dictionary)
    - address (DICTIONARY): The keys are a subset of { "house_no", "block", "town", "city", "state", "pincode" } (case-insensitive)
            Some examples are:
                    Case 1: {}
                            => All records match this case

                    Case 2: { "block": "AD", "city": "Delhi" }
                            => All records where the block is "AD" and the city is "Delhi" (the remaining address fields can be anything)

                    Case 3: { "house_no": 24, "block": "ABC", "town": "Vaishali", "city": "Ghaziabad", "state": "Uttar Pradesh", "pincode": 110020 }

    Returns:
    - A LIST of DICTIONARIES with the following two key-value pairs:
            KEY            VALUE
            "first_name"   first name (STRING)
            "last_name"    last name (STRING)
    '''
    pass


def find_alumni(records, institute_name):
    '''
    Description: Find all the alumni of the given institute name (case-insensitive).

    Note: A person is an alumnus of an institute only if the value of the "ongoing" field for that particular institute is False.

    Parameters:
    - records (LIST): A list of person records (each of which is a dictionary)
    - institute_name (STRING): Name of the institute (case-insensitive)

    Returns:
    - A LIST of DICTIONARIES with the following three key-value pairs:
            KEY            VALUE
            "first_name"   first name (STRING)
            "last_name"    last name (STRING)
            "percentage"   percentage (FLOAT)
    '''
    ls = []
    institute_name = institute_name.upper()

    for data in records:
        for inst in (data['education']):
            if inst['ongoing'] == False and institute_name in inst['institute']:

                ls.append(
                    {'first_name': data['first_name'], 'last_name': data['last_name'], 'percentage': inst['percentage']})

    return(ls)


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

                dic.update({i[0]: i[1]})

            if i[0] == j[0] and j[2] > i[2]:

                dic.update({i[0]: i[1]})
    return dic


def find_blood_donors(records, receiver_person_id):
    '''
    Description: Find all donors who can donate blood to the person with the given receiver ID.

            Note:
            - Possible blood groups are "A", "B", "AB" and "O".

            Rules:
            BLOOD GROUP      CAN DONATE TO
            A                A, AB
            B                B, AB
            AB               AB
            O                A, B, AB, O

    Parameters:
    - records (LIST): A list of person records (each of which is a dictionary)
    - receiver_person_id (INTEGER): The ID of the donee
            Note: It is guaranteed that exactly one person in records will have the ID as receiver_person_id

    Returns:
    - A DICTIONARY with keys as the IDs of potential donors and values as a list of strings, denoting the contact numbers of the donor
    '''
    for data in records:
        if data['id'] == receiver_person_id:
            x = data['blood_group']

    lsA = []
    lsB = []
    lsO = []
    lsAB = []
    ls1 = []
    dic = {}

    x = x.upper()
    for data in records:

        if(data['blood_group'] == 'A'):

            lsA.append([data['id'], data['contacts']])

        if(data['blood_group'] == 'O'):

            lsO.append([data['id'], data['contacts']])

        if(data['blood_group'] == 'AB'):

            lsAB.append([data['id'], data['contacts']])

        if(data['blood_group'] == 'B'):

            lsB.append([data['id'], data['contacts']])

    if x == "A":
        ls1 = lsO+lsA
        ls1.sort()

    if x == 'B':
        ls1 = lsB+lsO
        ls1.sort()

    if x == 'AB':
        ls1 = lsAB+lsO+lsA+lsB
        ls1.sort()

    if x == 'O':
        ls1 = lsO
        ls1.sort()

    for i in ls1:
        dic.update({i[0]: i[1]})

    return(dic)


def get_common_friends(records, list_of_ids):
    '''
    Description: Find the common friends of all the people with the given IDs

    Parameters:
    - records (LIST): A list of person records (each of which is a dictionary)
    - list_of_ids (LIST): A list of IDs (INTEGER) of all the people whose common friends are to be found

    Returns:
    - A LIST of INTEGERS containing the IDs of all the common friends of the specified list of people
    '''
    li = []
    li_intersect = []

    for data in records:
        if data['id'] in list_of_ids:
            fi = list(data['friend_ids'])
            li.append(fi)

    inter_sect = (set(li[0]).intersection(*li))

    for x in inter_sect:
        li_intersect.append(x)

    return li_intersect


def is_related(records, person_id_1, person_id_2):
    '''
    **** BONUS QUESTION ****
    Description: Check if 2 persons are friends

    Parameters:
    - records (LIST): A list of person records (each of which is a dictionary)
    - person_id_1 (INTEGER): first person ID
    - person_id_2 (INTEGER): second person ID

    Returns:
    - A BOOLEAN denoting if the persons are friends of each other, directly or indirectly (if A knows B, B knows C and C knows D, then A knows B, C and D).
    '''
    boolean = ''

    for data in records:

        if person_id_1 == data['id']:
            if person_id_2 in data['friend_ids']:
                boolean = True

        if person_id_2 == data['id']:
            if person_id_1 in data['friend_ids']:
                boolean = True

        elif person_id_1 == data['id']:
            for x in data['friend_ids']:

                if data['id'] == x:
                    print('True')
                    print(data['friend_ids'])
                    if person_id_2 in data['friend_ids']:
                        boolean = True
                    else:
                        is_related(records, x, person_id_2)

    return boolean


def delete_by_id(records, person_id):
    '''
    Description: Given a person ID, this function deletes them from the records. Note that the given person can also be a friend of any other person(s), so also delete the given person ID from other persons friend list. If the person ID is not available in the records, you can ignore that case.

    Parameters:
    - records (LIST): A list of person records (each of which is a dictionary)
    - person_id (INTEGER): The person id

    Returns:
    - A LIST of Dictionaries representing all the records (the updated version).
    In case there were no updates, return the original records.
    '''
    records_update = []
    ls = []
    for data in records:
        records_update.append(data)
    for item in records_update:

        if person_id in item['friend_ids']:
            (item['friend_ids']).remove(person_id)

        if item['id'] != person_id:
            ls.append(item)

    records = ls
    return(records)


def add_friend(records, person_id, friend_id):
    '''
    Description: Given a person ID and a friend ID, this function makes them friends of each other. If any of the IDs are not available, you can ignore that case.

    Parameters:
    - records (LIST): A list of person records (each of which is a dictionary)
    - person_id (INTEGER): The person id
    - friend_id (INTEGER): The friend id

    Returns:
    - A LIST of Dictionaries representing all the records (the updated version).
    In case there were no updates, return the original records.
    '''
    records_update = []

    for data in records:
        records_update.append(data)

    for item in records_update:

        if item['id'] == person_id:

            if friend_id in item['friend_ids']:
                pass

            if friend_id not in item['friend_ids']:
                (item['friend_ids']).append(friend_id)

        if item['id'] == friend_id:

            if person_id in item['friend_ids']:
                pass

            if person_id not in item['friend_ids']:
                (item['friend_ids']).append(person_id)

    records = records_update
    return (records)


def remove_friend(records, person_id, friend_id):
    '''
    Description: Given a person ID and a friend ID, this function removes them as friends of each other. If any of the IDs are not available, you can ignore that case.

    Parameters:
    - records (LIST): A list of person records (each of which is a dictionary)
    - person_id (INTEGER): The person id
    - friend_id (INTEGER): The friend id

    Returns:
    - A LIST of Dictionaries representing all the records (the updated version).
    In case there were no updates, return the original records.
    '''
    records_update = []

    for data in records:
        records_update.append(data)

    for item in records_update:

        if item['id'] == person_id:

            if friend_id in item['friend_ids']:
                (item['friend_ids']).remove(friend_id)

        if item['id'] == friend_id:

            if person_id in item['friend_ids']:
                (item['friend_ids']).remove(person_id)

    records = records_update

    return records


def add_education(records, person_id, institute_name, ongoing, percentage):
    '''
    Description: Adds an education record for the person with the given person ID. The education record constitutes of insitute name, the person's percentage and if that education is currently ongoing or not. Please look at the format of an education field from the PDF. If the person ID is not available in the records, you can ignore that case.

    Parameters:
    - records (LIST): A list of person records (each of which is a dictionary)
    - person_id (INTEGER): The person id
    - institute_name (STRING): The institute name (case-insensitive)
    - ongoing (BOOLEAN): The ongoing value representing if the education is currently ongoing or not
    - percentage (FLOAT): The person's score in percentage

    Returns:
    - A LIST of Dictionaries representing all the records (the updated version).
    In case there were no updates, return the original records.
    '''
    records_update = []

    for data in records:
        records_update.append(data)

    for item in records_update:

        if item['id'] == person_id and percentage > 0 and ongoing == False:
            item['education'].append({
                'institute': institute_name, 'ongoing': ongoing, 'percentage': percentage})

        if item['id'] == person_id and percentage <= 0 and ongoing == True:
            item['education'].append({
                'institute': institute_name, 'ongoing': ongoing})

    records = records_update
    return records
