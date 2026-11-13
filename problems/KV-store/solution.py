# {"name": "John:Doe", "city": "New,York"}

# {"ab": "xyz"}
# 2:ab3:xyz

def serialize(kv_dict):
    if not kv_dict:
        return

    outputs = []

    for key, value in kv_dict.items():
        key_str = str(key)
        value_str = str(value)
        output_string = f"{len(key_str)}:{key_str}{len(value_str)}:{value_str}"
        outputs.append(output_string)


    return "".join(outputs)


def len_data_extrator(str, pos):
    dim = str.index(":", pos)
    data_len = int(str[pos:dim])
    start_index = dim + 1
    end_index = start_index + data_len
    data = str[start_index:end_index]

    return data, end_index


def deserialize(str):
    if str == "":
        return
    pos = 0

    output_kv = {}
    while pos < len(str):

        key, end_index = len_data_extrator(str, pos)
        pos = end_index

        value, end_index = len_data_extrator(str, pos)
        pos = end_index

        output_kv[key] = value

    return output_kv




test_case = {"name": "John:Doe", "city": "New,York"}
#test_case = {"ab": "xyz"}
print(test_case)
s_str = serialize(test_case)

print(s_str)

result = deserialize(s_str)

print(result)
    