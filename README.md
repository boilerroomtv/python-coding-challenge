# Boiler Room Python Coding Challenge

Create a script that can import users from a CSV into a database table.

## Challenge

Update `main.py` so that it does the following:

1. Parse a CSV file of users:
   - Read the CSV file, which can be of any number of rows up to 100000.
   - Validate fields for import:
      -  Email addresses must be valid
      -  Tags must be alphanumeric with hyphens
   - See `example.csv` for the CSV format.

2. Find or insert users from CSV into an SQLite database:
   - Setup the database.
   - Connect to a database and perform operations to update or insert a user.
   - Dedupe on email address.
   - Each user must have a unique UUID using a salt/hash.

3. Post user data to an external API:
   - Post all imported users to fake endpoint.
   - Use endpoint `https://jsonplaceholder.typicode.com/posts`.
   - Endpoint body format should be `{users: [{email, uuid, tags: ['tag1', 'tag2']}]}`
   - Note that the API can only accept chunks of 75 users at a time.

## Requirements
- Your program should be command line only.
- The program should be optimized for performance.
- You should write tests to accompany your program.
- Setup your program with dependencies.
- Make sensible assumptions on validation.
- The program should have clear logs.
- Write instructions on how to run your program in markdown.

## Delivery
- this folder is a git repo, commit your changes to it locally before zipping it up and sending to us (we would like to see your working)
- make a note of any assumptions you've made during the build
