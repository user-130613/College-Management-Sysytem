This Django project features a comprehensive user management system with distinct roles and permissions, including Admin, Head of Department (HOD), Staff, and Students:

Admin:

Role: Superuser with the highest level of control.
Responsibilities: Manages the entire system.
Permissions: Can create, update, and delete HODs, Staff, and Students. Oversees the overall management and configuration of the application.
Head of Department (HOD):

Role: Departmental leader with administrative privileges.
Responsibilities: Manages departmental operations.
Permissions: Can add and manage Staff and Students within their department. Cannot access system-wide administrative functions reserved for the Admin.
Staff:

Role: Educational and administrative support personnel.
Responsibilities: Handles day-to-day tasks such as recording attendance and updating student marks.
Permissions: Can perform attendance tracking, grade management, and other related tasks. Lacks access to higher-level administrative functions.
Students:

Role: Primary users of the system for their academic and administrative needs.
Responsibilities: Engage with the system for their academic requirements.
Permissions: Limited to personal information access and feedback. Cannot perform administrative tasks.
General Access:

Feedback Forms and Leave Letters: Accessible to all users, including Admin, HODs, Staff, and Students. Admin, however, does not handle these forms, maintaining their role solely in system management.
This structure ensures a clear segregation of responsibilities and permissions, facilitating efficient management and operation of the system.
