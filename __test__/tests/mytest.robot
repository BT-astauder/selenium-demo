*** Settings ***
Library         Selenium2Library
Library         output_video_url.py
Test Setup                  Start browser
Test Teardown               Close All Browsers

*** Variables ***
${BROWSER}                  internetexplorer
${ALIAS}                    None
${REMOTE_URL}               http://8m4HoRq92in3C2JE8vFll0prTQgfGfAE:svcGcsF5BSY3LyyKU4V5UbnDStIoz9SR@F1P5412S.gridlastic.com:80/wd/hub
${DESIRED_CAPABILITIES}     platform:VISTA,video:True,version:11

*** Keywords ***
Start Browser
    [Documentation]         Start browser on Selenium Grid
    Open Browser            https://www.google.com/ncr  ${BROWSER}  ${ALIAS}  ${REMOTE_URL}  ${DESIRED_CAPABILITIES}
    Maximize Browser Window

*** Test Cases ***
Test Google
    [Documentation]         Test Google
    output video url
    Input Text    q    webdriver
    Submit Form
    Wait Until Page Contains    Searches related to webdriver

Login
    Open Browser    ${URL}  ${BROWSER}  ${ALIAS}  ${REMOTE_URL}  ${DESIRED_CAPABILITIES}
    Capture Page Screenshot
    Add Cookie   ${COOKIE_NAME}    ${COOKIE_VALUE}
	Go To     ${URL}
	Sleep    20s
    Capture Page Screenshot

Just a test
    Close Browser

#Failure
#	Should Be True    "a" == "b"
#	Fail    Test falsch