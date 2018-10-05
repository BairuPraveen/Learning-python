import re


def covert_fasta_to_dictionary(filename):
    sequence = ''
    sequence_id = 0
    sequence_flag = 0
    sequence_dct = {}
    with open(filename)as file:
        for lines in file:
            data = re.findall(r'(\w+\_\d+\.\d).*', lines)
            if data:
                sequence_flag = 1
                lines = lines.strip()
                sequence_id = data[0]
                sequence = ""
            elif sequence_flag == 1:
                sequence = "".join([sequence, lines])
                sequence_dct[sequence_id] = sequence
    return sequence_dct


def base_location(sequence_dct, id, start, end):
    sequence = None
    try:
        mystr = sequence_dct[id]
        length = len(mystr)
        if end<length:
            sequence = mystr[start:end]
        else:
            sequence = "OUT OF RANGE"
        return sequence
    except:
        print('ERROR:input id is not valid')
        return 0


def max_length(sequence_dct):
    max_id = ""
    max_id_len = 0
    max_sequence = ''
    for key, values in sequence_dct.items():
        seq_length = len(values)
        if seq_length > max_id_len:
            max_id_len = seq_length
            max_id = key
            max_sequence =(sequence_dct[max_id])

    return max_id, max_sequence


def min_length(sequence_dct):
    min_id = ""
    min_sequence = ''
    min_id_len = None
    for key, values in sequence_dct.items():
        seq_length = len(values)
        if not min_id_len:
            min_id_len = seq_length
        if seq_length < min_id_len:
            min_id_len = seq_length
            min_id = key
            min_sequence = (sequence_dct[min_id])
    return min_id, min_sequence


sequence_file = 'GCF_000757845.1_ASM75784v1_protein.faa'

sequence_dct = covert_fasta_to_dictionary(sequence_file)
print("total sequence length:",len(sequence_dct))


id = input("enter id no:")
while id not in sequence_dct:
    print("Id is not present")
    id = input("enter id no:")

else:
    From = eval(input('enter locaton from:'))
    To = eval(input('enter locaton to:'))

    data = base_location(sequence_dct, id,From, To)
    print("This ur searching lacation seqence:",data)

id, maximum = max_length(sequence_dct)
print(id)
print(maximum)

min_id, minimum = min_length(sequence_dct)
print(min_id)
print(minimum)


