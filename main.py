import wub_parser
import sys
import chief_executor
import cursor_man


# iterate through the functions
first_filename = "test.wubwub"
if(len(sys.argv) > 1):
    first_filename = sys.argv[1]


def load_wub_file(filenombre: str):
    """loads a .wubwub file and converts it into a token list

    """
    tokens = []
    with open(filenombre) as f:
        wub_script = f.read()

        tokens = wub_parser.parse(wub_script)
    return tokens


tokens = load_wub_file(first_filename)
cursor_man.create_cursor(tokens, "root")