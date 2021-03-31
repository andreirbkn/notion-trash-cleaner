from notion.client import NotionClient

def get_trash(client, q):
    query = {
        'sort' : "Relevance",
        'query': q,
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
    try:
        results = client.post('search', query)
    except:
        print("Something goes wrong")

    blocks = results.json()['results']
    return blocks

def show_names(client, blocks_ids):
    for block_id in blocks:
            id = block_id['id']
            page = client.get_block(id)
            print(page.title)
        
def throw_out(client, blocks):
     for block in blocks:
        try:
            client.post("deleteBlocks", {"blockIds": [block['id']], "permanentlyDelete": True})
            print(block['id'])
        except:
          print("Something goes wrong")

if __name__== "__main__":

    with open('token.txt', 'r') as file:
        token = file.read().replace('\n', '')
    client = NotionClient(token_v2=token)

    #alphabet = "qwertyuiop[]asdfghjkl;'zxcvbnm/1234567890-=+йцукенгшщзхъфывапролджэячсмитьбかきくけこがぎぐげごさしすせそざじずぜぞたちつてとだぢづでどなにぬねのはひふへほばびぶべぼぱぴぷぺぽまみむめもやゆよらりるれろわゐゑをю"

    print('====> Start')
    # for letter in alphabet:
    #     print ("=== " + letter + " ===")
    #     blocks = get_trash(client, letter)
    #     throw_out(client, blocks)

    N = 100

    while N > 0:
        print ("=== " + str(N) + " ===")
        blocks = get_trash(client, "")
        throw_out(client, blocks)
        N-=1
   
    print('====> Successfully cleared all trash blocks.')
