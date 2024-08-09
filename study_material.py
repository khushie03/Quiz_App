from serpapi import GoogleSearch

def scholar_section(query):
    if not query:
        return "No query provided."
    
    params = {
        "engine": "google_scholar",
        "q": query,
        "api_key": "c8b912a9727723424bffac813a03eb897d43cee8cfac0741c3b266a6cb8bef71"
    }

    try:
        search = GoogleSearch(params)
        results = search.get_dict()
        organic_results = results.get("organic_results", [])
        
    except Exception as e:
        print(f"Error fetching results: {e}")
        return []
    formatted_results = []
    for result in organic_results:
        title = result.get('title', 'No title')
        link = result.get('link', 'No link')
        snippet = result.get('snippet', 'No snippet')
        
        formatted_result = f"**Title:** {title}\n**Link:** {link}\n**Snippet:** {snippet}"
        formatted_results.append(formatted_result)
    
    return formatted_results

