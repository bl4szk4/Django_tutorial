# Django tutorial project
This project is part of Django tutorial, which is led by Dennis Ivy: https://github.com/divanov11

06.05.2024 - Comment and reviews section
- Users can comment projects

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