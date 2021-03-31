from notion.client import NotionClient

def get_trash(client):
    query = {
        'sort' : "Relevance",
        'query': '',
        'limit': 100,
        'spaceId': client.current_space.id,
        'source' : 'trash',
        'type' : "BlocksInSpace",
        'filters' : {
            "isDeletedOnly": True,
            "excludeTemplates": False,
            "isNavigableOnly": True,
            "requireEditPermissions": False,
            "ancestors": [],
            "createdBy": [],
            "editedBy": [],
            "lastEditedTime": {},
            "createdTime": {}
}
    }
    results = client.post('search', query)
    block_ids = results.json()['results']

    return block_ids

def show_names(client, blocks_ids):
    for block_id in block_ids:
            id = block_id['id']
            page = client.get_block(id)
            print(page.title)
        

if __name__== "__main__":

    with open('token.txt', 'r') as file:
        token = file.read().replace('\n', '')
    client = NotionClient(token_v2=token)

    print('Start')
 
    block_ids = get_trash(client, "")
    show_names(client, block_ids)
   
    print('Successfully cleared all trash blocks.')
