## List of best practices for Docker
* Use lightweight images based on alpine distribution
* Avoid unnecessary privileges
- Use docker layer caching. First install dependencies, then copy source code
- Use multi-stage build for complied applications
- Scan the images to detect potential problems and security issues. It is recommended to scan images every week.
- Support configuration of the container via environment variables
- Use docker-compose for easier runs
- Don’t install unnecessary packages to reduce complexity, dependencies, file sizes, and build times
- Use linting to detect bad practices in the Dockerfile. The most popular linter is hadolint.
- Include .dockerignore for reducing docker context size
- Run binaries in containers under non-root users
- Make included binaries non-writable

## References
- https://docs.docker.com/develop/develop-images/dockerfile_best-practices/
- https://sysdig.com/blog/dockerfile-best-practices/