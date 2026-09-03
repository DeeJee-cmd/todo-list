# Todo List Application
Django application for managing tasks and tags. The project is implemented according to a modular structure, fully designed on Bootstrap 5 and 100% covered by tests.

---

Test Admin Credentials
```text
Login: "admin"
Password: "1234qwer"
```

---
# Quick Start & Setup
## Clone & Virtual Environment

Windows (PowerShell/CMD):
```bash
py -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

MacOS / Linux:
```bash
python3 -m venv venv
source venv\bin\activate
pip install -r requirements.txt
```
---
## Environment Variables

```text
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
```
---
## Database & Fixtures

```bash
python manage.py migrate
python manage.py loaddata task_data.jso
```
---
## Run Development Server
```bash
python manage.py runserver
```
---
## Tests
```bash
python manage.py test tasks
```
---
![task.png](doc%2Ftask.png)

![tag.png](doc%2Ftag.png)
---

### Future Improvements & Roadmap

* **Database Migration:** Switch from SQLite to PostgreSQL for production environments.
* **Pagination & Filtering:** Implement pagination for task/tag lists and add dynamic filtering by completion status (`is_done`), tags, and deadlines.
* **REST API:** Introduce RESTful API endpoints using Django REST Framework for SPA or mobile app integration.
* **Background Tasks (Celery + Redis):** Set up asynchronous email notifications for upcoming deadlines.
* **Dynamic UI (HTMX):** Enable task status toggling and tag deletions without full page reloads.
