## List of best practices CI using github actions
- Keep Actions minimal
- Don't install unnecessary dependencies
- Never hardcode secrets
- Limit the scope of environment variables to as low as possible
- Ensure every repository contains a CI/CD workflow
- Store authors in Action metadata to promote code ownership
- Don’t use self-hosted runners in a public repository
- Use certified actions.

## List of best practices CI using Jenkins
- Use declarative pipelines
- Use docker agent
- Use secrets to manage your credentials
- Use env variables to reuse them in multiple locations
- Cache docker layers for faster builds
- Parallel running of testing and linting
- Setup A Different Job/Project For Each Maintenance Or Development Branch Created
- Prevent Resource Collisions In Jobs That Are Running In Parallel
- Avoid Complicated Groovy Codesode In Pipelines

## References:
+ https://www.datree.io/resources/github-actions-best-practices