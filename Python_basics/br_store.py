# Importing type-1 bbr, to make it easier
from br import blackbox

#  The class / user template for blackbox type -2
class blackbox_store(blackbox):
    # THis is inheritance import the function of type -1 and then make additions
    # can do all the functions of type -1 plus addl.
    def store_value(self):
        print("Compressing and storing values")

    # To override the def, define here again
    def write_data(self):
        print("Write data from FPGA to DSP")