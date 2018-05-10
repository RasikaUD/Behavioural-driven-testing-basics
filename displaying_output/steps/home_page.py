from behave import given, when, then

@given("I am at home page")
def at_home_page(context):
    print ("I am the code that will open the browser and will go to home page")
    print ("I am the code that will open the browser and will go to home page")
    print ("I am the code that will open the browser and will go to home page")

@when('I click on "Contact Us"')
def click_contact_us(context):
    print('I am clicking on the "contact us"')

@then('I should see 123 Testing St.')
def verify_address(context):
    print('I  see correct address')

@when('I click on "My Account"')
def click_myaccount(context):
    print("I am clicking on My account")

@then('I should see "Preferences"')
def verify_preferences(context):
    print("I see preferences page")
    assert 1!=2, "one is not same as two"