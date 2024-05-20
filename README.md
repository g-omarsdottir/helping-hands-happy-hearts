# Helping Hands, Happy Hearts

This project is a digital "pay it forward board" connecting those who need help with those eager to lend a hand in their neighborhood. 

We believe everyone wins when small acts of kindness become part of our daily routines. This platform offers a convenient channel to connect with neighbors within our fast-paced modern society.

Mockup
You can view the live project here (link to deployed website)
*(To open in a new window, press "ctrl" (or ⌘ for Mac) + click on the link)*

## Table of contents

Introduction
Project Goals
User Experience
Design
Project planning
- Wireframes
- Database Schema
- Agile Development Methods 
    - Epics
    - User Stories
    - MoSCoW Prioritization
    - Kanban board
Features
*Testing and Bugs (separate)*
Deployment and Local Development
Credits

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

### Target Group/Audience

-	People seeking to offer or receive help within their local community. 
-	People with diverse skills they would like to foster and put to good use.
-	People who need urgent help in unexpected situations, that are time sensitive and cannot wait until a paid service can be scheduled, 
-	People who need short term help, ranging from tech assistance and dog walking to gardening and simple errands, due to illness or weather conditions.
-	People who believe in the power of neighborly connections and want to contribute to a platform of small, impactful acts of kindness.
-	Educators who want to connect classroom learning with real-world problem-solving while building empathy and confidence in their pupils by helping them discover their skills through service, which benefits both the community and personal development.
-	Parents who want to foster kindness and community engagement in their children, while spending quality time together.

### First Time Visitors Goals
As a first time user I can
- ...

### Returning Visitors Goals
As a returning visitor, I want to
- ...

### Frequent Visitors Goals
As a frequent visitor, I want to
- ...

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
Mobile Version
![wireframes-mobile](/documentation/wireframes-mobile.png)

Desktop Version
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

## Project planning
### Database Schema

This project utilizes a relational database powered by [Neon.tech](https://neon.tech/), a serverless PostgreSQL solution.

The Entity Relationship Diagram (ERD, see below) was created using before starting the development process. Reduced complexity of the database entities and detailed planning streamlines the development process and minimizes the need for debugging.

Each Django model is represented with a table on the ERD along with its attributes and model fields.

**Database Overview:**
- **Key Features:** Stores user profile, user posts, and comments.
- **User Management:** The models utilize the Django Allauth User model.
- **Content Management:** Users can create and update own content, interact with other users by commenting on and liking content and comments.
- **Technical Design:** Separation of concern was implemented by deviding key components into individual Django Models *(see ERD)*. This allows for simple and reliable queries based on the primary key, as well as easy management and scalability.
- Relationships between the model fields are indicated with relationship lines on the ERD.
- **Security Practises:** Security best practices were obtained using CSRF Tokens for data protection and authentication using Django Allauth.

<details>
<summary> Click for Entity Relationship Diagram (ERD)</summary>

![Entity Relationship Diagram](/documentation/erd.png)
</details>


### Agile Development Methods 
- Epics
- User Stories
- MoSCoW Prioritization
- Kanban board

## Technology Used

### Libraries and Frameworks Used
[Django v4.2.13](https://docs.djangoproject.com/en/5.0/releases/4.2.13/) - Python web framework
[Django allauth](https://docs.allauth.org/en/latest/installation/index.html) - User account authentication and verification *(check: verif.)*
[Django Crispy Forms v2.1](https://django-crispy-forms.readthedocs.io/en/latest/install.html#installing-django-crispy-forms) - Simplifies the creation of forms
[Django ckeditor v6.7.1](https://pypi.org/project/django-ckeditor/) - Privides a handy richt text field widget for forms
[Django RichTextField v1.6.2](https://djangopackages.org/packages/p/django-richtextfield/) - Renders a customizable rich text editor for user posts
[Django Resized v1.0.2](https://pypi.org/project/django-resized/) - Handles resizing and format converting of images uploaded by users
[Pillow v10.3.0](https://pillow.readthedocs.io/en/stable/) - A Python imaging library, handles images in combination with the Django Resized Image Field
[Bootstrap v5.2.3](https://getbootstrap.com/docs/5.2/getting-started/download/) - Open-source CSS framework
[Crispy-Bootstrap v5 2024.2](https://pypi.org/project/crispy-bootstrap5/) - Provides Bootstrap-specific classes and styles to render forms
[Summernote v0.8.20.0](https://djangopackages.org/packages/p/django-summernote/) - Renders a customizable rich text editor for the admin panel
[Autoslug](https://django-autoslug.readthedocs.io/_/downloads/en/stable/pdf/) - Automatically generates slug field for improved UX for less experienced users
[cloudinary v1.36.0](https://cloudinary.com/documentation/django_integration) - Allows users to upload images
[dj3-cloudinary-storage v0.0.6](https://cloudinary.com/documentation/rails_activestorage) - Provides storage of images uploaded by users

### Programs Used
[diagrams.net](https://app.diagrams.net/) to create the layout flowchart and the database ERD
[Pixelied](https://pixelied.com/convert/jpg-converter/jpg-to-webp) to convert images into webp format
[Optimizilla](https://imagecompressor.com/) to compress image file size

## Features
*Testing and Bugs (separate)*
## Deployment and Local Development

### Neon Database

This project utilizes a relational database powered by [Neon.tech](https://neon.tech/), a serverless PostgreSQL solution.

- Log into or sign up for a Neon account.
- Create or navigate to your "Tier" (one free tier per user).
- Navigate to the "Dashboard" on the left side menu.
- In the section "Connection Details", you will find the link to the database displayed in the subsection "Connection String".

## Credits

- [Cloudinary](https://github.com/cloudinary-devs/my-django-app/blob/main/django_app/forms.py) - Code from Cloudinary [tutorial](https://cloudinary.com/documentation/django_helper_methods_tutorial) to allow users to upload images.
- [Django docs get_FOO_display()](https://docs.djangoproject.com/en/5.0/ref/models/instances/) - Return "human-readable" value of model fields.