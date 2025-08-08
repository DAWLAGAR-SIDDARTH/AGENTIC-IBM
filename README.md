# 🚀 AI-Driven Smart Traffic Light System

## 🌟 Project Overview

The **AI-Driven Smart Traffic Light System** is an innovative solution designed to combat urban traffic congestion. By moving away from outdated fixed-timer traffic signals, this project leverages modern AI and Machine Learning to create an adaptive system that responds to real-time traffic conditions. The system's core function is to analyze live video feeds from existing CCTV cameras to dynamically adjust traffic light timings. This not only improves traffic flow efficiency but also reduces travel times, lowers fuel consumption, and cuts down on harmful emissions, directly contributing to Sustainable Development Goal 11: Sustainable Cities and Communities.

This project was developed using a robust suite of IBM Cloud tools, ensuring scalability, reliability, and seamless integration with smart city infrastructure.

## ✨ Features

The system's key functionalities include:

* **Real-time Traffic Density Detection:** Utilizes computer vision to count and classify vehicles from live video feeds.

* **Dynamic Signal Timing Adjustments:** An AI model adjusts traffic light durations based on current traffic density to optimize flow.

* **Emergency Vehicle Prioritization:** Detects emergency vehicles and gives them priority clearance to ensure timely responses.

* **Multi-Intersection Coordination:** Allows communication between multiple intersections to optimize city-wide traffic flow, preventing bottlenecks.

* **Predictive Congestion Management:** Uses historical and real-time data to forecast congestion and proactively manage traffic.

* **Existing Infrastructure Compatibility:** Designed to integrate with standard CCTV cameras and traffic controllers via APIs.

## ⚙️ Workflow

The system operates through a continuous, intelligent feedback loop:

**Data Collection** 🎥
Live video feeds are streamed from traffic cameras.
⬇️
**Vehicle Detection** 🚗
A YOLOv8 computer vision model processes the video to detect and count vehicles, providing real-time traffic density data.
⬇️
**Intelligent Decision-Making** 🧠
A reinforcement learning model analyzes the traffic density and determines the optimal signal timing for each intersection.
⬇️
**Signal Adjustment** 🚦
The AI model communicates the new timings to the traffic controllers via a secure API.
⬇️
**Performance Monitoring** 📈
A real-time dashboard provides insights into traffic flow, congestion trends, and overall system performance.

## 🏗️ Architecture

The project's architecture is a modular, cloud-based system with the following key components:

* **Data Ingestion Layer:** Streams live video data from CCTV cameras.

* **Computer Vision Module:** A YOLOv8 model for real-time object detection and vehicle counting.

* **AI/Decision-Making Core:** A reinforcement learning model that serves as the "agent" to determine optimal traffic signal timings.

* **Deployment & Hosting:** The AI models are trained and deployed as RESTful APIs using IBM Watson Studio and IBM Cloud.

* **API Management:** IBM API Connect provides secure endpoints for communication between the AI models and municipal traffic systems.

* **Monitoring & Analytics:** IBM Cognos Analytics is used to create a dashboard for visualizing traffic data and system performance.

* **Data Storage:** Historical and training data are stored in IBM Cloud Object Storage.

## 💻 Tech Stack

The project leverages a modern and scalable technology stack:

* **Programming Language:** Python

* **Computer Vision:** YOLOv8

* **Machine Learning:** Reinforcement Learning models

* **Cloud Platform:** IBM Cloud

* **APIs:** RESTful APIs for communication

* **Data Storage:** IBM Cloud Object Storage

## 🛠️ IBM Tools Used

This project is a showcase of several powerful IBM tools, utilized to create a robust and scalable solution:

* **IBM Watson Studio:** The central hub for developing, training, and testing the AI and ML models (YOLOv8 and the reinforcement learning model).

* **IBM Cloud Object Storage:** Used for securely storing the large datasets, including historical traffic videos and images, necessary for model training.

* **IBM Watson Machine Learning:** Deploys the trained models as production-ready APIs, enabling real-time predictions for the traffic control system.

* **IBM API Connect:** Provides a secure and managed way to expose the AI model APIs to the municipal traffic system, ensuring safe communication.

* **IBM Cognos Analytics (Optional):** Can be used to build an interactive dashboard for performance monitoring and insights.

* **IBM Streams (Optional):** Can be incorporated for high-throughput, low-latency processing of continuous video feeds.

## 🚀 Setup Instructions

To get a local version of this project up and running for development or testing, follow these steps.

### Prerequisites

* Python 3.x

* A valid IBM Cloud account with access to Watson Studio, Cloud Object Storage, and Watson Machine Learning.

* `pip` for installing Python dependencies.

### Configure IBM Cloud Access

* Set up your IBM Cloud credentials as environment variables or in a configuration file, as per the best practices for your chosen IBM services.

### Model Training & Deployment

* Follow the instructions to upload your training data to IBM Cloud Object Storage.

* Use IBM Watson Studio to train and deploy your YOLOv8 and reinforcement learning models.

* Note down the API endpoints for your deployed models.

### Run the System

* Update the configuration files in the project with your specific model API endpoints.

* Execute the main script to start the traffic light system.


## 👥 Credits

This project was developed by Team JARVIS as part of the IBM AI-ML Project.

* **Shamla Lokesh**

* **Jonada Tejas**

* **Dawlagar Siddharth**

* **Harsh Soni**
