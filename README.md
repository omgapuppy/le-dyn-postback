# le-dyn-postback
Sends Dyn email bounces and complaints to Logentries

## Obtain log token(s)
1. Log in to your Logentries account
2. Add a new [token based log](https://logentries.com/doc/input-token/)

## Configure the listener

Requires Logentries Python library and Python Flask to be installed.
```pip install logentries```
```pip install Flask```

1. Replace the ```PORT``` value with an open port
   in your environment
2. Set an ENV VAR ```LOGENTRIES_TOKEN=your-le-token```
3. Run ```dyn-listener.py```

## Configure Dyn Postback URLs
1. Log into your Dyn account
2. Open the the Integration view
3. Scroll to the Postback URLs section of the Integration view
4. Enter the Postback URLs for your email.
   * This script supports **Bounce** and **Complaint** types

### Bounce Postback URLs:
When an email you send through Email Delivery bounces, Email Delivery will
record the bounce. If a bounce postback URL is set in your preferences,
it will also post the requested information back to you automatically
via that URL.

Enter the bounce postback URL in the following format:
```
http://SCRIPT_HOST_IP:PORT/bounce?e=@email&r=@bouncerule&t=@bouncetype&dc=@diagnostic&s=@status
```

### Spam Complaint Postback URL:
When a recipient clicks “Report Spam” in their email client for a message you
sent them, their email provider sends a message back to Email Delivery notifying
them of this. Email Delivery records the complaint, and if the spam complaint
postback URL is set, it also posts the information back to you via the specified URL.

Enter the complaint postback URL in the following format:
````
http://SCRIPT_HOST_IP:PORT/complaint?e=@email
````
