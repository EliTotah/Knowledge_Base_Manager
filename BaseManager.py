import json
import os

articles_file = 'articles.json'

# read articles from memory
def read_articles():
    try:
        if os.path.exists(articles_file):
            with open(articles_file, 'r') as file:
                data = json.load(file)  
            return data.get('articles', [])  
        return []  
    except (json.JSONDecodeError, IOError) as e: 
        print(f"Error reading file: {e}")
        return []

# save articles into memory
def save_articles(articles):
    try:
        with open(articles_file, 'w') as file:
            json.dump({'articles': articles}, file, indent=4)  
    except (IOError, json.JSONDecodeError) as e:  
        print(f"Error saving file: {e}")

# display articles
def show_articles(articles):
    if not articles:
        print("No articles available")
        return
    for article in articles:
        print(f"\n{article['id']}:")
        print(f"Title: {article['title']}")
        print(f"Content: {article['content']}")
        print(f"Tags: {', '.join(article['tags'])}")

# add article to the list
def add_article():
    title = input("Enter atricle title: ")
    content = input("Enter article content: ")
    # add tags one by one, until we get 'done'
    tags = []
    while True:
        tag = input("Enter a tag for the article and press Enter to add another. Type 'done' when you are finished: ")
        if tag.lower() == 'done':
            break
        tags.append(tag)
    articles = read_articles()
    # compute the new id
    last_id = articles[-1]['id'] if articles else 'A0'
    id = 'A' + str(int(last_id[1:]) + 1)
    # check that the article is not empty (we print error only if all the fields are empty)
    if not title.strip() and not content.strip() and not any(tag.strip() for tag in tags):
        print("Error: The article cannot be added because it is empty.")
        return
    article = {
        'id' : id,
        'title': title,
        'content': content,
        'tags': tags
    }
    articles.append(article)
    save_articles(articles)
    print(f"Article '{title}' added successfully")

# delete article from the list, by id
def delete_article():
    id = input("Enter atricle id: ")
    articles = read_articles()
    for i, article in enumerate(articles):
        if article['id'] == id:
            del articles[i]
            save_articles(articles)
            print(f"Article '{id}' deleted successfully")
            return
    print(f"Article '{id}' not found.")

#edit article by id
def edit_article():
    id = input("Enter atricle id: ")
    articles = read_articles()
    for article in articles:
        if article['id'] == id:
            newTitle = input("Enter new title: ")
            newContent = input("Enter new content: ")
            newTags = []
            while True:
                tag = input("Enter a tag for the article and press Enter to add another. Type 'done' when you are finished: ")
                if tag.lower() == 'done':
                    break
                newTags.append(tag)
            article['title'] = newTitle
            article['content'] = newContent
            article['tags'] = newTags
            save_articles(articles)
            print(f"Article '{id}' edited successfully")
            return
    print(f"Article '{id}' not found.")

# search for articles by keyword or tag
def search_articles():
    tag = input("Enter atricles tag or keyword: ")
    articles = read_articles()
    filtered_articles = []
    for article in articles:
        # check if tag is exists
        for t in article['tags']:
            if t.lower() == tag.lower():
                filtered_articles.append(article)
        # check if keyword exists in title or content
        if tag.lower() in article['title'].lower() or tag.lower() in article['content'].lower():
            filtered_articles.append(article)
    show_articles(filtered_articles)
    
def menu():
    print("\n--- Knowledge Base Manager ---")
    print("1. Show articles")
    print("2. Add article")
    print("3. Delete article")
    print("4. Edit article")
    print("5. Search articles")
    print("6. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        articles = read_articles()
        show_articles(articles)
    elif choice == '2':
        add_article()
    elif choice == '3':
        delete_article()
    elif choice == '4':
        edit_article()
    elif choice == '5':
        search_articles()
    elif choice == '6':
        print("bye!")
        exit()
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    while True:
        menu()