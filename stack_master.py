

stacks = {
    "data" : [

    ],
    "cursors" : [

    ]
}


def push(stack: str, what: str):
    """pushes an anonymous function to a stack

        as a failsafe, ignores newline and blank characters
    """
    stacks[stack].append(what)
    return get_len(stack) - 1

def pop(stack: str):
    """pops an anonymous function from a stack
    """
    return stacks[stack].pop()

def get_len(stack: str):
    """returns number of items in a stack
    """
    return len(stacks[stack])

def retrieve(stack: str, index: int):
    return stacks[stack][index]