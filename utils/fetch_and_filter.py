import requests
import xml.etree.ElementTree as ET
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")

def fetch_and_filter_relevant_papers(query, category="cs.AI", max_results=20):
    search_url = f"http://export.arxiv.org/api/query?search_query=cat:{category}&start=0&max_results={max_results}"
    response = requests.get(search_url)

    if response.status_code != 200:
        return []

    root = ET.fromstring(response.content)
    entries = root.findall('{http://www.w3.org/2005/Atom}entry')

    papers = []
    for entry in entries:
        title = entry.find('{http://www.w3.org/2005/Atom}title').text.strip().replace('\n', ' ')
        summary = entry.find('{http://www.w3.org/2005/Atom}summary').text.strip().replace('\n', ' ')
        link = entry.find('{http://www.w3.org/2005/Atom}id').text
        authors = ", ".join(
            [author.find('{http://www.w3.org/2005/Atom}name').text for author in entry.findall('{http://www.w3.org/2005/Atom}author')]
        )
        papers.append({"title": title, "summary": summary, "link": link, "authors": authors})

    # Semantic Search using SentenceTransformer
    query_emb = model.encode(query, convert_to_tensor=True)
    for paper in papers:
        title_emb = model.encode(paper["title"], convert_to_tensor=True)
        score = util.cos_sim(query_emb, title_emb).item()
        paper["score"] = round(score, 4)

    sorted_papers = sorted(papers, key=lambda x: x["score"], reverse=True)
    return sorted_papers
