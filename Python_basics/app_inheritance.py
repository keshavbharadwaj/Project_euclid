# Importing blockbox type-1 with file name as br, and class as blockbox
from br import blackbox
from br_store import blackbox_store

# blockbox type-1 object
my_blackbox = blackbox()
my_blackbox_updated = blackbox_store()


# Accessing the def inside the class blackbox
print("\nBBR-1")
my_blackbox.write_data()
my_blackbox.read_data()
my_blackbox.analyze_plot()

# Accessing the def inside the class blackbox-2
print("\nBBR-2")
my_blackbox_updated.write_data() # Override inside
my_blackbox_updated.read_data()
my_blackbox_updated.analyze_plot()
my_blackbox_updated.store_value()

# Using Inheritance to call classes within class