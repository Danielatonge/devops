## List of best practices python
- Use requirements.txt file for Python packages.
- Use Production ready framework - FASTAPI
- Use linters to fix little mistakes, stylistic inconsistencies, and dangerous logic
- List all dependencies and their version for reproducible builds
- Allow to configure the app using environment variables, as recommended by the twelve factor app
- Containerize application using Docker containers
- Use Jinja templates instead of hardcoding html strings in the source code
- Include .gitignore for skipping irrelevant files in the Git VCS
- Include .dockerignore for reducing docker context size

## References:
+ https://dzone.com/articles/7-best-python-code-review-tools-recommended-by-dev

## Unit Test
+ The function ```test_read_root()``` tests the root endpoint, sending a get request to ``` "/" ``` route and making sure the response status code is ```200``` i.e succesful

## Best practices on Code Testing
- Testing should be subdivided into units and each testing unit should focus on one tiny bit of functionality and make sure it is correct.
- Testing units should be independent i.e each testing unit must be able to run alone, regardless of the order that they are called.
- Each test must be loaded with a fresh dataset and may have to do some cleanup afterwards
- It is important to make tests that run fast. Rarely, tests can't be fast because of some constrain. Keep these heavier tests in a separate test suite that is run by some scheduled task.
- When developing a function inside a module, run this function's tests frequently, ideally automatically when you save the code.
- Make sure to run the full test suite before and after coding sessions.
- Implement a hook that runs all tests before pushing code to a shared repository
- On interruption of a development session, write a broken test about what you want to develop next.
- During debugging, the first step is to write a new test pinpointing the bug.
- Use long and descriptive names for testing functions.
- The purpose of a given test should be crystal clear.



## References:
+ https://docs.python-guide.org/writing/tests/