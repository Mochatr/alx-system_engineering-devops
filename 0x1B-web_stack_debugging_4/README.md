# Webstack Debugging Project

![Webstack debugging](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/313/frdkCrb.jpg)

## Overview

This project focuses on debugging and managing a web stack using Puppet manifests. The aim is to ensure a consistent and error-free environment setup through the use of automated Puppet scripts.

## Requirements

- **Operating System**: Ubuntu 14.04 LTS
- All files are interpreted on Ubuntu 14.04 LTS.
- All manifest files should end with a newline.
- A `README.md` file is present at the root of the project directory.
- Puppet manifests must pass `puppet-lint` version 2.1.1 without any errors.
- Puppet manifests must run without error.
- The first line of each Puppet manifest is a comment explaining the purpose of the manifest.
- Puppet manifest files end with the `.pp` extension.
- Files are checked with Puppet v3.4.

## Installation

### Installing Ruby and Puppet-lint

To set up your environment for running and testing Puppet manifests, follow these steps:

```bash
sudo apt-get update
sudo apt-get install -y ruby
sudo gem install puppet-lint -v 2.1.1
