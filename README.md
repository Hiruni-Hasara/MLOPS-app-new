# MLOPS-app-new: Heart Disease Prediction Web App

This project is a machine learning web application that predicts whether a person is at risk of heart disease based on their health data.

---

## Group members:
- **W.K.Hiruni Hasara (s 16210)**
- **Nethmi Sansala (s 16252)**
- **Chathuni Amasha (s 16242)**

---

## Built With

- **Python & Flask** (for backend)
- **HTML, CSS, JavaScript** (for frontend UI)
- **scikit-learn** (for machine learning)
- **Docker** (for packaging and deployment)

---

## How to Run This App (Using Docker)

You don’t need to install Python or any packages.  
Just follow these steps:

### 1. Install Docker Desktop (if not already installed)

[https://www.docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop)  
Then install and open Docker.

---

### 2. Build and Run the Docker Image

Open your terminal or PowerShell inside the project folder, then run:

---

```bash
docker build -t heart-app .
docker run -p 5000:5000 heart-app
```
Now open your browser and go to:

```bash
http://localhost:5000
```
You’ll see the prediction form...

