## Boiler Room Python Coding Challenge

### Insert users from a CSV into a database table

Update `main.py` so that it does the following:

1. Parse a CSV file of users:
   - Read the CSV file, which can be of any number of rows up to 100000.
   - Validate all cells in the CSV file for errors.
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

Requirements:
- Your program should be command line only.
- The program should be optimized for performance.
- You should write tests to accompany your program.
- Setup your test with any required dependencies.
- Make sensible assumptions on validation.
- The program should have clear logs.
- Write instructions on how to run your program in markdown.
