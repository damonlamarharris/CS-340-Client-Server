# CS-340-Client-Server
Coursework for a Client-Server Programming class using Python and MongoDB. Includes CRUD operations, data modeling, Dash dashboards, and Plotly charts for building interactive web applications.
Module 8 Journal
Damon Harris
04/26/2025


GitHub: https://github.com/damonlamarharris/CS-340-Client-Server.git

How do you write programs that are maintainable, readable, and adaptable?
Especially consider your work on the CRUD Python module from Project One, which you used to connect the dashboard widgets to the database in Project Two. What were the advantages of working in this way? How else could you use this CRUD Python module in the future?
To write maintainable, readable, and adaptable programs, I focus on organizing code into small, well-defined functions, using consistent naming conventions, writing clear comments and documentation, and designing the program to be modular. In Project One, the CRUD Python module I developed was a great example of this approach because it separated the database operations (Create, Read, Update, Delete) from the rest of the application logic.
The advantages of working in this way were:
•	Reusability: I was able to reuse the CRUD module directly in Project Two without rewriting any database code.
•	Flexibility: If the database connection settings or structure changed, I would only need to update the CRUD module, not the entire dashboard code.
•	Readability: Other developers (or my future self) can quickly understand what each part of the CRUD module does because it is organized into clearly named methods.
•	Maintainability: Isolating database logic made it much easier to test and debug any database connection issues separately from the dashboard functionality.
In the future, I could reuse this CRUD Python module in other applications that need to interact with MongoDB. For example, if I built a mobile app, a REST API, or a more advanced web dashboard, I could easily connect the app to MongoDB by importing and using this module with only minor changes.

How do you approach a problem as a computer scientist?
Consider how you approached the database or dashboard requirements that Grazioso Salvare requested. How did your approach to this project differ from previous assignments in other courses? What techniques or strategies would you use in the future to create databases to meet other client requests?
As a computer scientist, I approach a problem by first thoroughly understanding the client's requirements, then breaking the problem into smaller, manageable tasks. For Grazioso Salvare’s project, I carefully reviewed the dashboard and database requirements, identified what data needed to be imported, how it should be accessed, and what user interactions were necessary. Then, I planned the project step-by-step: setting up CRUD operations first, followed by building the dashboard and filter options on top of it.
This project differed from previous assignments because it required connecting multiple systems (MongoDB database, Python scripts, Dash web application) into a single, integrated solution. In other courses, assignments usually focused on just one skill at a time, but this project required thinking about architecture, user experience, and data management together.
In the future, to create databases for client needs, I will continue to use strategies such as early planning, prototyping a small working version, writing modular, reusable code, and getting regular feedback from the client to ensure the solution meets their real-world needs. Maintaining good documentation and designing flexible code for future updates would also be key strategies I would follow.

What do computer scientists do, and why does it matter?
How would your work on this type of project help a company like Grazioso Salvare to do their work better?
Computer scientists solve problems by designing, building, and improving software systems, algorithms, and data management tools. Their work matters because it enables businesses and organizations to operate more efficiently, analyze information faster, and make better data-based decisions.
In this project for Grazioso Salvare, my work helps the company by providing a user-friendly dashboard that makes it easier to access and visualize important animal data. Instead of manually searching through records, Grazioso Salvare staff can now quickly filter, locate, and analyze dogs that meet their search-and-rescue criteria. This allows them to train and deploy dogs faster, ultimately saving more lives during emergencies. The dashboard improves both accuracy and speed, helping Grazioso Salvare fulfill their mission more effectively.


