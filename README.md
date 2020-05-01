# Product Stock Checker Application

This is a Python application that is a product stock checker that currently checks the availability of products from the following retailers.

- Target
- Walmart
- Bj's

## Purpose of Application

This application was built out of the need to have a way to check for needed products during the Covid
situation in order to limit the exposure evident when going out in quarantine. The system is designed
items based on a list of products contained in an excel document.

## Send Mail Functionality

The application uses Python's sendmail functionality for notifications to gmail users for when a product becomes
available. In order to use sendmail with gmail you need to enable less secure apps. You can visit the 
following url in order to enable less secure apps.

https://myaccount.google.com/lesssecureapps

## Configuration

The files include config_template.py. Rename the file to config.py and update the following information
based on your required needs.
- GMAIL_USERNAME = "Enter your Gmail username"
- GMAIL_PASSWORD = "Enter your Gmail Password"
- GMAIL_EMAIL = "Enter your Gmail email address"

You can set what stores to check for products buy adjusting the following values.
- TARGET = True
- WALMART = True
- BJS = True
- COSTCO = False  # Not ready for release
- AMAZON = False  # Not ready for release

Set the time delay for checking default it every 15 minutes
- DELAY_IN_MINUTES = 5

Used if you want to use virtual displays for running on a server
- USE_VIRTUAL_DISPLAY = False

Below will run chrome browser in the background
- HEADLESS_MODE = True

Enable as true if you would like to un in a multithread mode
- MULTI_THREAD = True


