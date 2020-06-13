import stack_master
import table_king
import sys
from wub_config import EOS_DELIMITER, SUPER_EOS_DELIMITER

def bark(cursor = "root"):
    print("Woof!")

def print_stack(cursor):
    print(stack_master.stacks["data"])

def sum(cursor):
    """ pop x values from the stack, then push the sum
    """
    cursor.step()
    c_tok = cursor.get_current_token()

    try:
        count = float(c_tok)
        sum = 0
        for i in range(0, count):
            sum += stack_master.pop("data")
        stack_master.push("data", str(sum))
    except:
        print("I'm a numbers adding kinda guy")

def mult(cursor):
    """ pop x values from the stack, multiply them together and push the total
    """
    cursor.step()
    c_tok = cursor.get_current_token()

    try:
        count = float(c_tok)
        total = 1
        for i in range(0, count):
            total *= stack_master.pop("data")
        stack_master.push("data", str(total))
    except:
        print("I'm a numbers multiplying kinda guy")

def print_ln(cursor):
    """grabs tokens until next EOS and prints with spaces
    """
    tokens = []

    while True:
        cursor.step()
        c_tok = cursor.get_current_token()

        if c_tok == EOS_DELIMITER or c_tok == SUPER_EOS_DELIMITER:
            break

        tokens.append(c_tok)

    print(' '.join(tokens))

def out(cursor):
    _top = stack_master.get_len("data") - 1
    _data = stack_master.retrieve("data", _top)
    sys.stdout.write(_data)

def outx(cursor):
    cursor.step()
    c_tok = cursor.get_current_token()

    try:
        _i = int(c_tok)
        _data = stack_master.retrieve("data", 0 - _i)
        sys.stdout.write(_data)
    except:
        sys.stdout.write(" ")

def outyy(cursor):
    cursor.step()
    c_tok == cursor.get_current_token()

    try:
        for i in range(0, int(c_tok)):
            _data = stack_master.retrieve("data", -1 * i)
            sys.stdout.write(_data)
    except:
        sys.stdout.write(" ")

def def_func(cursor):
    tokens = []

    ## get function key/name

    cursor.step()
    key = cursor.get_current_token()

    ## get function definition (code we run later)

    super_EOS_found = False
    while not super_EOS_found:
        # move forward
        cursor.step()
        # get the token
        c_tok = cursor.get_current_token()

        # a ';;' (or other delimiter) indicates end of func definition statement
        if c_tok == SUPER_EOS_DELIMITER:
            super_EOS_found = True
            break
        
        # add token to tokens list
        tokens.append(c_tok)


    # add everything to table
    table_king.add_token(key=key, func = tokens)

def undef(cursor):
    """undefines a user function
    """

    cursor.step()
    c_tok = cursor.get_current_token()

    table_king.kill_token(c_tok)

def push(cursor):
    #get next token
    cursor.step()
    c_tok = cursor.get_current_token()
    stack_master.push("data", c_tok)

def pop(cursor):
    # get name
    cursor.step()
    c_tok = cursor.get_current_token()

    temp = stack_master.pop("data")

    table_king.add_token(key = c_tok, func = temp, table = "user")