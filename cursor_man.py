import chief_executor
import stack_master
import table_king
# 
# 
#   WELCOME TO THE CURSOR
#       MWAHAHAHAHAH
# 
#  each cursor reads the code
#  if it finds a function that can be executed,
#  it creates a NEW cursor to execute that
#  and puts that cursor on the cursor stack



class Cursor:
    def __init__ (self, tokens: list, parent = "root"):
        self.tokens = tokens
        self.parent = parent
        self.pos = -1; #step will take this to 0
        self.active = True
        self.stack_index = stack_master.push("cursors", self)

    def end_cursor(self):
        stack_end = stack_master.get_len("cursors") - 1
        if self.stack_index == stack_end:
            self.active = False
            stack_master.pop("cursors")
        else:
            raise Exception("Error: cursor_man.py -- attempted to remove cursor that is not at top of cursor stack ---> remove:", self.stack_index, " end-of-stack:", stack_end)

    def step(self):
        #check if we're at EOF
        if(self.pos == len(self.tokens) -1):
            self.end_cursor()
        else:
            self.pos = self.pos + 1

    def eval_token(self, token):
         # get function from tables
        func_pack = table_king.check_token(token)
        
        # if the function DOES NOT EXIST add to stack
        if not func_pack['func']:
            stack_master.push('data', token)
        #otherise, execute the function
        else:
            func = None
            runtime = "wub"
            
            # anything pulled from the "core" table 
            # has a custom runtime
            if(func_pack['table'] == "core"):
                func = func_pack["func"]
                runtime = func_pack["runtime"]
            else:
                func = func_pack["func"]

            execute_token(func, self, runtime) 

    def read_tokens(self):
        """compares tokens to function tables, then executes the corresponding function.
            if no match is found, the token is added to the data stack
        """
        self.step()
        if self.active:
            self.eval_token(self.tokens[self.pos])
            self.read_tokens()
        
    
    def get_current_token(self):
        """returns token at cursor position
        """
        return self.tokens[self.pos]
           

        pass
        #[TODO] cleanup, we've reached the end of the function / file      

    def get_parent(self):
        if(self.stack_index > 0):
            stack_master.retrieve("cursors", self.stack_index - 1)
        else:
            return "root"



def create_cursor(tokens: list, parent: Cursor):
    new_cursor = Cursor(tokens, parent)
    new_cursor.read_tokens()



def execute_token(func, parent_cursor = "root", runtime = "wub"):
    """executes a token with the given runtime. 'wub' is the default language runtime.
        the parent should be the cursor that called this function
    """

    if(runtime == "wub"):
        create_cursor(func, parent_cursor)

    # otherwise, it's an instruction to an runtime / runtime
    else:
        chief_executor.execute_token(func, parent_cursor, runtime)






