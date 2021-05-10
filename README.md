
# CowinBot
The goal is to automate taps/clicks. You cannot bypass captcha and that still slows you down. 

You will need to edit the following before running the script. Use the network tools (learn how to use it [here](https://developer.chrome.com/docs/devtools/network/)) on your browser to get them. Press F12 (if it doesnt work, use FN + F12) to get the network tools before you start login.

 - Bearer token ( in authorization header )
	 - Just login and see the call to benefeciaries. Switch to headers in the details and look for authorization header in request headers. Screenshot below. You need to copy in between the brackets -
	 ![enter image description here](https://raw.githubusercontent.com/aaravpandya/CowinBot/main/images/Auth.JPG)
 - Beneficiary id (after login there is a beneficiary call. inspect it.) 
   ![enter image description here](https://github.com/aaravpandya/CowinBot/blob/main/images/bene_id.JPG?raw=true)
 - District id (search for your city and inspect it.)
 ![enter image description here](https://raw.githubusercontent.com/aaravpandya/CowinBot/main/images/district_id.JPG)
 - Also remember to change date.
 - Absolute path to a html file. Just make an html file.

Put them in the script and run. ([learn](https://realpython.com/run-python-scripts/) how to run python scripts)

Script runs infinite loop; as soon as it finds a slot it opens a captcha for you in an edge window. Solve the captcha and enter it in the command line. That is the only human input required and thus the only pain point in the process.

## Few important points

 - Token is valid for 15 mins. Plan ahead.
 - Automating OTP and Captcha is not possible. For captcha I would recommend setting a dual monitor setup or have edge and command line side by side. Can save a second or two. 
 - Centers are not selectable. Trying to minimise time to submission here. It selects the first center it finds. Please keep that in mind. 
 - Slot_index is 0 by default. In my city i get options for 4 slot timings. But it can vary I guess. You can try setting it to a different time if thats what you want. But that can be error prone as maybe the array returned doesnt have that many values.
 - Understand the time when you want to run the script. In my city, slots generally open around 5 PM. I would start running this around  4:58. Do prep before hand.
 - Dont mess with headers. Seems like they try to do validation for user agent. 
 - Was able to book a slot in what seemed like 2-5 seconds. Depends on your computer and internet speed as well.
 - Let me know if this works out for you.
 - Good luck 👍.
