import urllib2, urllib, json

VERIFY_URL = "https://www.google.com/recaptcha/api/siteverify"

class grecaptcha(object):
    def __init__(self, secret, response, remoteip):
        if secret and response and remoteip and len(secret) and len(response):
            self.secret = secret
            self.response = response
            self.remoteip = remoteip
            
            request = urllib2.Request (
                url = VERIFY_URL,
                data = urllib.urlencode({
                    "secret": secret,
                    "response": response,
                    "remoteip": remoteip
                }),
                headers = {
                    "Content-type": "application/x-www-form-urlencoded",
                    "User-agent": "gRecaptcha4py - Python Module"
                    }
                )
            
            APIresponse = urllib2.urlopen(request)
            
            resp = json.load(APIresponse)
            
            self.success = resp["success"]
            self.error_codes = resp["error-codes"]

        else:
            self.success = False
            if(not secret):
                self.error_codes = "missing-input-secret"
            elif(not response):
                self.error_codes = "missing-input-response"
            elif(not remoteip):
                self.error_codes = "missing-input-remoteip"
            else:
                self.error_codes = "something else"