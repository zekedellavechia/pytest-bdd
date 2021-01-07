@login
Feature: Login Feature
  Login Tests for site

  @smoke
  Scenario: Login with valid user
    Given login page is displayed
    When the user enters valid credentials
    Then the user accesses the site
