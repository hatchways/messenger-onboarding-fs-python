## General Instructions

For this project, you are provided a starting code for a messenger application and are to build on this starting code by adding new features. The starting code is for the application described in the section below, and you can find your assigned work on the Issues tab of this repository. Please open a **single pull request** with all of the changes needed to implement the features described in the issue, then return to the [Hatchways dashboard](https://app.hatchways.io/app#/dashboard/assess/assessment-interview) to mark your assessment as completed.

Note that this repository contains some tests that will run on GitHub actions once you create a pull requests. These simple tests will ensure that your app is running as expected and that you have completed the basics of the assigned tasks. You will not be able to mark your assessment as completed until these tests pass. Please **do not modify** these tests, as they exist to help ensure your code passes the basic requirements of the assessment. There are additional, more thorough tests that will run once you mark your assessment as completed. After submitting, you will be able to see the high level results but not the specific details of these tests.

We will use [this rubric](https://drive.google.com/file/d/1sMvFvsIDI22rWINk6Vzxnhcq0DbrTe4H/view?usp=sharing) to evaluate your submission. Please note that if your submission does not attempt to complete all of the requirements, or does not pass our plagiarism screening, we will be unable to provide feedback on it. Please contact hello@hatchways.io if you have any questions or concerns.

## Introduction to this Application

You will be modifying an existing project containing a messenger application. The following functionality has already been implemented on both the frontend and the backend:

- User Registration
- User Login
- Conversation Display

Note: the rest of the application may not be entirely complete and bug-free in terms of both functionality and styling. Please do not fix these issues and only work on the exact tasks outlined in your ticket.

## System Requirements

We recommend using Python 3.8 or 3.9.

## Initial Setup

Create a .env file in the [server](./server) directory, and copy the contents from [.env.sample](./server/.env.sample).

In the server folder, install dependencies (you may want to use a virtual environment):

**Note:** if you're running Python 3.10, you might run into an issue with the Greenlet dependency. We recommend downgrading to Python 3.8 or 3.9 for this project.

```
cd server
pip install -r requirements.txt
```

In the client folder, install dependencies:

```
cd client
npm install
```

### Running the Application Locally

In one terminal, start the front end:

```
cd client
npm start
```

In a separate terminal, start the back end:

```
cd server
python manage.py runserver
```

### Unit Tests
Your repository contains a non-comprehensive set of tests used to determine if your pull request has met the basic requirements of the task given to you. These tests will fail before you complete your task and should NOT be modified unless specified in your GitHub issue. If these tests continue to fail when you're ready to submit, make sure your solution has been tested thoroughly to make sure you haven't missed anything.

To run these tests for the server, run `python manage.py test` from the `server` directory.

To run these tests for the client, first start the front end in one terminal, then in a separate terminal, run `npx cypress run` from the `client` directory.


### Linting
This project is set up to use [Prettier](https://prettier.io/) for the client code and [black](https://github.com/psf/black) for the server code. 

To format the client code:
```
cd client
npx prettier --write .
```

To format the server code:
```
cd server
black .
```

## Database

### Setup

Note: No database setup should be required to get started with running the project.

This project uses SQLite, which stores your tables inside a file.

### Seed Data

We've included sample data that the application has been configured to use. If you want to re-seed the database, you can use the following commands:
```
cd server
python manage.py makemigrations
python manage.py migrate 

python manage.py shell
from messenger_backend.seed import seed
seed()
exit()
```
seed.py can be referenced to see what the sample data is. Viewing the database file itself is not required to complete your tasks, but if you would like to, an application like DB Browser for SQLite can be used.
