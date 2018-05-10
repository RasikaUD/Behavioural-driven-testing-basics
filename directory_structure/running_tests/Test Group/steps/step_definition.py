
from behave import given, when, then
#import login
#from login import login


@given("I am in Main directory")
def in_main_dir(context):
    print("I am in Main directory executed....")
    pass

@then("I should also be in main directory")
def also_in_main_dir(context):
    print("I should also be in main directory executed....")
    pass

@given("I am in subdirectory of main directory")
def in_sub_dir(context):
    print("I am in subdirectory of main directory executed....")
    pass

@given("I am negative test in main steps")
def in_neg_dir(context):
    print ("I am negative test in main steps executed....")