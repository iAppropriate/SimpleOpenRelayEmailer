#!/usr/bin/python
# -*- coding: utf-8 -*-

import smtplib

sender = 'noreply@example.com'
receivers = ['john.smith@example.com']

message = """From: noreply <noreply@example.com>
To:  John Smith <john.smith@example.com>
Subject: <SUBJECT>

<BODY>
"""

try:
   smtpObj = smtplib.SMTP('<MAILSERVER>', 25)
   smtpObj.sendmail(sender, receivers, message)         
   print "Successfully sent email"
except SMTPException:
   print "Error: unable to send email"