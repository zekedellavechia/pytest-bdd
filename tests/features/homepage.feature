Feature: Homepage related cases
  As an user
  I want to navigate the main page,
  So i can see all the content.

  Scenario: Navigate to home page
    Given homepage is displayed
    When the user clicks home
    Then homepage page opens



  Scenario: Navigate to results page
    Given homepage is displayed
    When the user clicks results
    Then results page opens
    And close browser