# Simple Online Marketplace built with Django

This repository is a tutorial for learning the basics of Django by building a simple online marketplace where people can buy and sell items. The project will cover essential aspects of web development such as authentication, communication between users, dashboard for your items, form handling, and customizations.

## Prerequisites

- Basic understanding of Python programming language
- Familiarity with HTML and CSS
- A text editor or IDE for coding
- Python 3.x installed on your system
- Django framework installed on your system
<br>

## Getting Started
<br>
To get started, clone this repository on your local system using the following command:

```
git clone https://github.com/ujstor/django-online-marketplace.git
```
<br>
After cloning the repository, navigate to the project directory using the following command:

```
cd django-online-marketplace
```
<br>
Create a virtual environment for the project using the following command:

```
python -m venv env
```
<br>
Activate the virtual environment using the following command:

| Platform | Shell | Command to Activate Virtual Environment |
| -------- | ----- | --------------------------------------- |
| POSIX | bash/zsh | `$ source <venv>/bin/activate` |
| POSIX | fish | `$ source <venv>/bin/activate.fish` |
| POSIX | csh/tcsh | `$ source <venv>/bin/activate.csh` |
| PowerShell | | `$ <venv>/bin/Activate.ps1` |
| Windows | cmd.exe | `C:\> <venv>\Scripts\activate.bat` |
| Windows | PowerShell | `PS C:\> <venv>\Scripts\Activate.ps1` |

<br>
Install the project dependencies using the following command:

```
pip install -r requirements.txt
```
<br>
Finally, run the Django development server using the following command:

```
python manage.py runserver
```

The server will start running on `http://localhost:8000/`. Open the URL in your web browser to see the online marketplace in action.
<br>
## Features

- User registration and login system
- User authentication and authorization
- Communication between users using messaging system
- Dashboard for users to manage their items
- Form handling and customizations for adding new items to the marketplace
<br>

## Contributing

Contributions are welcome! Please open an issue or a pull request if you find any bug or want to suggest any feature.
<br>

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.