Feature: Demo of displaying output on console
  Scenario: A test will pass(stdout demo)
    Given I am at home page
    When I click on "Contact Us"
    Then I should see 123 Testing St.

 Scenario: A test will fail(stout demo)
   Given I am at home page
   When I click on "My account"
   Then I should see "Preferences"
