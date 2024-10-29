# MyWebsite
This project is designed for individuals who want to create a personal website. It includes sections for a CV, detailing work experience, education, skills, and projects. Additionally, it features an about page, a contact page with social media links and various contact methods, and a blog section for sharing experiences, thoughts, ideas, and travel stories.

## Initial Setup

### Prerequisites

This project uses Poetry for dependency and package management. Ensure you have Python 3.10.xy installed. It's recommended to use `pyenv` for managing Python versions. You also need to install Poetry.

- [Pyenv Installation Guide](https://pypi.org/project/pyenv/#description)
- [Poetry Installation Guide](https://python-poetry.org/docs/)

#### Installing pyenv and Python

On macOS, you can install `pyenv` using Homebrew:

1. Open a Terminal on your Mac (`command` + `space` and type Terminal).
2. Install Homebrew by following the instructions from the official website [Homebrew](https://brew.sh).
3. Install `pyenv` using Homebrew:
    ```bash
    brew install pyenv
    ```
4. Install Python 3.12 with `pyenv`:
    ```bash
    pyenv install 3.12
    ```
5. Set the installed Python version as the global default:
    ```bash
    pyenv global 3.12
    ```

#### Installing Poetry

You can install Poetry via Homebrew:

6. Install Poetry:
    ```bash
    brew install poetry
    ```

### Project Installation

#### Cloning the Project

1. Create a directory where you want to save the project (`path/to/your/folder`)
2. Open a Terminal and navigate to the folder:
    ```bash
    cd path/to/your/folder
    ```
2. Clone the project repository from GitLab using the https:
    ```bash
    git clone https://github.com/KonradAppel/MyWebsite.git
    ```
    > If you are not allowed to download the project, create your own `Access Token` in GitLab.

#### Installing Dependencies

3. After successfully downloading the project open a Terminal and navigate to the main folder of the project:
    ```bash
    cd path/to/your/folder/mywebsite
    ```
4. Install the project dependencies using Poetry:
    ```bash
    poetry install
    ```
    > After installation the virtualenvironment is not yet findeable by VSCode. Thats why we have to activate the newly created virtual environment.
5. Activate the virtual environment created by Poetry:
    ```bash
    poetry shell
    ```
    > If you want to know where the virtual environment is stored enter `poetry env info`.
    > If VSCode can not finde the environment copy the executable path from the `poetry env info` message to help VSCode find it. Once VSCode knows this environment it shouldn't make any problems.

## Running the App

1. Open a Terminal and navigate to the main folder of the project:
    ```bash
    cd path/to/your/folder/mywebsite
    ```

2. If you are not already in the poetry kia environment, activate the virtual environment by:
    ```bash
    poetry shell
    ```
3. Start the Streamlit app:
    ```bash
    streamlit run app.py
    ```
4. The App should automatically start in the Browser.

> To stop the app, close the Terminal or press `Ctrl + C`.