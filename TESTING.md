# Helping Hands, Happy Hearts

You can view the live project here [Helping Hands, Happy Hearts](https://helping-hands-happy-hearts-546cab7eb98a.herokuapp.com/)<br>
*(To open in a new window, press "ctrl" (or ⌘ for Mac) + click on the link)*

You can read the documentation in the [README.md](README.md)

## Table of contents

- [Validator Testing](#validator-testing)
    - [Python](#python)
    - [HTML](#html)
    - [CSS](#css)
    - [Lighthouse Testing](#lighthouse-testing)
    - [WAVE Web Accessibility Evaluation Tool](#wave-web-accessibility-evaluation-tool)
    - [Coolors contrast checker](#coolors-color-contrast-checker)
- [Manual Testing](#manual-testing)
    - [Browser Compatibility](#browser-compatibility)
    - [Responsiveness](#responsiveness-testing)
- [Bugs](#bugs)
- [Programs Used](#programs-used-for-this-testingmd)

## Validator Testing

### Python

[Python Linter Validator]( https://pep8ci.herokuapp.com/) provided by the Code Institute according to the PEP 8 style guide for validating the Python code.

- All custom written Python code files passed through the Python Linter Validator according to the PEP 8 style without errors.

    <details>
    <summary>Click for image board/admin.py</summary>

    ![board/admin.py](/documentation/testing/board-admin.png)
    </details>

    <details>
    <summary>Click for image board/apps.py</summary>

    ![board/apps.py](/documentation/testing/board-apps.png)
    </details>

    <details>
    <summary>Click for image board/forms.py</summary>

    ![board/forms.py](/documentation/testing/board-forms.png)
    </details>

    <details>
    <summary>Click for image board/models.py</summary>

    ![board/models.py](/documentation/testing/board-models.png)
    </details>

    <details>
    <summary>Click for image board/views.py</summary>

    ![board/views.py](/documentation/testing/board-views.png)
    </details>

    <details>
    <summary>Click for image board/urls.py</summary>

    ![board/urls.py](/documentation/testing/board-urls.png)
    </details>

    <details>
    <summary>Click for image core/urls.py</summary>

    ![board/urls.py](/documentation/testing/core-urls.png)
    </details>

    <details>
    <summary>Click for image core/settings.py</summary>

    ![board/settings.py](/documentation/testing/core-settings.png)
    </details>

    <details>
    <summary>Click for image home/apps.py</summary>

    ![home/apps.py](/documentation/testing/home-apps.png)
    </details>

    <details>
    <summary>Click for image home/urls.py</summary>

    ![home/urls.py](/documentation/testing/home-urls.png)
    </details>

    <details>
    <summary>Click for image home/views.py</summary>

    ![home/views.py](/documentation/testing/home-views.png)
    </details>
    <br>

- The Django’s Allauth templates do not pass through the linter because Django templates have their own style requirements to ensure proper rendering and translation of the templates and do not follow the PEP 8 guidelines.

    <details>
    <summary>Click for image testing allauth login</summary>

    ![allauth login](/documentation/testing/allauth-login.png)
    </details>

    <details>
    <summary>Click for image testing allauth signup</summary>

    ![allauth signup](/documentation/testing/allauth-signup.png)
    </details>
    <br>

### HTML

[World Wide Web Consortium's validator](https://validator.w3.org/) was used for validating the HTML code by URI input as well as loading the source code of each page from the browser by direct input into the validator. The source code is used to validate the Django template tags as HTML code.

All testing for HTML was performed on the deployed website.

<details>
<summary>Click for image HTML validator testing by URI</summary>

![html-uri](/documentation/testing/html-uri.png)
</details>

<details>
<summary>Click for representative image HTML validator testing for all HTML files</summary>

![html](/documentation/testing/html.png)
</details>

### CSS

No errors were detected when passing through the official [World Wide Web Consortium (W3C)](https://validator.w3.org/) validator for CSS.

<details>
<summary>Click for image css validator testing</summary>

![css](/documentation/testing/css.png)
</details>

### JavaScript

The JavaScript passed without errors through the [JSHint Validator, a JavaScript Code Quality Tool](https://jshint.com/). 

<details>
<summary>Click for image JavaScript validator testing</summary>

![css](/documentation/testing/jshint.png)
</details>

### Lighthouse Testing

All Lighthouse testing was performed on the deployed website using Chrome Developer Tools Lighthouse Report.

![Lighthouse desktop](/documentation/testing/lighthouse-desktop.png)

![Lighthouse desktop](/documentation/testing/lighthouse-mobile.png)

### WAVE Web Accessibility Evaluation Tool

[Wave WebAIM Validator](https://wave.webaim.org/) was used to validate web accessibility on the deployed website.

![webaim](/documentation/testing/webaim.png)

Alerts arise on overview of posts in Offers & Requests. The bootstrap cards are anchored and this approach doesn't seem to sit well with the validator. 

Contrast errors are due to insufficient contrast of links in Django Allauth templates.

### Coolors Color Contrast Checker

[Coolors Color Contrast Checker](https://coolors.co/contrast-checker/333333-f5f5f5) was used to validate color contrast for web accessability in terms of readability.

![contrast](/documentation/contrast.png)

## Manual Testing

| Feature                    | Action                                                                         | Outcome                                                                   | Result  |
|----------------------------|--------------------------------------------------------------------------------|---------------------------------------------------------------------------|---------|
| Sign-Up                    | Click Sign Up on navbar                                                        | Form for email  username password                                         | success |
| Sign-Up                    | User Feedback                                                                  | Success message including username displayed                              | success |
| Sign-In                    | Click on Sign-In on navbar                                                     | Login form displayed                                                      | success |
| Sign-In                    | User Feedback                                                                  | Success message including username displayed                              | success |
| Sign-In                    | Enter incorrect credentials                                                    | Error message for invalid login                                           | success |
| Create Post                | Click Create Post on navbar or button                                          | Login to create post displayed                                            | success |
| Create Post                | Submit empty form or leave out required fields marked with asterisk            | Error message and no submission                                           | success |
| Create Post                | Fill form                                                                      | Publish post immedately                                                   | success |
| Create Post                | Style post using RichTextField                                                 | Styled post published                                                     | success |
| Create Post                | Click on calender widget                                                       | Choose a target date from calender                                        | success |
| Create Post                | Click on fields with dropdown menu                                             | User can choose options for fields from dropdown menus                    | success |
| Create Post                | User Feedback                                                                  | Success message add post                                                  | success |
| Read Post                  | Go to Offers & Requests page                                                   | List of posts (newest first)                                              | success |
| Read Post                  | Click on post on overview board offers and requests                            | correct post opens displaying all details                                 | success |
| Read Post                  | Click on button return to overview                                             | Return to Offers & Requests page                                          | success |
| Update Post                | Click edit button (own posts only)                                             | Edit post details                                                         | success |
| Update Post                | Click on submit button to edit post                                            | Post immediately updated                                                  | success |
| Update Post                | Remove required fields and submit empty                                        | Error message and no submission                                           | success |
| Update Post                | Click on button no edit and to return to post                                  | Return to post without updating                                           | success |
| Update Post                | User Feedback                                                                  | Success message  post updated                                             | success |
| Update Post                | Try accessing a post from other users through URL (incognido mode and friends) | Updating posts from other users not possible                              | success |
| Sign out                   | Click on Sign Out on navbar                                                    | Sign out from user account                                                | success |
| Sign out                   | Sign out confirmation                                                          | Confirmation required to sign out in case of a mistake or change of heart | success |
| Delete post                | Click on delete post in admin panel                                            | Delete post as admin                                                      | success |
| Delete post                | Click on delete post (logged in)                                               | Delete own post as user                                                   | success |
| Delete post                | Try accessing a post from other users through URL (incognido mode and friends) | Deleting posts from other users not possible                              | success |
| Delete post                | Click button return to post                                                    | Return to post without deleting post                                      | success |
| Like Post                  | Click like button (logged in)                                                  | Number of likes updates after liking a post and success message           | success |
| Like Post                  | Not logged in                                                                  | Number of likes is visible if not logged in but button is not displayed   | success |
| Unlike Post                | Click on button again to unlike post (logged in)                               | Number of likes updates after uniking a post and success message          | success |
| Web accessability          | Explore the website using a screenreader                                       | Links are focusable using keyboard                                        | success |
| Website Orientation        | Navigate between pages                                                         | Verify indication of current location on navigation bar                   | success |
| Contact details site owner | Click on email link                                                            | Opens in default email app                                                | success |

### Browser Compatibility

The browser compatibility was tested on the deployed project on Chrome, Microsoft Edge, Apple Safari and Mozilla Firefox. The manual testing table above was performed on all browsers to ensure good user experience regardless of the browser used.

### Responsiveness Testing

![mockup-min](/documentation/testing/mockup-min.png)

The responsiveness was tested on Chrome Developer Tools as well as by friends and family on various devices and screensizes. 

Responsiveness was obtained primarily by utilizing Bootstrap 5 grid system. This made media queries in css stylesheet unnecessary and allowed for concise code and constistent performance in responsiveness.

## Bugs

### Unsolved Bugs 

There are no unsolved bugs in the deployed project.

### Solved Bugs

All identified and fixed bugs are thoroughly documented within the associated commit messages. This provides a clear record of the development process and ensures traceability for future reference. 

| Bug                                               | Description                                                                              | Solution Applied                                                                                                                                                       | Result |
|---------------------------------------------------|------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|
| Active class on navigation items                  | Active class underline to indicate users location on website not displaying on two items | Fix typo in url_name in header template                                                                                                                                | Solved |
| Active class on navigation item Offers & Requests | Active class underline to indicate users location on website not displaying              | Add missing quotation mark                                                                                                                                             | Solved |
| Redirect urls                                     | Not performing consistently due to other changes in code                                 | Import reverse_lazy and replace hardcoded success URLs with reverse_lazy calls                                                                                         | Solved |
| Delete Post                                       | Error at submission of form                                                              | Fix form on post_confirm_delete.html from action=post to method=POST to implement the DeleteView correctly                                                             | Solved |
| Default post_image                                | Error on page load if no image uploaded by user                                          | Fix logic for placeholder image on post_detail.html by first checking if there is an uploaded user image on the post, instead of checking for placeholder in image url | Solved |
| No post_image uploaded                            | Error at submission of form                                                              | Add method to view to first save form without submitting to handle optional image upload                                                                               | Solved |
| CloudinaryField                                   | Forced fetched format not working                                                        | Change Field to ResizedImageField                                                                                                                                      | Solved |
| Location list tuples                              | Error due to incorrect code                                                              | Add missing commas                                                                                                                                                     | Solved |

## Programs Used for this TESTING.md

- [Python Linter Validator]( https://pep8ci.herokuapp.com/) provided by the Code Institute according to the PEP 8 style guide for validating the Python code.
- [World Wide Web Consortium's validator](https://validator.w3.org/) was used for validating the HTML code.
- [World Wide Web Consortium (W3C)](https://validator.w3.org/) validator for CSS stylesheet.
- [[JSHint Validator, a JavaScript Code Quality Tool](https://jshint.com/)] for JavaScript script.
- Chrome Developer Tools for Lighthouse Report.
- [Wave WebAIM Validator](https://wave.webaim.org/) was used to validate web accessibility on the deployed website.
- [Coolor Color Contract Checker](https://coolors.co/contrast-checker/333333-f5f5f5) to assess contrast for accessibility.
- [Table-magic](https://stevecat.net/table-magic/) - to create manual testing for this TESTING.md.