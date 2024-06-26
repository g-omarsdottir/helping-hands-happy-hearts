# Helping Hands, Happy Hearts

This project is a digital "pay it forward board" connecting those who need help with those eager to lend a hand in their neighborhood. 

We believe everyone wins when small acts of kindness become part of our daily routines. This platform offers a convenient channel to connect with neighbors within our fast-paced modern society.

![Mockup](/documentation/mockup.png)

You can view the live project here [Helping Hands, Happy Hearts](https://helping-hands-happy-hearts-546cab7eb98a.herokuapp.com/)<br>
*(To open in a new window, press "ctrl" (or ⌘ for Mac) + click on the link)*

## Table of contents

- [Introduction](#introduction)
- [Project Goals](#project-goal)
- [User Experience](#user-experience)
    - [Target Group](#target-group)
    - [Visitors Goals](#visitors-goals)
- [Design](#design)
    - [Layout](#layout)
    - [Wireframes](#wireframes)
    - [Colors](#colors)
- [Project planning](#project-planning)
    - [Database Schema](#database-schema)
    - [Agile Development Methods (Epics, User Stories, MoSCoW Prioritization, Kanban board)](#agile-development-methods)
- [Features](#features)
    - [Main Features](#main-features)
    - [Responsiveness](#responsiveness)
    - [Security](#security)
    - [Future Features](#future-features)
- [Deployment and Local Development](#deployment-and-local-development)
    - [Database](#neon-database)
    - [Deployment](#deployement-using-heroku)
    - [Local Clone](#local-clone)
    - [Fork](#fork)
- [Credits](#credits)
    - [Content](#content)
    - [Imagery](#imagery)
    - [Acknowledgements](#acknowledgements)

Testing and Bugs are documented in the separate file [TESTING.md](TESTING.md)

## Introduction

The delightful tingling feeling one gets while doing a good deed, often comes too short in our modern fast-moving and hectic life. It can be difficult to devote a large amount of time for volunteer work and such organizations depend on long-term volunteers, since otherwise the manpower for coordinating grows just as much as the number of volunteers. This website offers people an opportunity to channel their eagerness to help and dive right in and help others without any long-term commitment and at their own personal time schedule. 

On the flip side, it offers people who don’t know who or even how to ask for help a platform to express their need for help, without the social conflict of putting someone in the spot by asking directly. 
The good deeds can vary from elderly folks setting up their new smartphone or have issues connecting to the internet. It’s hardly possible to even pay bills these days without filling out an online form. Young people grow up using modern technology and have the opportunity to shine without much effort. Or maybe someone twisted their ankle and needs someone to walk the dog. Of course, there are paid services for such tasks, but the offers and availability can be scarce and involve planning ahead, which is not always possible. Maybe someone loves gardening but doesn’t have garden and can thus combine a great day outdoors with helping a neighbor in need.  

The project can be a great platform to include in the local schools to nourish the happiness of helping others from early on. After all, it takes a village to raise a child. If time schedule to finish the learning material for the semester doesn’t allow for extracurricular activities, the teacher can easily adjust the plan without much ado.

Social Media influencers have a bounty of opportunities to create content and boost their number of followers and likes on their posts without much effort. They can pick and choose according to what image they are seeking to convey on their own platform. There’s no denying that helping for the sake of helping is more noble, but we all know that there is no such thing a selfless good deed, even if the win is only to feel good, so why not make the most of it. It’s a win-win for everyone involved.

## Project Goal

-	**Combining Convenience with Compassion:** To make it easy to offer or request help without long-term commitments or awkward direct requests.
-	**Bridging Gaps:** Lack of technology skills or a social network, physical limitations, or simple lack of time may create barriers. Our platform fosters connections to overcome these.
-	**Community Spirit:** From dog walking to gardening, or tech help to tutoring, the platform empowers neighbors to support each other in diverse ways.
-	**Potential Impact:** Schools can encourage positive action, and social media influencers can inspire and boost their number of followers and likes on their posts while also making a positive impact.

## User Experience

### Target Group

-	People seeking to offer or receive help within their local community. 
-	People with diverse skills they would like to foster and put to good use.
-	People who need urgent help in unexpected situations, that are time sensitive and cannot wait until a paid service can be scheduled, 
-	People who need short term help, ranging from tech assistance and dog walking to gardening and simple errands, due to illness or weather conditions.
-	People who believe in the power of neighborly connections and want to contribute to a platform of small, impactful acts of kindness.
-	Educators who want to connect classroom learning with real-world problem-solving while building empathy and confidence in their pupils by helping them discover their skills through service, which benefits both the community and personal development.
-	Parents who want to foster kindness and community engagement in their children, while spending quality time together.

### Visitors Goals

### First Time Visitors Goals

As a first time user I can
- Browse a wide range of help requests and offered services.
- Discover the variety of ways they can contribute or find assistance.
- Understand the scope of the platform and its potential benefits.


### Returning Visitors Goals

As a returning visitor, I want to
- Regularly check for relevant offers that address my current needs.
- Easily find new opportunities to offer help that match my skills.
- Feel comfortable reaching out and requesting assistance.


### Frequent Visitors Goals

As a frequent visitor, I want to
- Search for new offers and requests.
- Feel connected to a kind and caring community.

## Design

### Layout

The layout of the website is devided into an area accessible to all and area exclusively for logged-in users. 

For better user experience and uncertainty avoidance about what the project is about, hesitance to sign up, and to able older people with little computer skills to be able to take advantage of what the platform has to offer, the website's content is visible to all. This area contains the Hompage, the Offers & Requests page (Offers and Requests), the Sign-In page, and the Sign-Up page.

To contribute content and engage in conversations, the users must be logged in.

<details>
<summary>Click for Layout Flowchart</summary>

![layout](/documentation/layout.png)
</details>

### Wireframes

#### Wireframes Mobile Version

![wireframes-mobile](/documentation/wireframes-mobile.png)

<details>
<summary>Click for wireframe Logged-In View - "Add Post"</summary>

![mobile-loggedin](/documentation/mobile-loggedin.png)
</details>


#### Wireframes Desktop Version

<details>
<summary>Click for wireframe "Home"</summary>

![home](/documentation/home.png)
</details>

<details>
<summary>Click for wireframe "Offers & Reqests"</summary>

![offers-requests](/documentation/offers-requests.png)
</details>

<details>
<summary>Click for wireframe "Sign-Up"</summary>

![sign-up](/documentation/sign-up.png)
</details>

<details>
<summary>Click for wireframe "Sign-In"</summary>

![sign-in](/documentation/sign-in.png)
</details>


<details>
<summary>Click for wireframe Logged-In View - "Add Post"</summary>

![desktop-loggedin](/documentation/desktop-loggedin.png)
</details>

### Colors

The colors used are from this color palette suggested by [coolers](https://coolors.co/palettes/trending):

![color palette](/documentation/colors.png)

For a sleek layout and escpecailly not knowing what kind of images users would upload, the use of colors was kept minimal to avoid visual clutter. Color accents were used to create depth with box-shadows and for pseudo-class hover effect. The footer is in vibrant coral color since it is conteptually seperated from the rest of the website and thus does not irritate or take the focus off the rest of the content.

The font color is a warm tone of black and background color is offwhite, which make a very good match for accessability, readability and contrast while being easy on the eye. [Coolors Color Contrast Checker](https://coolors.co/contrast-checker/333333-f5f5f5) score:

![contrast](/documentation/contrast.png)

## Project planning

### Database Schema

This project utilizes a relational database powered by [Neon.tech](https://neon.tech/), a serverless PostgreSQL solution.

The Entity Relationship Diagram (ERD, see below) was created using before starting the development process. Reduced complexity of the database entities and detailed planning streamlines the development process and minimizes the need for debugging.

Each Django model is represented with a table on the ERD along with its attributes and model fields.

**Database Overview:**
- **Key Features:** Stores user posts.
- **User Management:** The models utilize the Django Allauth User model.
- **Content Management:** Users can create and update own content, interact with other users by liking content.
- **Technical Design:** Separation of concern was implemented by deviding key components into individual Django Models *(see ERD)*. This allows for simple and reliable queries based on the primary key, as well as easy management and scalability.
- **Relationships** between the model fields are indicated with relationship lines on the ERD.
- **Security Practises:** Security best practices were obtained using CSRF Tokens for data protection and authentication using Django Allauth.

<details>
<summary> Click for Entity Relationship Diagram (ERD)</summary>

![Entity Relationship Diagram](/documentation/erd.png)
</details>

### Agile Development Methods 

#### Epics

- Epics are the main goals and features of the project that can be broken down into smaller tasks called user stories. Each epic can have multiple user stories. The epics can be viewed on this project's Kanban board (see below).

#### User Stories

- User stories describe the features from an epic in more and from the user's perspective. They start with "As a [role] I can [capability] so that [received benefit]". Each user story has a clear goal, which is explained in detail in the acceptance criteria. The acceptance criteria describe the requirements to fulfill the feature of the user story. The user stories can be viewed on this project's Kanban board (see below).

#### MoSCoW Prioritization

- A handy method to categorize features based on urgency and necessity. The acronym stands for Must Have, Should Have, Could Have, and Won't Have. This method helps decide which features are absolutely necessary for the current iteration, which ones could be added if time permits, and which ones might be postponed indefinitely. The MoSCoW prioritazion was defined using labels on each user story (see Kanban board, below).

#### Kanban board

- A visual tool in agile project management. It visually represents the workflow stages and the status of individual user stories. The Kanban board for this project can be viewed [here](https://github.com/users/g-omarsdottir/projects/4).

## Technology Used

### Languages Used

- Python
- HTML
- CSS
- JavaScript

### Libraries and Frameworks Used

In addition to libraries and frameworks already installed in the Code Institute template:
- [Django v4.2.13](https://docs.djangoproject.com/en/5.0/releases/4.2.13/) - Python web framework
- [Django allauth](https://docs.allauth.org/en/latest/installation/index.html) - User account authentication and verification *(check: verif.)*
- [Django Crispy Forms v2.1](https://django-crispy-forms.readthedocs.io/en/latest/install.html#installing-django-crispy-forms) - Simplifies the creation of forms
- [Django ckeditor v6.7.1](https://pypi.org/project/django-ckeditor/) - Privides a handy richt text field widget for forms
- [Django RichTextField v1.6.2](https://djangopackages.org/packages/p/django-richtextfield/) - Renders a customizable rich text editor for user posts
- [Django Resized v1.0.2](https://pypi.org/project/django-resized/) - Handles resizing and format converting of images uploaded by users
- [Pillow v10.3.0](https://pillow.readthedocs.io/en/stable/) - A Python imaging library, handles images in combination with the Django Resized Image Field
- [Bootstrap v5.2.3](https://getbootstrap.com/docs/5.2/getting-started/download/) - Open-source CSS framework
- [Crispy-Bootstrap v5 2024.2](https://pypi.org/project/crispy-bootstrap5/) - Provides Bootstrap-specific classes and styles to render forms
- [Summernote v0.8.20.0](https://djangopackages.org/packages/p/django-summernote/) - Renders a customizable rich text editor for the admin panel
- [Autoslug](https://django-autoslug.readthedocs.io/_/downloads/en/stable/pdf/) - Automatically generates slug field for improved UX for less experienced users
- [cloudinary v1.36.0](https://cloudinary.com/documentation/django_integration) - Allows users to upload images
- [dj3-cloudinary-storage v0.0.6](https://cloudinary.com/documentation/rails_activestorage) - Provides storage of images uploaded by users
- [Black v24.4.2](https://black.readthedocs.io/en/stable/) - Formats code compliant to pep8
- [whitenoise v5.3.0](https://pypi.org/project/whitenoise/) - Python package to simplify static file serving for web apps
- [psycopg2 v2.9.9](https://pypi.org/project/psycopg2/) - PostgreSQL database adapter for the Python programming language
- [gunicorn v20.1.0](https://docs.gunicorn.org/en/20.1.0/) - Gunicorn serves as a Python WSGI HTTP server for UNIX, designed to interface with WSGI-compliant web applications to serve applications efficiently and reliably, handling multiple concurrent connections and requests optimisation (equivalent to manage.py runserver used in development but for deployed app)
- [dj-database-url v0.5.0](https://pypi.org/project/dj-database-url/0.5.0/) - Django utility allows to utilize the 12factor inspired DATABASE_URL environment variable to configure the Django application

### Programs Used

- [diagrams.net](https://app.diagrams.net/) to create the layout flowchart and the database ERD
- [balsamiq](https://balsamiq.com/?gad_source=1&gclid=CjwKCAjw9cCyBhBzEiwAJTUWNUqgDLXtJBfd_25tyqofGEHLEm5fRfDXTwm6E25bZFvYSqIkYfaZnRoCLFUQAvD_BwE) to create the wireframes
- [Pixelied](https://pixelied.com/convert/jpg-converter/jpg-to-webp) to convert images into webp format
- [Optimizilla](https://imagecompressor.com/) to compress image file size
- [Coolor Color Contract Checker](https://coolors.co/contrast-checker/333333-f5f5f5) to assess contrast for accessibility
- [Techsini.com](https://techsini.com/multi-mockup/index.php) to create the mockup for this README
- [Chrome Extension Ignor X-Frame headers](https://chromewebstore.google.com/detail/ignore-x-frame-headers/gleekbfjekiniecknbkamfmkohkpodhe) to be able to create a mockup on Techsini from a django project
- [Canva](https://www.canva.com/) to create the website logo

## Features

### Main Features

### Clean and User-Friendly Interface

- The website uses a clean layout with a clear visual hierarchy for easy navigation.
- A limited color palette is used to avoid visual clutter.
- Navigation elements (links and buttons) are prominently placed and clearly labeled.
- The user’s current location on the website is always indicated.
- Users are given full control with buttons to return to overview, add post by clicking a button without scrolling to navigation bar directly under the overview of posts. 
- If a user wants to delete a post, the user has the option to cancel the deletion and return to the post without deleting.

![navbar](/documentation/navbar.png)

![return](/documentation/feature-return.png)

### Informative Homepage

- A clear and concise welcome message greets visitors. 
- A brief description explains the website's concept of community support.
- Contact details, including when to contact the site owner and average response time, are clearly displayed. The email link is clickable and opens in the user's default email app.
- The GitHub account of the website developer is included in the footer. In theory, the social media accounts of the project would be linked in the footer.

![feature-welcome](/documentation/feature-welcome.png)

![feature-contact](/documentation/feature-contact.png)

![feature-email](/documentation/feature-email.png)

### Sign-Up and Sign-In

- Everyone can view post listings and details, but users must be logged in to pin posts on the board.
- A prominent "Sign Up" and "Sign-In link is available in the navigation bar.
- A user-friendly form allows sign-up with email address, chosen username, and password.
- Users choose a username for displaying author names on posts.
- Clear error messages are displayed for invalid input during sign-up and login.
- The templates are from Django Allauth and have the project's base template as background.

![feature-signup](/documentation/feature-signup.png)

### Create Post

- A clearly visible "Create Post" link and button provide easy access to post creation.
- A user-friendly form allows adding relevant information like title, description, category, and location.
- Required fields are marked with an asterisk (*) for clear guidance.
- Immediate feedback with solutions is provided for missing fields.
- Users can publish posts immediately without waiting for approval, fostering a dynamic and helpful community.

![feature-create](/documentation/feature-create.png)

### Offers & Requests Page

- A list of available posts is displayed on the Offers & Requests page.
- Posts are listed chronologically, with newest posts appearing first.
- Each post displays a title, short description, and relevant details (category, location).

![feature-board](/documentation/board.png)

### Read, Update, Delete Management of Posts

- Users can click on the post on the overview and can view the post in detail.
- Users can edit and delete their own posts using clearly visible options.
- Edit and delete options are hidden for posts created by other users.

![feature-detailpost](/documentation/feature-detailpost.png)

![feature-edit-delete](/documentation/feature-edit-delete.png)

### Liking Posts

- A like button allows users to like and unlike posts (toggle functionality).
- The number of likes is displayed for each post.
- The like button is hidden for non-logged-in users, but the like count remains visible and they are encouraged to sign up or sign in to participate.

![like-unlike](/documentation/like.png)


### Clear User Feedback to CRUD functionalities

- - The user is informed of every successful creation, update or delete action with an alert message. The alert messages are elegantly provided with the Django utily SuccessMessageMixin.
- Clear error messages are displayed for unsuccessful actions.
- Clicking on a post displays the correct detailed post for easy reading.

![success-messages](/documentation/success-messages.png)

### Responsiveness

- Responsiveness on all screensizes was obtained using minimal code and no mediaqueries using Bootstrap 5 grid system. Since this project is to showcase coding abilities using Django and less emphasis is layed on frontend styling, I took advantage of being able to further practise my Bootstrap skills and achieve for maximum responsiveness with minimum amount of code.

### Security

The application prioritizes user data security and employs robust measures to safeguard against potential threats. This includes access control, and secure coding practices. 
- **CRUD functunalities:** Django’s built in authentication and validation of class-based views handles secure operation of CRUD functionalities elegantly and additional mixins prevent manipulation of content by other users in a concise and robust coding practise. Django's class-based views to view, delete and edit in combination Dango's authentication system's mixins LoginRequiredMixin and UserPassesTestMixin handle elegantly user actions and prevent if not authenticated not logged in by redirecting the user to the login page. 
- **Authentication and Authorization:** Signup and Login handles elegantly by Django Allauth.
- **Data Validation and Sanitization:** Form validation ensures data integrity and prevents unauthorized manipulation.
- **Error Handling:** customized error page guide users and provide informative messages in case of issues.
- **Environment Security:** Secure handling of sensitive data is prioritized throughout the development and deployment phases. This involves storing critical information such as database URLs, secret keys, and Cloudinary URLs securely. During development, these details are stored in a private .env.py file, excluded from version control via .gitignore. In production, they are managed as configurable variables, enhancing security by disabling debug mode.
- **CSRF Protection:** The application employs CSRF protection measures to safeguard against unauthorized activities. CSRF tokens are seamlessly integrated into every form submission, bolstering the security posture.
- **Handling RichTextFields:** While adhering to standard security protocols, I encountered a nuanced challenge with RichTextFields in forms intended for posting content. Without explicitly marking the form field as safe, the user's desired styling cannot be applied. Addressing this issue elegantly remains a learning curve for me as a novice web developer.

### Future Features

- Comment feature to comment on posts.
- Button to turn on amplified text for low vision people. Older people don't necessecarily know how to utilize assistive technology, so including a button for extra large text would be helpful.

    <details>
    <summary> Click for image</summary>

    ![Low Vision Button](/documentation/future-feature.png)
    </details>

- User profiles for including a profile picture for improved user experience. The model field for saving post as a draft or publish directly can easily be implemented at a later time, since it is present in the database and set to default=publish, and is not displayed to users so it doesn't cause confusion at the time being.
- Bookmarks to save interesting user posts.
- Website internal messaging between users, so they don't have to include their contact details on the website.
- Add more visual user feedback using JavaScript to customize the layout further and improve user experience.
- Search function.
- Implement and utilize all Django Allauths functions, like password retrieval.

## Deployment and Local Development

### Neon Database

This project utilizes a relational database powered by [Neon.tech](https://neon.tech/), a serverless PostgreSQL solution.

- Log into or sign up for a Neon account.
- Create or navigate to your "Tier" (one free tier per user).
- Navigate to the "Dashboard" on the left side menu.
- In the section "Connection Details", you will find the link to the database displayed in the subsection "Connection String".

### Deployement using Heroku

To deploy the repository:
- Log into Heroku and navigate to the dashboard.
- Navigate to the button "New" in the top right corner and select "Create New App" from the navigation dropdown menu.
- Enter a name for the app. The name of the app must be unique and cannot be identical to any other app deployed by other users on Heroku.
- Select your region, "United States" or "Europe", from the navigation dropdown menu.
- Click on the button "Create App".
- Navigate to "Deploy" on the top navigation menu, scroll down to "Deploy Method" and connect the repository with GitHub.
- Navigate to "Settings" on the top navigation menu.
- In the section "Config Var", click on the button "Reveal Config Vars".
- Click on "Add a new Config Var" and add the necessary keys and values.
    - SECRET_KEY with the value of the secret key
    - DATABASE_URL with the value of the database url
    - CLOUDINARY_URL with the value of the cloudinary url
- Navigate to section "Deploy" on the top navigation menu.
- Select "GitHub" as the deployment method.
- Search for the repository to be deployed by using the search bar and click "Connect".
- Select the repository branch to be deployed.
- Choose "Manual" deployment.
    - Manual deployment must be manually re-deployed after pushing new changes to the repository.
    - Crucial when working with DEBUG=True during development.
- Click the button "View" to open the link to the deployed project.

### Local Development

#### Local Clone

To clone the repository:
- Log in to GitHub and navigate to the repository of this project.
- Click on the green button "Code" to open the dropdown menu, select "Clone with HTTPS, SSH or GitHub CLI" and copy the link provided.
- Open "Terminal" (or "Git Bash") in your code editor.
- Change the current working directory to the location where you want the cloned directory to be made.
- Type "git clone" in the terminal and then paste the URL copied on GitHub in step 2, above.
- Press "Enter" and your local clone will be created.
- Install requirements from requirements.txt using the command "pip install -r requirements.txt". If working in a virtual environment, activate the virtual environment before running the command.
- Create a env.py to store database url, secret key and cloudinary url.

#### Fork

To fork the repository:
- Log in to Github and navigate to the repository of this project.
- Click the button "Fork" in the top right corner to open dropdown menu and select "Create a new fork".

## Credits

- The content for this project was written by me, Gudrun Omarsdottir.

### Content

- Special thanks to Dee-McG for her extremely helpful [video tutorial](https://www.youtube.com/watch?v=sBjbty691eI&list=PLXuTq6OsqZjbCSfiLNb2f1FOs8viArjWy) on building a recipe django blog for recipes and [documentation](https://github.com/Dee-McG/Recipe-Tutorial). Her tutorial was a great inspiration and very helpful in addition to the official documentation to understand the concepts.
- Code Institute walkthrough project codestar for inspiration.
- My friend Stephan Reich, Software Developer, for invaluable advice, especially with urls (reverse_lazy) and how to use a button to toggle likes on and off.
- [Django docs get_FOO_display()](https://docs.djangoproject.com/en/5.0/ref/models/instances/) - Return "human-readable" value of model fields.
- [Stackoverflow](https://stackoverflow.com/) for various how-tos, tipps and tricks of the trade.
- Official documentation from [Bootstrap](https://getbootstrap.com/docs/5.0/getting-started/introduction/) and [Django](https://docs.djangoproject.com/en/5.0/).
- [Gemini AI](https://gemini.google.com/app) for inspiration for the user posts on the website.

### Imagery

- [Favicon by surang](https://www.flaticon.com/free-icons/charity")
- [Dani Guitarra on Unsplash](https://unsplash.com/photos/persons-hand-forming-heart-7JbUsmYPwP8) - for main website and default placeholder image
- [Daniel Watson on Unsplash](https://unsplash.com/photos/green-and-black-lawnmower-on-green-grass-8vBpYpTGo90)
- [sabinevanerp on Pixabay, 1:](https://pixabay.com/photos/woman-indoors-people-grown-up-hand-3188750/),[2:](https://pixabay.com/users/sabinevanerp-2145163/?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=3188745)
- [Bjørnar Kibsgaard on Pixabay](https://pixabay.com/users/bjokib-6383051/?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=7917641)
- [JackieLou DL on Pixabay](https://pixabay.com/photos/dog-walk-snow-shetland-sheepdog-6000001/)
- [John Schnobrich on Unsplash](https://unsplash.com/photos/person-using-laptop-FlPc9_VocJ4)
- [Andras Vas on Unsplash](https://unsplash.com/photos/macbook-pro-turned-on-Bd7gNnWJBkU)

### Acknowledgements

- My mentor, Mitko Bachvarov, for his guidance and encouragement.
- My fellow students at Code Institute, especially [Niclas Hugdahl](https://github.com/NiclO1337) and [Amir Schkolnik](https://github.com/AmirShkolnik), for guidance, inspiration, testing and proofreading.
- My Code Institute class facilitator, Kristyna Wach, for her cheerful motivation and encouragement.
- Slack community for support and advice.
- Stackoverflow community for information.