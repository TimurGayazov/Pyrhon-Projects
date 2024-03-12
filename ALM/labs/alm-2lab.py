def check_code(op):
    if op == "11" or op == "00":
        return True
    return False


def check_op_str(op1, op2):
    for i in op1:
        if i != "0" and i != "1":
            return False
    for i in op2:
        if i != "0" and i != "1":
            return False
    return True


def format_text(text):
    temp_str = bin(int(text)).removeprefix("0b")
    if len(temp_str) > 64:
        return False
    elif len(temp_str) < 64:
        delta = 64 - len(temp_str)
        return "0" * delta + temp_str
    return temp_str


def print_all(id):
    print("~ " + "S" + str(
        id) + " ~" + "\n" + '-' * 70 + '\n' + "Kod = " + op_code + "\nOp1 = " + first_num + "\nOp2 = " + second_num + "\nRes = " + result + "\nErr = " + Err + '\n' + '-' * 70)


Err = "000"
op_code = "00"
first_num = "0" * 64
second_num = "0" * 64
result = "0" * 64
print_all(0)

if __name__ == '__main__':
    print_all(1)
    with open("input.txt", "r") as infile:
        print_all(2)
        in_str = infile.read().split()
        op_code = in_str[0]
        first_num = in_str[1]
        second_num = in_str[2]
        print_all(3)
        print_all(4)
        if not check_code(op_code):
            Err = "010"
            print_all(0)
            exit()
        elif not check_op_str(first_num, second_num):
            print_all(5)
            Err = "011"
            print_all(0)
            exit()
        elif len(first_num) != 64 or len(second_num) != 64:
            Err = "100"
            print_all(0)
            exit()
        int_first_num = int(first_num, 2)
        int_second_num = int(second_num, 2)
        print_all(6)
        if op_code == "00":
            print_all(7)
            result = format_text(int_first_num * int_second_num)
            if not result:
                Err = "101"
                result = 64 * "0"
                print_all(0)
                exit()
        else:
            if int_second_num == 0:
                Err = "001"
                print_all(0)
                exit()
            else:
                print_all(8)
                result = format_text(int_first_num / int_second_num)
                if not result:
                    Err = "101"
                    result = 64 * "0"
                    exit()
        print_all(0)
