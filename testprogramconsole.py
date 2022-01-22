
# KVCC 
# CIS-226-23199
# Advanced Python Programming
from programconsole import program_console
from programconsole import EXPECTED

def test_program_console():
    answer = []
    answer = program_console(answer)
    assert answer == EXPECTED