# Configuration Management with Puppet

## Overview
This project focuses on Configuration Management using Puppet in an Ubuntu 20.04 environment. It aims to create and maintain consistent state configurations for software and systems through Puppet manifests.

## Prerequisites
- Ubuntu 20.04 LTS
- Puppet 5.5
- Ruby (with specific packages: `ruby-augeas`, `ruby-shadow`)
- Puppet-lint 2.1.1

## Environment Setup
1. Install Ruby and its packages:
   ```bash
   sudo apt-get install -y ruby=1:2.7+1 --allow-downgrades
   sudo apt-get install -y ruby-augeas
   sudo apt-get install -y ruby-shadow

