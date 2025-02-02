# FAQ Project

## **Project Overview**
This project is a Django-based FAQ management system that supports multilingual translations, WYSIWYG editor integration, REST API, caching with Redis, and unit testing.

---

## **Installation Steps**

### **1. Clone the Repository**
1. Create a folder on your laptop:
   ```bash
   mkdir "FAQ Project"
   cd "FAQ Project"
   ```
2. Open Command Prompt in this directory.
3. Clone the Git repository:
   ```bash
   git clone https://github.com/Ganga522/FAQ-Project.git
   ```

### **2. Set Up Virtual Environment**
4. Create a virtual environment:
   ```bash
   virtualenv env
   ```
5. Activate the virtual environment:
   - **Windows**:
     ```bash
     env\Scripts\activate
     ```
   - **Mac/Linux**:
     ```bash
     source env/bin/activate
     ```
6. Navigate to the project folder:
   ```bash
   cd FAQ-Project
   ```

### **3. Install Dependencies**
7. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### **4. Apply Migrations**
8. Run the following command to apply migrations:
   ```bash
   python manage.py migrate
   ```

---

## **Steps to Install Redis Server**

### **1. Download & Install Redis**
9. Open a browser and visit the following link:
   ```
   https://github.com/microsoftarchive/redis/releases
   ```
10. Download **Redis-x64-3.0.504.msi** and install it.

### **2. Configure Redis**
11. Add the Redis installation path to **environmental variables**:
    - The default installation path is:
      ```
      C:\Program Files\Redis
      ```
12. Open a new **Command Prompt** and start the Redis server:
    ```bash
    redis-server.exe
    ```
13. Verify that Redis is running by opening another **Command Prompt** and running:
    ```bash
    redis-cli ping
    ```
    If you see **PONG**, Redis is running successfully.

---

## **Run the Project**

### **1. Create a Superuser**
14. Create an admin user to access the Django Admin Panel:
    ```bash
    python manage.py createsuperuser
    ```
    - Username: `admin`
    - Email: `admin`
    - Password: `admin`

### **2. Start the Server**
15. Run the Django development server:
    ```bash
    python manage.py runserver
    ```

### **3. Access the Admin Panel**
16. Open your browser and go to:
    ```
    http://127.0.0.1:8000/admin
    ```
17. Log in using the superuser credentials and navigate to the **FAQ** section.
18. Add FAQs by entering a **question** and a **formatted answer** using the WYSIWYG editor.

---

## **Using the API (Postman)**

### **1. Install Postman**
19. Download and install Postman from:
    ```
    https://www.postman.com/downloads/
    ```

### **2. Test the API Endpoints**
20. Use the following API endpoints in Postman to retrieve FAQs:

#### **Fetch FAQs (Default - English)**
```bash
GET http://127.0.0.1:8000/api/faqs/
```

#### **Fetch FAQs in Hindi**
```bash
GET http://127.0.0.1:8000/api/faqs/?lang=hi
```

#### **Fetch FAQs in Bengali**
```bash
GET http://127.0.0.1:8000/api/faqs/?lang=bn
```

---

## **Run Unit Tests**
21. Navigate to the `faq` directory and run tests using pytest:
    ```bash
    cd faq
    pytest
    ```

---

## **Project Features**
✅ FAQ Model with **Multilingual Support**
✅ **WYSIWYG Editor** Integration (django-ckeditor)
✅ **REST API** for FAQ Management
✅ **Caching** with Redis for performance
✅ **Automated Translations** using Google Translate API
✅ **Django Admin Panel** for managing FAQs
✅ **Unit Testing** with Pytest
✅ **PEP8 Compliance** and Code Linting

---

## **Contributors**
- **K. Gangadhar** ([GitHub Profile](https://github.com/Ganga522))

## **License**
This project is licensed under the MIT License.

🚀 **Happy Coding!**

