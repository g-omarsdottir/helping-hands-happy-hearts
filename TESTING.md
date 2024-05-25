# Helping Hands, Happy Hearts

You can view the live project here [Helping Hands, Happy Hearts](https://helping-hands-happy-hearts-546cab7eb98a.herokuapp.com/)<br>
*(To open in a new window, press "ctrl" (or ⌘ for Mac) + click on the link)*

You can read the documentation in the [README.md](README.md)

## Table of contents

Automated Testing
Validator Testing
Python Linter
HTML
CSS
Lighthouse Testing
WAVE Web Accessibility Evaluation Tool
Manual Testing

## Automated Testing

### Validator Testing

#### Python

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

#### HTML

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


#### CSS

No errors were detected when passing through the official [World Wide Web Consortium (W3C)](https://validator.w3.org/) validator for CSS.

<details>
<summary>Click for image css validator testing</summary>

![css](/documentation/testing/css.png)
</details>

#### Lighthouse Testing

All Lighthouse testing was performed on the deployed website.

![Lighthouse desktop](/documentation/testing/lighthouse-desktop.png)

![Lighthouse desktop](/documentation/testing/lighthouse-mobile.png)

#### WAVE Web Accessibility Evaluation Tool

[Wave WebAIM Validator](https://wave.webaim.org/) was used to validate web accessibility on the deployed website.

![webaim](/documentation/testing/webaim.png)

Alerts arise on overview of posts in Offers & Requests. The bootstrap cards are anchored and this approach doesn't seem to sit well with the validator. 

Contrast errors are due to insufficient contrast of links in Django Allauth templates.

### Manual Testing

