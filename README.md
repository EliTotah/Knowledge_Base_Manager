
# Knowledge_Base_Manager

A command-line tool that simulates a support knowledge base. This knowledge base will store help articles (each with a title, content, and tags) that can be created, updated, and searched.

## Features

- **Add Article**: Adds a new article with a title, content, and tags.
- **Edit Article**: Allows you to modify an article's title, content, or tags.
- **Delete Article**: Deletes an article by its title.
- **Show Articles**: Displays all articles with their titles, content, and tags.
- **Search Articles**: Searches for articles by tags or keywords in the title/content.

## Requirements

- Python 3.x
- Standard Python libraries: `json`, `os`

## Installation

Clone the repository:

```bash
git clone https://github.com/EliTotah/Knowledge_Base_Manager.git
```

## Running the Application

To run the application, execute the following command:

```bash
python BaseManager.py
```

The application will present a menu where you can choose options such as adding, editing, deleting, or searching articles.

## Article format

Articles are stored in a JSON file and should have the following format:

```json
{
  "id": "A1",
  "title": "Article Title",
  "content": "Article Content",
  "tags": ["tag1", "tag2"]
}
```
