# Django Personal Website

Welcome to the repository for my personal website! This Django-based web app showcases my portfolio, projects, and provides a contact form. It is designed with a modern dark theme and includes animations for a dynamic user experience.

## Live Website

You can view the live website at: [mahdimeyghani.pythonanywhere.com](https://mahdimeyghani.pythonanywhere.com)

## Features

- **Home Page**: Displays a brief introduction and showcases Python projects with images, descriptions, and links to their source code.
- **Contact Page**: Includes a form to get in touch with me, with error handling and success messages.
- **Responsive Design**: Optimized for both desktop and mobile views.
- **Animations**: Uses Animate.css for scroll-triggered animations.

## Technologies Used

- **Django**: Web framework for the backend.
- **Bootstrap**: Frontend framework for responsive design.
- **Animate.css**: Library for animations.
- **JavaScript**: For scroll-triggered animations.
- **CSS**: Custom styles for a unique look and feel.

## Files Structure

### `base.html`

The base template for the website that includes the common layout and navigation for all pages.

### `home.html`

The homepage template that extends `base.html` and displays an introduction, project list, and a link to more projects.

### `contact.html`

The contact page template that extends `base.html` and includes a form for users to contact me.

### `style.css`

Custom CSS file for styling the website. Includes styles for typography, layout, images, projects, and responsive design.

### `animations.js`

JavaScript file for handling animations using the Intersection Observer API and Animate.css.

## Static and Media Files

- **CSS**: Located in `static/portfolio_website/style.css`.
- **JavaScript**: Located in `static/portfolio_website/animations.js`.
- **Images**: Located in `static/portfolio_website/pictures/`.

## Setup and Installation

To run this project locally, follow these steps:

1. **Clone the repository**:

    ```bash
    git clone https://github.com/Mahdi-Meyghani/Django-Personal-Website.git
    ```

2. **Navigate to the project directory**:

    ```bash
    cd Django-Personal-Website
    ```

3. **Create a virtual environment and activate it**:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use: venv\Scripts\activate
    ```

4. **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

5. **Apply migrations**:

    ```bash
    python manage.py migrate
    ```

6. **Run the development server**:

    ```bash
    python manage.py runserver
    ```

7. **Open your browser and go to** `http://localhost:8000`

## Contributing

Feel free to contribute to this project. You can submit issues or pull requests on the [GitHub repository](https://github.com/Mahdi-Meyghani/Django-Personal-Website).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

You can contact me via the contact form on the [website](https://mahdimeyghani.pythonanywhere.com) or through my [GitHub profile](https://github.com/Mahdi-Meyghani).
