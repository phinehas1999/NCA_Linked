# 📚 Django E-Learning Platform

An open-source e-learning web application built with **Django** and **HTML**, designed to help learners explore courses, join events, and communicate through chats.
This project aims to provide a lightweight, customizable starting point for anyone building an online education platform.

---

## 🚀 Features

* 🧩 **User Authentication** – Sign up, log in, and log out using Django’s built-in auth system.
* 🎥 **Course Management**

  * Create, edit, delete, and view courses.
  * Join or leave courses as a participant.
  * Post comments/messages on each course.
* 🎉 **Event Management**

  * Post and manage educational events.
  * Edit and delete events.
* 💬 **Community Chat (Ask Section)**

  * Global discussion board for all users.
  * Users can create and delete their own messages.
* 🔍 **Search Functionality**

  * Search courses or categories by name.
* 🧭 **Dynamic Navbar**

  * Categories are automatically loaded for navigation across all pages.
* 🛡️ **Access Control**

  * Certain actions (creating courses/events, posting messages) require authentication.

---

## 🏗️ Tech Stack

| Component      | Technology                   |
| -------------- | ---------------------------- |
| Backend        | Django (Python)              |
| Frontend       | HTML, CSS (Django templates) |
| Database       | SQLite (default)             |
| Authentication | Django’s built-in User model |
| ORM            | Django ORM                   |

---

## ⚙️ Installation & Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/phinehas1999/NCA_Linked.git
   ```

2. **Create a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # on macOS/Linux
   venv\Scripts\activate     # on Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**

   ```bash
   python manage.py migrate
   ```

5. **Run the development server**

   ```bash
   python manage.py runserver
   ```

6. **Visit the site**

   ```
   http://127.0.0.1:8000/
   ```

---

## 🧑‍💻 Contributing

Contributions are welcome!
If you’d like to help improve this project:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m "Add feature X"`).
4. Push to your fork and create a pull request.

---

## 🧭 Routes Overview

| URL Path       | View            | Description                     |
| -------------- | --------------- | ------------------------------- |
| `/`            | `homepage`      | Main course listing and search  |
| `/course/<id>` | `videopage`     | View a specific course and chat |
| `/join`        | `joinedcourses` | View user’s joined courses      |
| `/events`      | `events`        | List of events                  |
| `/postcourse`  | `postcourse`    | Create new course               |
| `/postevent`   | `postevent`     | Create new event                |
| `/login`       | `loginpage`     | Log in existing user            |
| `/signup`      | `signuppage`    | Register new user               |
| `/logout`      | `logoutpage`    | Log out user                    |
| `/ask`         | `Ask`           | Community chat board            |

---

## 📜 License

This project is open source and available under the [MIT License](LICENSE).

---

## 💡 Future Improvements (ideas)

* Introduce course progress tracking.
* Add REST API with Django REST Framework.
* Improve frontend with React or TailwindCSS.
* Add admin dashboard for managing content.

---

## ✨ Author

Developed by **Phinehas Abdu**
If you like this project, consider starring ⭐ the repo!
