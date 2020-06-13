import core_actions

core = [
    {
        "key": "bark",
        "func": core_actions.bark,
        "runtime": "the snake"
    },
    {
        "key":"->",
        "func": core_actions.push,
        "runtime":"python"
    },
    {
        "key":"<-",
        "func":core_actions.pop,
        "runtime":"python"
    },
    {
        "key": "def",
        "func": core_actions.def_func,
        "runtime": "python"
    },
    {
        "key":"undef",
        "func": core_actions.undef,
        "runtime":"python"
    },
    {
        "key":"print",
        "func": core_actions.print_ln,
        "runtime":"python"
    },
    {
        'key':'add',
        'func': core_actions,
        'runtime':'python'
    },
    {
        "key":"mult",
        "func": core_actions.mult,
        "runtime":"python"
    },
]