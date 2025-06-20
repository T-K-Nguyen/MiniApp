# Mini Application

## Overview
The Mini Application is a simple web-based task management tool that allows users to create, manage, and track their tasks. This project includes a login system with a visually appealing night mountain-themed interface.


<p align="center"> 
 <img src="Screenshots/num1.png" width="600"/> 
 <br/> <i>Figure: Application to-do list</i> 
</p>


## Features
- User authentication (login and registration)
- Responsive design with a full-page background
- Task management functionality (to be expanded)
- Small database management

## Screen Sequence
<table>
  <tr>
    <td align="center">
      <img src="Screenshots/login_screen.png" width="800"/><br/>
      <i>Authentication normal view</i>
    </td>
    <td align="center">
      <img src="Screenshots/login_phone.png" width="200"/><br/>
      <i>Authentication phone view</i>
    </td>
  </tr>
  <tr>
    <td align="center">
      <img src="Screenshots/register_screen.png" width="800"/><br/>
      <i>Register normal view</i>
    </td>
    <td align="center">
      <img src="Screenshots/register_phone.png" width="200"/><br/>
      <i>Register phone view</i>
    </td>
  </tr>
<tr>
    <td align="center">
      <img src="Screenshots/num1.png" width="800"/><br/>
      <i>Main page normal view</i>
    </td>
    <td align="center">
      <img src="Screenshots/num_phone.png" width="200"/><br/>
      <i>Main page phone view</i>
    </td>
  </tr>
</table>

## Prerequisites
- Python 3.x
- Flask (web framework)
- Flask-Login (for user authentication)
- Flask_SQLAlchemy (for SQLite database)
- Flask-Bootstrap (for styling)
- A web browser to view the application

## Installation

### Clone the Repository
```bash
git clone https://github.com/T-K-Nguyen/MiniApp.git
```

### Set Up a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Install Dependencies
```bash
pip install flask flask-login flask-bootstrap flask_sqlalchemy werkzeug
```

### Run the Application
```bash
python app.py
```
Open your browser and navigate to `http://127.0.0.1:5000/login` to access the login page (your's maybe different).

## Usage
1. Open the application in your browser.
2. Log in with an existing account or register a new one (username=thuan, password=ADMIN).
3. Once logged in, you can manage your todo list (functionality to be implemented).

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m "Description of changes"`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- Inspired by night-themed UI designs.
- Built with Flask and Bootstrap for a clean, responsive interface.