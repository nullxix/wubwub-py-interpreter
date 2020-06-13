

# 
#   THE FUNCTIONS MWAHAHAHA
# 

    # def a function
        # add to table

    # defx
        # insert grab + release
        # add to table

    # -> push to stack
    # <- pop from stack

    # grab
        # evaluate code until x returns

    # release
    # undef
        # --> remove next token from table

    # kidnap
        # grab the next TOKENS (no eval)

    # # ; 
        # comment function begins with '#' ends with ';'
        # essentially escapes all characters between those so they'll do nothing
        # as of this writing, there is no way to escape a ';'



# 
#   THE PROCESS MWAHAHAHA
# 

    # 1. get the tokens
    # 2. iterate through tokens
    # 3. compare token to tables
    # 4. run token
    # 5. token undef? RETURN IT MWAHAHAHA


    # 1. get tokens
        # accept a string or array,
        # if (string)
            # convert to array
        # if array
            # do next step

    # 2. iterate
        # if END OF FILE
        # accept an array
        # table compare (3)
        # step <-- move forward

    # 3 check if on table
        # loop through all tables
            # if on table run (3) for that table
        # if NOT on table
            # -> push to stack (5)
            # END & REPEAT (9)
    
    # 4. run on table
        #instructions different for each table MIGHT NEED INTERPRETER STACK [see w.1]

            # scope table --> run function

            # user table --> run function            

            # core table --> run function with specified interpreter (default wubwub )
                        #   python interpreter (this) <-- might need to have a subroutine/interpreter stack,
                        #   + a way to communicate one level higher (review this) [see w.1]

    # 5. push token to stack
        # everything on 'stack' is an anonymous function
        # because _everything_ is a function in wubwub,
        # we can simply put the token, all alone, on the stack


    # 9. Repeat
        # step (x.1) 
        # go back to the beginning

#
#           Welcome to X
#   Internal Procedures/ Functions
#       MWAHAHAHAHAHAHAHAAHA
#

    # x.1 step
        # advance cursor
            # if EOF
                #terminate program

    # x.2 run (token)
        # MAYBE -- run interceptor table (haven't decided yet)
            # alternatively, trigger an event, etc.
        


#
#       Welcome to W
#  Musings on Inner Workings, How This Will Work
#       MAWHAAHAHAHAHAAHHAAHAHA
#

    # w.1 interpreter stack / nested interpretes 
        # intro:
            # each function must be interpreted, of course.
            # the cursor state of an interpreter must be maintained--
            # to this end we create a new interpreter instance to run
            # each function
                # --- a TON of interpreters will be created by this procedure
                # might be more performant to create multiple 'cursors'
                # for each interpreter following a singleton pattern
            
            # lower cursors/interprrs on the stack need access
            # to higher cursors, because many functions
            # address the cursor position


        # ideas / discussion
            # 1.  
                # give each cur/interpprp a reference to its parent
                # call parent.cursor.move, etc.
            # 1.1
                # the cursor parent pattern feels wrong in implementation
                # we're already putting the cursors on a stack
                # it might be better to simply use one or the other
            # 1.2
                # putting everything on a stack has become something of a running gag
                # because this is a "for-fun" language we're going with that
                # this will likely be (marginally) more complicated to implement,
                # but _should_ be more reliable in the long-term
                # probably won't matter when we re-write the interpreter in C++

                # this stack will (probably) need to be in some way indexed
                # because we need to access members deeper in the stack
            

        # conclusion v 0.0.1

            # we're going to have a "run(interpreter, parent)" function
                # if there's an instance of that interpterer running
                    # add a cursor to the stack and make it execute
                # else
                    # open new instance of interpreter
            
            # an interpreter can call on parent.cursor to affect the parent cursor

            # there will be a default "root" parent for the core interpreter
                # if the core interpreter tries to call root.cursor
                    # 1. throw an error
                    # OR
                    # 2. don't

                    # 1 is better, but this is a FOR-FUN language, let's do 2
                    # 2 might allow us to sneak in some added functionality
        
        # conclusion v 0.0.2

            # we're axing the parent model in favor of putting it on an "indexed stack"
            # because making everything a type of stack has become a running joke
            