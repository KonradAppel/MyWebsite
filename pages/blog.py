import streamlit as st
from notion_client import Client
import os
from dotenv import load_dotenv

# Lade die .env Datei
if os.path.exists('.env'):
    load_dotenv()

# Greife auf die Umgebungsvariablen zu
notion_token = os.getenv("NOTION_TOKEN")
if not notion_token:
    st.error("Der Notion API-Token ist nicht gesetzt.")
else:
    notion_client = Client(auth=notion_token)

# Hauptseite-ID in Notion
main_page_id = os.getenv("NOTION_TOKEN_PAGE")
if not main_page_id:
    st.error("Der Notion API-Token ist nicht gesetzt.")

def app():
    st.title("Blog")
    st.write("Welcome to my travel blog!")
    
    # Caching der Unterseiteninformationen (Blog-Beiträge)
    @st.cache_data(ttl=3600)
    def get_blog_entries(_notion_client, page_id):
        blocks = _notion_client.blocks.children.list(block_id=page_id).get("results")
        blog_entries = [block for block in blocks if block["type"] == "child_page"]
        return blog_entries

    # Caching des Inhalts eines Blog-Beitrags
    @st.cache_data(ttl=3600)
    def get_entry_content(_notion_client, entry_id):
        return _notion_client.blocks.children.list(block_id=entry_id).get("results")

    # Alle Blog-Einträge (Unterseiten) abrufen
    blog_entries = get_blog_entries(notion_client, main_page_id)
    blog_titles = {entry['id']: entry['child_page']['title'] for entry in blog_entries}

    # Blog-Einträge untereinander anzeigen
    for entry_id, title in blog_titles.items():
        with st.expander(title):
            entry_content = get_entry_content(notion_client, entry_id)
            for block in entry_content:
                block_type = block["type"]

                if block_type == "paragraph":
                    if block["paragraph"]["rich_text"]:
                        text = "".join([text_part["text"]["content"] for text_part in block["paragraph"]["rich_text"]])
                        st.write(text)

                elif block_type == "image":
                    image_url = block["image"]["file"]["url"] if "file" in block["image"] else block["image"]["external"]["url"]
                    st.image(image_url)

                elif block_type == "code":
                    code_text = "".join([text_part["text"]["content"] for text_part in block["code"]["rich_text"]])
                    language = block["code"]["language"]
                    st.code(code_text, language=language)

app()
