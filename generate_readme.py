import miniflux

from os import getenv, remove, path
from datetime import datetime

target_file = "README.md"

if path.exists(target_file): remove(target_file)
core_url = getenv("MINIFLUX_API_URL", "https://rss.hjkl.no")
api_key = getenv("MINIFLUX_API_KEY", "REDACTED")

client = miniflux.Client(core_url, api_key=api_key)
feeds = client.get_feeds()

header = f"""# rss feeds
> generated: {datetime.now()}

"""

with open(target_file, "a") as f:
    f.write(header)
    for list_key in feeds:
        title = list_key['title']
        feed_url = list_key['feed_url']
        site_url = list_key['site_url']
        temp =  (f"""- {title} 
        \n\t- URL: [{site_url}]({site_url})
        \n\t- RSS: [{feed_url}]({feed_url})
""")
        f.write(temp)