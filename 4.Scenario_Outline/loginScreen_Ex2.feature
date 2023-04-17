# This is a Feature file

Feature: Fill the Contact Form

    Scenario Outline: User Login credentials

        Given Launch the App and Click on Login Button
        When Enter <emailid> UserID
        When Enter  <password> password
        Then Verify Home Screen


        Examples:
             | emailid          |password|
             | student@gmail.com| S1234  |
             | Teacher@gmail.com| T1234  |

"""
A Scenario Outline is used if we have a group of similar criteria and the results are to be passed in a Scenario. A Scenario Outline is accompanied with an Examples table. A Scenario Outline can have multiple Examples tables.

The tests get executed once for every row found (after the header row) within the Examples table. The values to be tested are represented by their names enclosed in brackets<>. These names should match with the Examples table header.

It helps to reduce the lines of code (eliminates repeating steps) and orders our tests.
"""