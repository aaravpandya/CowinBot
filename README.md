# CowinBot
The goal is to automate taps/clicks. You cannot bypass captcha and that still slows you down. 

You will need the following before running the script. Use the network tools on your browser to get them. 

 - Bearer token ( in authorization header )
 - Beneficiary id (after login there is a beneficiary call. inspect it.)
 - Absolute path to a html file. Just make one. 

Put them in the script and run. 

Script runs infinite loop; as soon as it finds a slot it opens a captcha for you in an edge window. Solve the captcha and enter it in the command line. That is the only human input required and thus the only pain point in the process.

## Few important points

 - Token is valid for 15 mins. Plan ahead.
 - Automating OTP and Captcha is not possible. For captcha I would recommend setting a dual monitor setup or have edge and command line side by side. Can save a second or two. 
 - Centers are not selectable. Trying to minimise time to submission here. It selects the first center it finds. Please keep that in mind. 
 - Slot_index is 0 by default. In my city i get options for 4 slot timings. But it can vary I guess. You can try setting it to a different time if thats what you want. But that can be error prone as maybe the array returned doesnt have that many values.
 - Understand the time when you want to run the script. In my city, slots generally open around 5 PM. I would start running this around  4:58. Do prep before hand.
 - Dont mess with headers. Seems like they try to do validation for user agent. 
 - Good luck 👍.
