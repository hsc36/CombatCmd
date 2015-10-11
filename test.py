# Test functions and processes (NOT for low-level unit testing)


#--- Functions ---#
# @TODO: Functions for use in test processes
def list_init_variables(object):
	return [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith('__')]

#--- Processes ---#
# @TODO: Test classes and simulated gameplay