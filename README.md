# gRecaptcha4py
A straight forward python module for Google's Recaptcha v2 a.k.a g-recaptcha. This module is the back-end or server-side integration that is needed to if the user is not a robot.

###Usage
1. Import grecaptcha class from gRecaptcha4y
````````````````
from gRecaptcha4py import grecaptcha
````````````````

2. Create a new instance of grecaptcha class with parameters of your secret code, the response string from user, the user remote IP.
`````````````````
captcha = grecaptcha("secret", "response", "remoteip")
`````````````````

3. Check the result by checking out success and error_code attribute. Result should be the same as the one on Google's Recaptcha Docs.
`````````````````
if not captcha.success:
  print captcha.error_code
`````````````````

