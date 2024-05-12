# Django tutorial project
This project is part of Django tutorial, which is led by Dennis Ivy: https://github.com/divanov11

12.05.2024 - GET for projects
- implemented GET method for projects and a single project using Django Rest Framework
- added relations for models in API
- added JWS authentication for API

07.05.2024 - API
- Starting API

07.05.2024 - Email
- Sending welcome email after registration
- Possibility of restoring forgotten password

06.05.2024 - Comment and reviews section
- Users can comment projects
- Ordering projects by their vote ratio
- Added conditions for comment section
- Sending messages for users

03.05.2024 - Searching
- added possibility to search projects and developers by name, skills, description and tags
- Added pagination for projects and profiles
- Added JS for connecting pagination and searching

30.04.2024 - Skills
- Added possibility to add, edit or delete skills

29.04.2024 - Login, Logout and register
- Added login and registration panels
- Users can be logged in and registered
- Messages prompts with info about login
- Restrictions for projects creation - just for logged users
- Added user profile page
- Added profile changes for logged users

22.04.2024 - Sharing project on GitHub
- Added new app: Users
- Created models for users
- connected Profiles database with Projects
- added profiles websites
- added signals to Profiles (on_save and on_delete)