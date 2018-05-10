from behave import given, then, when

@given("I have a new {item} in my cart")
def i_have_item_in_cart(context,item):
    print("The item is: {}".format(item))

@when("I click on {click_button}")
def i_click_on(context, click_button):
    print ("You clicked on {}".format(click_button))

@then('I should see "{status}"')
def i_should_see_status(context,status):
    if status not in ['success','error']:
        raise Exception("Unexpected text passed in")
    if status.lower()=='success':
        print ("Yayyyy")
    else:
        print ("Noooooo")
    print ("Checking  if I see the '{}' text".format(status))
    print("PASS. I see see {}".format(status))

