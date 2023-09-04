## PERPETUAL ERP - DJANGO

- The system is easy to use and understand. It has a simple interface that allows you to perform all operations without any difficulties, which makes it easier for users to access their data.

- This software will help your company implement resource planning by integrating all the processes needed to run your companies with a single system.

# Benefits of the software

- Improves Accuracy and Productivity
  Integrating and automating business processes eliminates redundancies and improves accuracy and productivity. In addition, departments with interconnected processes can synchronize work to achieve faster and better outcomes.

- Improves Reporting
  Your businesses will benefit from enhanced real-time data reporting from a single source system. Accurate and complete reporting will help you adequately plan, budget, forecast, and communicate the state of operations to the organization and interested parties, such as shareholders.

- Increases Efficiency
  Quick access to needed information for clients, vendors, and business partners. This contributes to improved customer and employee satisfaction, quicker response rates, and increased accuracy rates. In addition, associated costs often decrease as the company operates more efficiently.

- Increases Collaboration
  Departments are better able to collaborate and share knowledge; a newly synergized workforce can improve productivity and employee satisfaction as employees are better able to see how each functional group contributes to the mission and vision of your company. Also, menial and manual tasks are eliminated, allowing employees to allocate their time to more meaningful work.

## PERPETUAL ERP MODULES

# 1) Finance & Accounting - One of the most critical functions for businesses

This module handles all aspects of a business’s accounting and financial operations. Expense management, general ledger, accounts payable, and receivable, balance sheets, budgeting, bank statements, profile and loss reporting, and tax management are some of the primary functions managed by the finance module. Real-time financial tracking enhances forecasting and agility, providing companies with a competitive advantage.

# 2) Inventory Management / POS

It provides various features such as stock utilization reports, real-time receipts, master units, inventory audits, JIT (Just-in-time) inventory, multi-location functionality, item analysis & forecasting, and so on.

# 3) Supply Chain Management

Supply chain management modules are largely used by manufacturers, logistics companies, and suppliers & distributors to schedule, regulate, and implement the necessary production or distribution of final products in order to maximize cost savings throughout the process (starting from the vendor to the customer).

# 4) Sales Management

The sales module is responsible for analysing sales inquiries, creating quotations and sales invoices, tracking and accepting sales orders, and handling the dispatch of materials and services.

# 5) Purchase Management

The purchase management module includes features such as vendor listing, supplier and product linking, sending and receiving of quotes, planning and tracking out purchase orders, and generating GRNs (Good Receipt Notes).

# 6) Customer Relationship Management

Review of business partners and contacts.
Business cases and opportunities.
Projects (project functionality)
Marketing.
Communications history.
Scheduling and planning.
Documentation.
Analysis and evaluation – Reports.

# 7) Human Resource Management

It assists in employee on boarding processes and the management of employee data, as well as record keeping of employee data such as performance evaluations, certifications, job roles, skill matrices, and timesheet tracking. It may also include a payroll management system that helps with salary management, payroll reporting, and other tasks.

# 8) Analytics & Reporting

The analytics & reporting module in ERP provides real-time access to data and allows businesses to analyze data such as financial data, sales data, customer data, supplier data, etc at the primary or dashboard levels to get visibility to business processes and enable decision-making. Most ERPs allow the creation of custom reports.

==========================================================================

## 1. Setup Cloned Project

```
When you’re ready to start your new Django web application, create a new folder and navigate into it. In this folder, you’ll set up a new virtual environment using your command line:
```

# a) Setup / Prepare Virtual Environment

```bash
$ python -m venv .venv
```

# b) Activate the virtual environment

```
$ source .venv/Scripts/activate
```

# c) Install Django and Pin Your Dependencies

```
(.venv)$ python -m pip install django
(.venv)$ python -m pip freeze > requirements.txt
```

```
pip install ruff
ruff check --fix . to check for issues and forced fix
pip install python-dotenv
pip install django-bootstrap-v5
pip install pandas --powerful Python data analysis toolkit
pip install openpyxl
pip install Jinja2
```

# d) Set Up a Django Project

```A Django project is a high-level unit of organization that contains logic that governs your whole web application.
Each project can contain multiple apps.
```

(.venv)$ django-admin startproject <project-name>

`OR If you want to avoid creating the additional top-level project folder add a . at the end`

(.venv) $ django-admin startproject <projectname> .

# e) Start a Django App

```
A Django app is a lower-level unit of your web application. You can have zero to many apps in a project,
and you’ll usually have at least one app. You’ll learn more about apps in the next section.
```

(env) $ python manage.py startapp <appname>

# f) Run Project

_Note: For running the first time, create database tables_

```bash
(.venv)$ python manage.py makemigrations
(.venv)$ python manage.py migrate
```

Then

```bash
(.venv)$ python manage.py runserver
```

Goto `http://127.0.0.1:8000/`

## Contributors

- [Edwin Niwaha](https://github.com/edwin-niwaha)
