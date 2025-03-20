# BD-A1 Project

## 📌 Project Overview
This project is a **Big Data Analysis Pipeline** using **Docker**. It processes a dataset (`Games.csv`) by:
- **Loading the data** (`load.py`)
- **Preprocessing** (`dpre.py`)
- **Exploratory Data Analysis (EDA)** (`eda.py`)
- **Visualization** (`vis.py`)
- **K-Means Clustering** (`model.py`)

## 🚀 How to Run the Project
1. **Build the Docker Image**  
   ```bash
   docker build -t bd-a1-image .
