
from prettyTable import PrettyTable


input_array = [1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,13,1,19,1,10,19,23,1,23,9,27,1,5,27,31,2,31,13,35,1,35,5,39,1,39,5,43,2,13,43,47,2,47,10,51,1,51,6,55,2,55,9,59,1,59,5,63,1,63,13,67,2,67,6,71,1,71,5,75,1,75,5,79,1,79,9,83,1,10,83,87,1,87,10,91,1,91,9,95,1,10,95,99,1,10,99,103,2,103,10,107,1,107,9,111,2,6,111,115,1,5,115,119,2,119,13,123,1,6,123,127,2,9,127,131,1,131,5,135,1,135,13,139,1,139,10,143,1,2,143,147,1,147,10,0,99,2,0,14,0]


def int_code_program():
    print(input_array)
    i = 0
    while i < len(input_array):
        op_code = input_array[i]
        if op_code == 1:
            # each value  acts as an index to use from 
            print('index {} opCode {}'.format(i, input_array[i]))

            i += 1
            add_index_1 = i
            print('\tadd_index_1 {} add_index_value_1 {} '.format(add_index_1 , input_array[add_index_1]))
            i += 1
            add_index_2 = i
            print('\tadd_index_2 {} add_index_value_2 {} '.format(add_index_2 , input_array[add_index_2]))
            i += 1
            destination_index = i
            print('\tadded destination_value {} destination_index {} '.format(input_array[add_index_1] + input_array[add_index_2],  input_array[destination_index]))
            input_array[input_array[destination_index]] = input_array[add_index_1] + input_array[add_index_2]
        elif op_code == 2:
            # each value acts as an index to use from 
            print('index {} opCode {}'.format(i, input_array[i]))
            i += 1
            multiply_index_1 = i
            print('\tmultiply_index_1 {} multiply_index_value_1 {} '.format(multiply_index_1 , input_array[multiply_index_1]))
            i += 1
            multiply_index_2 = i
            print('\tmultiply_index_2 {} multiply_index_value_2 {} '.format(multiply_index_2 , input_array[multiply_index_2]))
            i += 1
            destination_index = i
            print('\tdestination_index {} destination_value {} '.format(destination_index,  input_array[destination_index]))
            input_array[input_array[destination_index]] = input_array[multiply_index_1] * input_array[multiply_index_2]
        elif op_code == 99:
            print('breaking after {} times'.format(i))
            break
        print(input_array)
        i += 1
    print(input_array[0])


if __name__ == '__main__':
    int_code_program()
    
    