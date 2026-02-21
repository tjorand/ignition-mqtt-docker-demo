# IgnitionAssesment
End-to-end MQTT demo system using Ubuntu, Docker, and Ignition SCADA, showcasing broker/client architecture, real-time messaging, and HMI integration.

REQUIREMENTS 

Ignition Software from InductiveAutomation https://inductiveautomation.com/downloads
MQTT Engine Module from CirrusLink https://inductiveautomation.com/downloads/third-party-modules/8.1.43
MQTT Transmission Module from CirrusLink https://inductiveautomation.com/downloads/third-party-modules/8.1.43

PROJECT OUTLINES 

The purpose of this demo is to create a simple framework for end to end MQTT communication using Ubuntu, Docker, and Ignition SCADA, showcasing broker/client architecture, real-time messaging, and HMI integration. 

The MQTT broker will be hosted on the Ignition Gateway using the MQTT modules above. The Ignition HMI project will display a set of sample user inputs, which will publish to the broker. On this same machine, there will be a docker container that will act as a client to the MQTT broker. The container will then pull the user inputs, and depending on the values, will then publush a set of sample data back to the broker. The HMI will pull the sample data from the broker, and display it to the user. 



