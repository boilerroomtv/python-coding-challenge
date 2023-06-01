## Technical Test Brief

### Task 1:

Write a program that performs the following tasks:

1. Handle a CSV file:
   - Read the CSV file, which can be of any length.
   - Validate all cells in the CSV file for errors.

2. Find or insert a user into a database:
   - Connect to a database and perform operations to find or insert a user.
   - Each user must have a unique UUID using a salt/hash.

3. Post user data to an external API:
   - Send user data to an external API.
   - Note that the API can only accept chunks of 75 users at a time.

Additional requirements:
- The program should be optimized for performance.
- You should write tests to accompany your program.

### Task 2:

In addition to completing Task 1, provide suggestions for improving the program and handling the limitation of the external API that only accepts 75 users at a time. Consider the following points:

1. Handling the 75 user chunk limitation:
   - Describe how you would efficiently split the user data into chunks of 75 users and send them to the API.
   - Explain any strategies or algorithms you would employ to handle this limitation effectively.

2. Other systems or tools:
   - Identify any additional systems, tools, or technologies you would use to enhance the program's performance or functionality.
   - Justify your choices and briefly explain how these systems or tools would complement the existing solution.

   Note: Provide clear, concise answers and focus on the technical aspects of the program, including scalability, error handling, and integration with external systems.