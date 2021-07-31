# Jungle Devs - Django Challenge #001

## Development
- Clone this repository and cd its directory:
```bash
git clone https://github.com/pedrodotpy/django-challenge-001
cd django-challenge-001
```

- Create your `.env` file using `.env-example` as an example.


- Create a virtual environment and activate it:
```bash
virtualenv -p python3 venv
source venv/bin/activate
```

- Install the requirements:
```bash
pip install -r requirements.txt
```

- Start the postgresql container. **Important:** `POSTGRES_HOST`, inside the `.env`, must be referencing your local host.
```bash
docker-compose up db
```

- Run the server
```bash
python manage.py runserver 8000
```

## Production
- Clone this repository and cd its directory:
```bash
git clone https://github.com/pedrodotpy/django-challenge-001
cd django-challenge-001
```

- Create your `.env` file using `.env-example` as an example.


- Make sure your `.env` is correct:
  1. `POSTGRES_HOST` must have the value `db`.
  2. It's highly advisible to change the `SECRET_KEY`.
 ```bash
 POSTGRES_HOST=db
 SECRET_KEY=change_me
  ```

- Active the containers:
```bash
docker-compose up
```

- Run manage.py commands
```bash
docker-compose exec app python manage.py [command]
```

## SCHEMA
This API has an auto-generated OpenAPI schema. Their endpoints are the following:<br/>
- UI - **api/schema/swagger-ui**
- YML - **api/schema**

There's also a Postman collection in this repo.

## Description

**Challenge goal**: The purpose of this challenge is to give an overall understanding of a backend application. You’ll be implementing a simplified version of a news provider API. The concepts that you’re going to apply are:

- REST architecture;
- Authentication and permissions;
- Data modeling and migrations;
- PostgreSQL database;
- Query optimization;
- Serialization;
- Production builds (using Docker).

**Target level**: This is an all around challenge that cover both juniors and experience devs based on the depth of how the concepts were applied.

**Final accomplishment**: By the end of this challenge you’ll have a production ready API.

## Acceptance criteria

- Clear instructions on how to run the application in development mode
- Clear instructions on how to run the application in a Docker container for production
- A good API documentation or collection
- Login API: `/api/login/`
- Sign-up API: `/api/sign-up/`
- Administrator restricted APIs:
  - CRUD `/api/admin/authors/`
  - CRUD `/api/admin/articles/`
- List article endpoint `/api/articles/?category=:slug` with the following response:
```json
[
  {
    "id": "39df53da-542a-3518-9c19-3568e21644fe",
    "author": {
      "id": "2d460e48-a4fa-370b-a2d0-79f2f601988c",
      "name": "Author Name",
      "picture": "https://picture.url"
    },
    "category": "Category",
    "title": "Article title",
    "summary": "This is a summary of the article"
  },
  ...
]
```
- Article detail endpoint `/api/articles/:id/` with different responses for anonymous and logged users:

    **Anonymous**
    ```json
    {
      "id": "39df53da-542a-3518-9c19-3568e21644fe",
      "author": {
        "id": "2d460e48-a4fa-370b-a2d0-79f2f601988c",
        "name": "Author Name",
        "picture": "https://picture.url"
      },
      "category": "Category",
      "title": "Article title",
      "summary": "This is a summary of the article",
      "firstParagraph": "<p>This is the first paragraph of this article</p>"
    }
    ```

    **Logged user**
    ```json
    {
      "id": "39df53da-542a-3518-9c19-3568e21644fe",
      "author": {
        "id": "2d460e48-a4fa-370b-a2d0-79f2f601988c",
        "name": "Author Name",
        "picture": "https://picture.url"
      },
      "category": "Category",
      "title": "Article title",
      "summary": "This is a summary of the article",
      "firstParagraph": "<p>This is the first paragraph of this article</p>",
      "body": "<div><p>Second paragraph</p><p>Third paragraph</p></div>"
    }
    ```
