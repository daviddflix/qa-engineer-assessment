# Task: Python Server Testing

You are tasked with designing and implementing a test plan for a Python-based RESTful API server that interacts with cryptocurrency data. The server provides endpoints to fetch data (simulating the Binance API), save data to a database, and retrieve saved data.

## Server Specifications

The server is implemented using Flask and SQLAlchemy. It provides the following endpoints:

1. `/fetch` (GET): Simulates fetching cryptocurrency data based on name and symbol.
2. `/save` (POST): Saves cryptocurrency data to the database.
3. `/retrieve` (GET): Retrieves all saved cryptocurrency data from the database.

## Requirements

1. Set up the testing environment:
   - Install the required dependencies from `requirements.txt`.
   - Run the server using `python index.py`.

2. Design and implement a comprehensive test plan that covers:
   - Functional testing of all endpoints
   - Integration testing with the database
   - Error handling and edge cases
   - Performance testing

3. Implement your tests using a Python testing framework of your choice (e.g., pytest, unittest).

4. Your test suite should cover the following scenarios:
   - Successful data fetching with valid parameters
   - Error handling for invalid parameters in the fetch endpoint
   - Successful data saving with valid data
   - Error handling for invalid data in the save endpoint
   - Successful data retrieval
   - Database consistency checks

5. Implement mocking for the simulated Binance API call in the `/fetch` endpoint.

6. Design and implement performance tests to evaluate the server's response time and throughput.

7. Provide a detailed report of your testing process, including:
   - Test cases and their results
   - Any bugs or issues discovered
   - Suggestions for improving the server's reliability and performance


Use the submission template to document your approach, methodologies, and test results.