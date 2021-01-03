Feature: Homepage related cases
  As an user
  I want to navigate the main page,
  So i can see all the content.

  Scenario: Navigate to home page
    Given homepage is displayed
    When the user clicks home
    Then homepage page opens

  Scenario: Navigate to about page
    Given homepage is displayed
    When the user clicks about
    Then about page opens

  Scenario: Navigate to results page
    Given homepage is displayed
    When the user clicks results
    Then results page opens

  Scenario: Navigate to FAQ page
    Given homepage is displayed
    When the user clicks FAQ
    Then FAQ page opens

  Scenario: Navigate to resources page
    Given homepage is displayed
    When the user clicks resources
    Then resources page opens

  Scenario: Navigate to our partners page
    Given homepage is displayed
    When the user clicks our partners
    Then our partners page opens

  Scenario: Navigate to Contact us page
    Given homepage is displayed
    When the user clicks contact us
    Then contact us page opens