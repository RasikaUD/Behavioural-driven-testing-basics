Feature: Passing parameters to steps
Scenario: Method 1 of passing step parameters
  Given I have a new 'DVD' in my cart
  And I have a new 'Book' in my cart
  And I have a new 'Dress' in my cart
  When I click on 'Next'
  And I click on 'FINISH'
  Then I should see "success"
  And I should see "error"
