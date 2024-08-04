# Name - MOHAMMAD SHARIQ
# Roll No - 2020220
import a2


'''
- This is the skeleton code, wherein you have to write the logic for each of the
functions defined below.

- DO NOT modify/delete the given functions.

- DO NOT import any python libraries. You may only import a2.py.

- Make sure to return value as specified in the function description.

- Remove the pass statement from the function when you implement it.

- Do not create any global variables in this module.
'''


# Write the code here for creating an interactive program.
print('-'*200)
s = '  STUDENT  PROFILES '
print('\n', s.center(198, '#'))
print('\n', '-'*200)
print('  QUERIES You Can Perform $$$  '.center(198, '*'))
print('''
            1. read_data_from_file( Gives Info of all Students )
            2. filter_by_first_name
            3. filter_by_last_name
            4. filter_by_full_name
            5. filter_by_age_range
            6. count_by_gender
            7. filter_by_address
            8. find_alumni
            9. find_topper_of_each_institute
            10. find_blood_donors
            11. get_common_friends
            12. is_related
            13. delete_by_id
            14. add_friend
            15. remove_friend
            16. add_education
''')


while True:
    try:
        que_id = int(input('Enter the Query-ID YOU want to perform  ::: '))

    except:
        pass

    if que_id == 1:

        print('\n      Showing Student Details --->   \n')
        print('\n', a2.read_data_from_file(), '\n')

    if que_id == 2:

        print('\n')
        first_name = input(
            'ENTER first_name of Student by which You want to filter:: ')
        print('\n', 'ID-s Of students with {} as their first_name -- '.format(first_name), a2.filter_by_first_name(
            a2.read_data_from_file(), first_name), '\n')
    if que_id == 3:
        print('\n')
        last_name = input(
            'ENTER last_name of Student by which You want to filter:: ')
        print('\n', 'ID-s Of students with {} as their last_name -- '.format(last_name), a2.filter_by_last_name(
            a2.read_data_from_file(), last_name), '\n')

    if que_id == 4:
        print('\n')
        full_name = input(
            'ENTER full_name of Student by which You want to filter:: ')
        print('\n', 'ID-s Of students with {} as their full_name -- '.format(full_name), a2.filter_by_full_name(
            a2.read_data_from_file(), full_name), '\n')

    if que_id == 5:
        print('\n')
        min_age, max_age = (int(x) for x in (input(
            ' Enter Min and Max age of Student by which You want to filter:: ').split()))

        print('\n', '  ID-s Of students with min_age {} and max_age {} --  '.format(min_age, max_age), a2.filter_by_age_range(
            a2.read_data_from_file(), min_age, max_age), '\n')
    if que_id == 6:
        print('\n')
        print('  No. of Male and Female Students are :   ',
              a2.count_by_gender(a2.read_data_from_file()), '\n')

    if que_id == 7:
        print('\n')
        address = input('  Enter the address::  ')
        print('\n', 'The students with {} in their address are --->'.format(address), '\n\n',
              a2.find_alumni(a2.read_data_from_file(), address), '\n')

    if que_id == 8:
        print('\n')
        institute_name = input('  Enter the name of the Institute ::  ')
        print('\n', 'The alumnis of {} institute  ---  '.format(institute_name.upper()), '\n\n',
              a2.find_alumni(a2.read_data_from_file(), institute_name), '\n')

    if que_id == 9:

        print('\n', 'The following Students are Toppers ----> ', '\n\n',
              a2.find_topper_of_each_institute(a2.read_data_from_file(), '\n'))

    if que_id == 10:

        print('\n')
        reciever_person_id = int(input('Enter Donee ID --  '))
        print('\n', 'The following can be donors ----> ', '\n\n',
              a2.find_blood_donors(a2.read_data_from_file(), reciever_person_id), '\n')

    if que_id == 11:
        print('\n')
        list_of_ids = [int(x) for x in (input(
            ' Enter the Ids of the Students whom Common friend list is required --- ').split())]

        print('\n', 'The Common friends are ----->  ', '\n\n',
              a2.get_common_friends(a2.read_data_from_file(), list_of_ids), '\n')

    if que_id == 12:

        print('\n')
        person_id_1 = int(input(
            ' Enter the person_1_ID ---  '))
        person_id_2 = nt(input(
            ' Enter the person_2_ID ---  '))
        print('\n', 'Are they Friends --->  ', '\n\n',
              a2.is_related(a2.read_data_from_file(), person_id_1, person_id_2), '\n')

    if que_id == 13:
        print('\n')
        person_id = int(input(
            ' Enter the Id of the Student whom info You want to delete ---  '))
        print('\n', 'The Updated Student Details --->  ', '\n\n',
              a2.delete_by_id(a2.read_data_from_file(), person_id), '\n')

    if que_id == 14:
        print('\n')
        person_id = int(input(
            ' Enter the Person_Id '))
        friend_id = int(input(
            ' Enter the Friend_Id whom You want to add as friend --- '))

        print('\n', 'The Updated Student Details --->  ', '\n\n',
              a2.add_friend(a2.read_data_from_file(), person_id, friend_id), '\n')

    if que_id == 15:

        print('\n')
        person_id = int(input(
            ' Enter the Person_Id '))
        friend_id = int(input(
            ' Enter the Friend_Id whom You want to remove as friend --- '))

        print('\n', 'The Updated Student Details --->  ', '\n\n',
              a2.remove_friend(a2.read_data_from_file(), person_id, friend_id), '\n')

    if que_id == 16:
        print('\n')
        print('Enter the education details you want to add --->  ', '\n')
        person_id = int(input(
            ' Enter the Person_Id  :'))
        institute_name = input(' Enter the institute_ name  : ')
        ongoing = (input(' Enter the ongoing status  :'))
        ongoing = ongoing[0].upper()+ongoing[1:]

        percentage = float(input(' Enter the percentage  :'))

        print('\n', 'The Updated Student Details --->  ', '\n\n',
              a2.add_education(a2.read_data_from_file(), person_id, institute_name, ongoing, percentage), '\n')

    if que_id == -1:
        print('\n', 'Exiting.............')
        break
