
# KVCC 
# CIS-226-23199
# Advanced Python Programming
from programconsole import program_console
from programconsole import EXPECTED

def test_program_console(searchtext, filename):
    answer = [(searchtext, filename)]
    answer = program_console(answer)
    EXPECTED = [(searchtext, filename)]
    assert answer == EXPECTED