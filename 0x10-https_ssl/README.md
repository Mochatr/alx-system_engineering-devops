# 0x10. HTTPS SSL

## Concepts
For this project, the following concepts need to be understood:

- DNS
- Web stack debugging

## Background Context 

HTTPS (Hypertext Transfer Protocol Secure) is used to securely transfer information over the internet. It utilizes SSL/TLS protocol to encrypt communication between a client and server.

The two main elements that SSL provides are:

- **Confidentiality** - Encrypts data in transit so it cannot be read by third parties
- **Authenticity** - Verifies the identity of the server and client through certificates to prevent man-in-the-middle attacks

SSL termination means decrypting HTTPS traffic before it reaches the web servers. A load balancer configured for SSL termination handles encrypting and decrypting traffic.

## Learning Objectives

At the end of this project, the following should be understood:

- What is HTTPS SSL 2 main roles
- What is the purpose encrypting traffic  
- What SSL termination means

## Requirements

### General
- Allowed editors: vi, vim, emacs
- All files should end with a new line  
- A README.md file included at the root directory
- All Bash scripts must be executable and pass Shellcheck
- Bash scripts start with `#!/usr/bin/env bash` and have a comment explaining what they do

### Tasks

1. Configure your domain zone so that the subdomain www points to your load-balancer IP (lb-01).
2. Add other subdomains for lb-01, web-01, and web-02. 
3. Create a Bash script that displays DNS record information for subdomains.
