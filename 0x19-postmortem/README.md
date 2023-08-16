
![images](https://github.com/davidgregs87/alx-system_engineering-devops/assets/108700012/82b29b5e-3503-4cd6-8d16-5b3d6e2faaf9)

# Postmoterm/Incident Report based on 0x17-web_stack_debugging_3

## Issue Summary

This issue started on Wednesday, 9th August at 3:45pm(GMT + 1 (WAT)) - Saturday, 12th August at 5:55am(GMT + 1 (WAT)) The resultant effect of this issue lead to the unavailability of our services, more than 50% of our clients could'nt access our services worldwide. The root cause of this issue was as a result of mis-configuration in our server web-13234-01 that made it impossible for users to access our services.

## Timeline

This issue was detected on the 9th August at 3:45pm(GMT + 1 (WAT)) with the help of our monitoring alert(PagerDuty) which sent an alert to the available person on-call and the person on-call notified other team members also.

I was also a member of the persons that was notified, so we came together and started debugging. Firstly, we went through the log files if there could be any help from there, then we went down into the stack to check the configuration files for our webserver because our assumption was that may any part of the configuration file must have mistakenly be tampared with or might have been deleted.

Another misleading/debugging path that were taken was that we even had to delete the copy the all files inside the /var/www/html folder to somewhere else and delete the whole entire webserver "I think we went too extreme lol :)" and installed the same webserver but this time a new one.

When we put up everything back on and try accessing the server, it still didn't work! So finally we had to use "strace" to do the debugging this time around and we found out the main cause of the issue.

## Root Cause/Resolution

The root cause of the whole issue was a typo in one of the php files in the /var/www/html which the strace command helped us in finding it out. So we fix it by simply writing a puppet manifest file that executes a 'sed' command by replacing the typo with the correct field, we now restarted the server and try accessing the server and VOILA! it worked.

## Corrective and Preventative Measures

When it comes to typo errors i personally don't think anybody is above it, we make typo errors everyday. So this issue can be prevented by testing the files that would be used to serve the webpages of our services on a different machine first, before deploying it to the main server. This will avoid the same mistake all over again. Because "Failing is fine, but failing twice because of the same issue is not acceptable".

![download](https://github.com/davidgregs87/alx-system_engineering-devops/assets/108700012/7fbc9754-f59a-4fd9-a398-9c0a21940f63)

