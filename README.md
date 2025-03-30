# My learning project
Dockerized Nginx + Flask Backend with PostgreSQL

---

## **🛠 Technologies Used**  

This project uses the following technologies:

| Tech          | Description |
|---------------|------------|
| **Docker**    | Containerization platform to package the app |
| **Docker Compose**| Tool to manage multi-container applications |
| **Python**   | Programming language for backend logic |
| **Flask**    | Lightweight web framework for API development |
| **PostgreSQL**| Relational database used to store user information |
| **Nginx**   | Web server to serve static frontend files |

---

## **Setup**  

### **Prerequisites**  
Install docker and docker-compose
```
sudo pacman -S docker docker-compose
```

### **Clone the Repository**
```bash
git clone https://github.com/your-repo/docker-nginx-flask
cd docker-nginx-flask
```

### **Build and Run the Containers**  
```bash
docker-compose up --build
```
---

## **Accessing the Application**

🔹 Open start page in your browser:
```bash
http://localhost/
```
🔹 API available at:  
```bash
http://localhost:5000/api/login
```

---

## **🔗 API Endpoints (Flask Backend)**  

| Endpoint         | Method | Description |
|-----------------|--------|-------------|
| `/api/login`    | POST   | Register/login a user |

📌 **Example Request:**  
```json
{
  "username": "testuser",
  "password": "securepass"
}
```
📌 **Response:**  
```json
{
  "message": "User registered successfully"
}
```

---
