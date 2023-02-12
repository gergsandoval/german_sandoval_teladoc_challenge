Feature: User Management

    Scenario: Add an user and validate the has been added to the table
        Given I open protractor practice website
        When I add a new user
        | first_name | last_name  | user_name   | password | customer     | role       | email                | cellphone  |
        | Maria      | Washington | mwashington | iefie8Ez | Company BBB  | Admin      | mwashington@mail.com | 1234567890 |
        Then I see the user has been added to the table
        | first_name | last_name  | user_name   | customer     | role       | email                | cellphone  | locked |
        | Maria      | Washington | mwashington |              | Admin      | mwashington@mail.com | 1234567890 | False  |

    Scenario: Delete the user 'novak' from the table and validate the user has been deleted
        Given I open protractor practice website
        When I delete user 'novak'
        Then I see the user 'novak' has been deleted from the user list