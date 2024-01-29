# Web Stack Debugging and Load Balancer Configuration

## Concepts
In this project, we delve into the following concepts:

- **Load Balancer:** A crucial component for distributing incoming network traffic across multiple servers to ensure no single server bears too much load.
- **Web Stack Debugging:** The process of troubleshooting and resolving issues within the layers of the web stack to ensure optimal performance and reliability.

## Background Context
To enhance our web stack's redundancy and reliability, we've introduced two additional servers:
- `gc-[STUDENT_ID]-web-02-XXXXXXXXXX`
- `gc-[STUDENT_ID]-lb-01-XXXXXXXXXX`

The goal is to double the number of web servers, accommodating more traffic and maintaining service even if one server encounters issues.

## Project Objective
The primary objective is to configure these new Ubuntu servers using Bash scripts, automating the setup process to meet the specified requirements. This includes the integration and configuration of a load balancer and the necessary debugging of the web stack.

## Resources
Before proceeding, it's recommended to go through the following materials:
- [Introduction to Load-Balancing and HAProxy](#)
- [Understanding HTTP Headers](#)
- [HAProxy Packages for Debian/Ubuntu](#)

## Requirements

### General
- **Editors:** Use vi, vim, or emacs for editing files.
- **Server Environment:** Scripts should be tested and will be interpreted on Ubuntu 16.04 LTS.
- **File Endings:** Ensure every file ends with a new line.
- **Documentation:** Include a README.md file at the root of the project folder.
- **Script Permissions:** All Bash script files must be executable.
- **Shellcheck Compliance:** Scripts must pass Shellcheck (version 0.3.7) without errors.
- **Script Headers:**
  - The first line of each Bash script must be `#!/usr/bin/env bash`.
  - The second line should include a comment describing the script's purpose.

### Specific Scripts
**Note:** Each script should be well-commented, clearly explaining what it does and how it achieves the project's objectives.

1. **Load Balancer Setup:** Script to configure the `gc-[STUDENT_ID]-lb-01-XXXXXXXXXX` server with the necessary load balancing settings.
2. **Web Server Setup:** Scripts to prepare the `gc-[STUDENT_ID]-web-02-XXXXXXXXXX` server, ensuring it meets the web stack requirements and integrates well with the load balancer.
