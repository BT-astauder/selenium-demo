*** Settings ***
Library         Selenium2Library

*** Test Cases ***
Login
	Open Browser    ${URL}
    Capture Page Screenshot
    Add Cookie   ${COOKIE_NAME}    ${COOKIE_VALUE}
	Go To     ${URL}
	Sleep    20s
    Capture Page Screenshot

Just a test
    Close Browser

Failure
	Should Be True    "a" == "b"
	Fail    Test falsch