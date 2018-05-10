from behave import then

@then("I am in a python file of the subdirectory")
def in_python_file(context):
    print("I am in a python file of the subdirectory")
    pass