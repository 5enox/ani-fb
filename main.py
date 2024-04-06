import anipy_cli
from upload import handle_download_upload


def search_and_choose_episode(search_query, episode):
    # Query for the search query
    entry = anipy_cli.Entry()
    query_class = anipy_cli.query(search_query, entry)
    links_and_names = query_class.get_links()
    # Print the available episodes and their links
    print("Available Episodes:")
    for i, name in enumerate(links_and_names[1]):
        print(f"{i+1}. {name}")

    # Choose an episode
    choice = int(input("Enter the episode number you want to download: "))
    chosen_link = links_and_names[0][choice-1]
    chosen_link = f'https://gogoanime.gg{chosen_link}'
    # Generate the episode link for the chosen episode
    entry.category_url = chosen_link
    entry.ep = episode  # Assuming the default episode is 1 for the chosen anime
    ep_class = anipy_cli.epHandler(entry)
    entry = ep_class.gen_eplink()
    url_class = anipy_cli.videourl(entry, "best")
    # generate stream url (this also, automatically generates the embed url)
    url_class.stream_url()
    # get your entry back filled with stream and embed url fields
    entry = url_class.get_entry()
    download_link = entry.stream_url
    return download_link


# Example usage:
search_query = input("Enter the name of the anime you want to download: ")
episode = input("Enter the episode number you want to download: ")
download_link = search_and_choose_episode(search_query, episode)
print(download_link)
handle_download_upload(download_link)
