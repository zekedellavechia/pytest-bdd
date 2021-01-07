@homepage
Feature: Homepage related cases
  As an user
  I want to navigate the main page,
  So i can see all the content.


  Background:
    Given homepage is displayed

  Scenario: Navigate to home page
    When the user clicks home
    Then homepage page opens

  Scenario: Navigate to about page
    When the user clicks about
    Then about page opens

  @smoke
  Scenario: Navigate to results page
    When the user clicks results
    Then results page opens

  Scenario: Navigate to FAQ page
    When the user clicks FAQ
    Then FAQ page opens

  Scenario: Navigate to resources page
    When the user clicks resources
    Then resources page opens

  Scenario: Navigate to our partners page
    When the user clicks our partners
    Then our partners page opens

  Scenario: Navigate to Contact us page
    When the user clicks contact us
    Then contact us page opens
    # todo maybe i should add close browser for all cases (?
