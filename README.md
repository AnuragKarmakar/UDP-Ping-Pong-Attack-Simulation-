# UDP-Ping-Pong-Attack-Simulation-
Simulating and mitigating UDP Ping Pong attacks to demonstrate network vulnerabilities and defense strategies.

## Repository Description

This repository provides a comprehensive simulation of the UDP Ping Pong Attack, demonstrating how an attacker exploits UDP's connectionless nature by spoofing packets to cause network congestion and potential denial-of-service (DoS). It includes scripts, explanations, and mitigation strategies to understand, reproduce, and prevent such attacks.

## Project Overview

### Objective

The goal of this project is to simulate, demonstrate, and provide mitigation strategies for a UDP Ping Pong attack in a controlled virtual environment.

### Network Topology

* **Victim (10.9.0.5)**: Automatically responds to UDP packets.
* **Server (10.9.0.2)**: Automatically responds to UDP packets.
* **Attacker (10.9.0.25)**: Sends spoofed UDP packets to initiate the attack.

### Tools & Technologies

* Docker
* Scapy
* Socket Programming
* Python
* Wireshark

## Python Scripts

### attack.py

* Sends a spoofed UDP packet from the victim's IP to the server.

### server-listener.py

* Acts as a UDP server listening and responding to packets with "Server - Pong."

### victim\_listener.py

* Acts as a UDP client listening and responding with "Victim-Ping."

## How to Run the Simulation

1. **Setup Docker Environment**:

   * Configure Docker containers for Attacker, Server, and Victim hosts.

2. **Execute Python Scripts**:

   * Run `server-listener.py` on the server.
   * Run `victim_listener.py` on the victim.
   * Execute `attack.py` from the attacker to start the UDP Ping Pong attack.

3. **Monitor the Attack**:

   * Use Wireshark to capture and analyze network traffic.
   * Observe increased network and resource usage demonstrating the DoS impact.

## Mitigation Strategies

* **Prevent Spoofing**: Configure firewall rules to block spoofed UDP packets.
* **Rate Limiting**: Implement rate-limiting on UDP responses.
* **Disable Unnecessary Services**: Shut down UDP services that aren't required.
* **Monitoring**: Use network monitoring to detect unusual traffic patterns early.

## Project Reflection

This simulation provides insights into the vulnerabilities of UDP services and emphasizes the importance of robust network defense mechanisms.
