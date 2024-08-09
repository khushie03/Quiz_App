from serpapi import GoogleSearch

def scholar_section(query):
    if not query:
        return "No query provided."
    
    params = {
        "engine": "google_scholar",
        "q": query,
        "api_key": "your_Serp_api_key"
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    organic_results = results.get("organic_results", [])

    if not organic_results:
        return "No results found."

    formatted_results = []
    for result in organic_results:
        title = result.get('title', 'No title')
        link = result.get('link', 'No link')
        snippet = result.get('snippet', 'No snippet')
        
        formatted_result = f"**Title:** {title}\n**Link:** {link}\n**Snippet:** {snippet}"
        formatted_results.append(formatted_result)
    
    return formatted_results
