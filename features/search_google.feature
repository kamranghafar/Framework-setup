Feature: Search Google

@smoke
Scenario: Search for kamran ghaffar on Google and click the first link
    Given the user is on the Google homepage
    When the user searches for kamran ghaffar
    Then the user clicks on the first search result
