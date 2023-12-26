# Infrastructure Overview

## Additional Elements

### Firewalls
- **Purpose:** Added for enhanced security to filter and control incoming/outgoing traffic.
- **Function:** Provide layered defense against potential threats and unauthorized access.

### HTTPS Traffic
- **Reasoning:** Serves traffic over HTTPS with an SSL certificate to ensure encryption and secure communication.
- **Purpose:** Prevents data interception, ensuring confidentiality and integrity during transmission.

### Monitoring
- **Usage:** Utilized to track system performance, detect anomalies, and identify potential issues.
- **Data Collection:** Monitoring tools gather data on server health, traffic patterns, and resource utilization.

### Monitoring Tool
- **Data Collection Method:** The monitoring tool, like Sumo Logic, collects data by aggregating logs, metrics, and system information.

### Monitoring Web Server QPS
- **Process:** Configure monitoring tools to track and measure incoming query rates over time.

## Infrastructure Issues

### SSL Termination at Load Balancer
- **Issue:** Termination at this level can increase load and processing time due to the added encryption and decryption steps.

### Single MySQL Server for Writes
- **Issue:** Having only one server capable of accepting writes poses a single point of failure, risking downtime or data loss if it fails.

### Identical Server Components
- **Problem:** Uniform components across servers may create a common vulnerability, risking widespread issues if a flaw affects all servers simultaneously.

