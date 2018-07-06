# Django Drivers App
Driver Management application written in Python (Django).

**Components:**
- UI to enable intrested parties to search for information pertaining to a given driver etc.
- An interface to manage Drivers data using CRUDE operations(*CREATE,REMOVE,UPDATE,EDIT*).

**Pre-requisites:**
- python3 (v3.5) or latest
- python-pip3 (v10.0.1) or latest

## Installation
* It is necessary to install virtualenv, If not, run this:
```bash
    $ pip install virtualenv
```
* Then, use the 'Git' to clone the repo to your PC
    ```bash
        $ git clone git@github.com:Nkirui/maderesawa.git
    ```
    
  * #### Dependencies
  1. cd into your cloned repo as follows:
      ```bash
          $ cd maderesawa
      ```
  2. Create and fire up your virtual environment your best way:
      ```bash
          $ virtualenv  venv -p python3
          $ source venv/bin/activate
      ```
  3. Then install the dependencies needed to run the app:
      
      ```bash
          $ pip install -r requirements.txt
      ```
  4. Make those migrations work
      ```bash
          $ python manage.py makemigrations
          $ python manage.py migrate
      ```
  5. to access the admin panel
      ```bash
      $ python manage.py createsuperuser
      ```

* #### Run It
    Fire up the server using this one simple command:
    ```bash
        $ python manage.py runserver
    ```
    You can now access the site by visting the url below on your favourite browser
    ```
        http://localhost:8000
    ```
