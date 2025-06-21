# 🛠️ IT Ticketing System - Django Project

A robust and scalable **IT Ticketing System** built with Django, designed to streamline IT support operations within an organization. This application enables efficient **ticket raising**, **task assignment**, **admin management**, **RBAC (Role-Based Access Control)**, and **task lifecycle tracking**, ensuring seamless collaboration between end-users, support staff, and administrators.

---

## 🚀 Features

### 🎫 Ticket Management
- Users can raise IT tickets for various issues.
- Tickets can include attachments, priority levels, and detailed descriptions.
- Automatic status tracking: Open → In Progress → Resolved → Closed.

### 📋 Task Management
- Admins or support staff can break tickets into smaller tasks.
- Assign, update, or mark tasks as completed.
- View task progress with timelines and statuses.

### 👥 Role-Based Access Control (RBAC)
- Roles: Admin, Support Staff, Employee (or End-User).
- Each role has defined permissions (view, edit, assign, close, etc.).
- Secure, modular access ensures data integrity and privacy.

### ⚙️ Admin Management
- Admin dashboard for ticket oversight, user management, and analytics.
- Create and manage roles and permissions dynamically.
- Monitor ticket queues, performance metrics, and SLA compliance.

### ✅ Task Assignment & Notifications
- Assign tasks to team members with deadlines and priority.
- Automatic email or in-app notifications for updates and escalations.
- Commenting and activity log for each ticket/task.

---

## 🛠️ Tech Stack

- **Backend**: Django (Python)
- **Frontend**: HTML5, CSS3, Bootstrap, Django Templates
- **Database**: PostgreSQL / SQLite (based on environment)
- **Authentication**: Django’s built-in Auth + custom RBAC middleware
- **Deployment**: Gunicorn + Nginx (Production Ready)
- **Extras**: Django REST Framework (optional for API access), Celery (for async tasks), Redis (for queue management)

---

## 📦 Installation & Setup

### Prerequisites
- Python 3.8+
- pip / virtualenv
- PostgreSQL (or SQLite for testing)

### Steps

```bash
# Clone the repository
git clone https://github.com/your-username/it-ticketing-system.git
cd it-ticketing-system

# Create virtual environment
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Setup DB
python manage.py makemigrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run the server
python manage.py runserver
