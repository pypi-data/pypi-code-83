#!/usr/bin/env python
# coding: utf-8

# In[17]:


import smtplib
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 
import logging





logger = logging.getLogger()




def appendAttachments(file,msg):
    # open the file to be sent  
    
    attachment = open(filename, "rb") 
      
    # instance of MIMEBase and named as p 
    p = MIMEBase('application', 'octet-stream') 
      
    # To change the payload into encoded form 
    p.set_payload((attachment).read()) 
      
    # encode into base64 
    encoders.encode_base64(p) 
       
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
      
    
    # attach the instance 'p' to instance 'msg' 
    msg.attach(p)
    
    return msg





def send_mail(username, password, recipient_list, subject, message = '', files = [], filenames = []):
    """
    This takes into input parameters as shown below

    Args:
        username: required
            type: str
            The email id of outlook from which one needs to send an email.
        password: required
            type: str
            Password of outlook email for authentication.
        recipient list:
            type: list
            The recipients enclosed in a list
        subject: required
            type: str
            The subject line of the mailer
        message: optional
            type: str
            Any text to be displayed in body of the mailer. Please provide absolute local path of the attachment.
        files: optional
            type: Any
            Attachments to be uploaded in the mailer. Note mail restrictions of memory still applies.
        filenames: optional
            type: List of str
            Applicable only when files is not empty.
            Pass on the list containing names of files one wants to display in the mail body. By default will show processed absolute path names.
            

    Returns:
        A mail is sent to intended recipients. Can be used to automate sending of mails/reports.

    Raises:
        KeyError: To be updated.
    """
    msg = MIMEMultipart()
    msg['From'] = username
    msg['To'] = ', '.join(recipient_list)
    msg['Subject'] = subject
    if message != '':
        msg.attach(MIMEText(message))
    if len(files) > 0:
        for i in files:
            msg = appendAttachments(i,msg)
    
    
    
    #Setting the threshold of logger to DEBUG
    logger.setLevel(logging.DEBUG)
    logger.info('Sending mail')
    try:
        mailServer = smtplib.SMTP('smtp-mail.outlook.com', 587)
        mailServer.ehlo()
        mailServer.starttls()
        mailServer.ehlo()
        mailServer.login(username, password)
        mailServer.sendmail(username, recipient_list, msg.as_string())
        mailServer.close()
        logger.info('Mail sent.')
    except Exception as e:
        logger.error(e)
    
        


# In[ ]:




