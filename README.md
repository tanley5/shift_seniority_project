# shift_seniority_project

## Purpose

The purpose of this project is for the admin to be able to send out a form for email recipients to fill. In this example, the admin is sending out a set of shifts to be filled.

## Explanation

In this project, the admin will be able to submit a list of emails and the avialable shifts for the emails to choose from. The admin will be able to fix part of the data (CRUD), before running the script. Once the script is activated, no data should be changed. The individuals in the email list will receive a link to choose which shifts they want. Upon completion, the email recipients will be redirected to a "Thank You" page. The admin will have visibility of all the changes in the shifts.

## Lessons Learned

I learned how to create external functions, not related to django, to accomplish tasks in Django. I learned the use of 'threads' in running functions in the background. I learned how to use django emails using 'SMTP'. I learned how to create views and urls outside of django specified files.

## Other ways to expand the project

The next step is to create a function to send the form according to the email recipient's seniority. Once completed, the form will go to the next email recipient, etc.

Another thing that we can add is to remove completed forms automatically. Currently, when the forms are completed, the admin must remove the forms manually. Failing to do so will eat up computer resources.
