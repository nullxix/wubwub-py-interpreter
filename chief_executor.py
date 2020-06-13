#
#           MASTER OF EXECUTING TOKENS
#                  if a token is found in the function table
#                  pass ME the function, and I will handle it
#
#
#


def execute_token(func: str, cursor = "root", runtime = "wub"):
    if(runtime == "wub" or runtime == "wubwub" or runtime == "ww"):
        pass
    elif(runtime == "python" or runtime == "the snake"):
        func(cursor)
