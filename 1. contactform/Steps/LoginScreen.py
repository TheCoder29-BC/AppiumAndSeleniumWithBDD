from behave import given, when, then


@given("Launch the App and Click on Login Button") #defining for the .feature file should the same line
def methodOne(context):
    print("L1 - Launching the App")


@when("Enter UserID")
def methodTwo(context):
    print("L2 - Enter the UserID in Login Screen")


@when("Enter password")
def methodThree(context):
    print("L3 - Enter the Password in Login Screen")


@when("Click on Login Button")
def methodFour(context):
    print("L4 - Clicked on the login Button")


@when("Home page opens")
def methodFour(context):
    print("L5 - Home Page opened")


@then("Verify Home Screen")
def methodFive(context):
    print("L6 - Home Screen Opened")


@then("Take Screenshot")
def methodSix(context):
    print("L7 - ScreenShot taken")

#To run the tests open Terminal go to the feature file path and then write this command
#behave login_screen.feature --no-capture -f plain for MAC
#behave login_screen.feature
#behave login_screen.feature --no-capture Windows

"""
    --- Output ---
    cmd : behave login_screen.feature
Feature: Fill the Contact Form # login_screen.feature:3

  Scenario: User Login credentials                 # login_screen.feature:5
    Given Launch the App and Click on Login Button # steps/LoginScreen.py:4
    When Enter UserID                              # steps/LoginScreen.py:9
    When Enter password                            # steps/LoginScreen.py:14
    When click on Login Button                     # steps/LoginScreen.py:19
    And Home page opens                            # steps/LoginScreen.py:24
    Then Verify Home Screen                        # steps/LoginScreen.py:29
    Then Take screenshot                           # steps/LoginScreen.py:34

  Scenario: Enter the data in Contact Form        # login_screen.feature:16
    Given Launch the App and Click on ContactForm # steps/ContactForm.py:4
    When Enter Name                               # steps/ContactForm.py:14
    When Enter Email                              # steps/ContactForm.py:19
    When Enter Mobile Number                      # steps/ContactForm.py:24
    And we need to click on submit button         # steps/ContactForm.py:29
    Then Click on submit                          # steps/ContactForm.py:34
    Then Take Screenshot of contact Form          # steps/ContactForm.py:39

1 feature passed, 0 failed, 0 skipped
2 scenarios passed, 0 failed, 0 skipped
14 steps passed, 0 failed, 0 skipped, 0 undefined
Took 0m0.004s

"""

"""
    --- Output ---
    cmd: behave login_screen.feature --no-capture
    
Feature: Fill the Contact Form # login_screen.feature:3

  Scenario: User Login credentials                 # login_screen.feature:5
    Given Launch the App and Click on Login Button # steps/LoginScreen.py:4
L1 - Launching the App
    When Enter UserID                              # steps/LoginScreen.py:9
L2 - Enter the UserID in Login Screen
    When Enter password                            # steps/LoginScreen.py:14
L3 - Enter the Password in Login Screen
    When click on Login Button                     # steps/LoginScreen.py:19
L4 - Clicked on the login Button
    And Home page opens                            # steps/LoginScreen.py:24
L5 - Home Page opened
    Then Verify Home Screen                        # steps/LoginScreen.py:29
L6 - Home Screen Opened
    Then Take screenshot                           # steps/LoginScreen.py:34
L7 - ScreenShot taken

  Scenario: Enter the data in Contact Form        # login_screen.feature:16
    Given Launch the App and Click on ContactForm # steps/ContactForm.py:4
C1 - Launching the App
    When Enter Name                               # steps/ContactForm.py:14
C3 - Enter the Password in Login Screen
    When Enter Email                              # steps/ContactForm.py:19
C4 - Clicked on the login Button
    When Enter Mobile Number                      # steps/ContactForm.py:24
C5 - Home Screen Opened
    And we need to click on submit button         # steps/ContactForm.py:29
C6 - Clicking on Submit button
    Then Click on submit                          # steps/ContactForm.py:34
C7 - Click on the submit button
    Then Take Screenshot of contact Form          # steps/ContactForm.py:39
C8 - ScreenShot taken

1 feature passed, 0 failed, 0 skipped
2 scenarios passed, 0 failed, 0 skipped
14 steps passed, 0 failed, 0 skipped, 0 undefined
Took 0m0.015s

"""