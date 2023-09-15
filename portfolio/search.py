from portfolio import portfolio

def add_to_index(index, model):
    if not portfolio.elasticsearch:
        return
    
    data = {}
    for field in model.__searchable__:
        data[field] = getattr(model, field)
    portfolio.elasticsearch.index(index=index, id=model.id, body=data)

def remove_from_index(index, model):
    if not portfolio.elasticsearch:
        return
    portfolio.elasticsearch.delete(index=index, id=model.id)

def query_index(index, query, page, per_page):
    if not portfolio.elasticsearch:
        return
    search = portfolio.elasticsearch.search(
        index=index,
        query={
            'multi_match': {
                'query': query,
                "fields": ["*"]
            }
        },
        from_=(page - 1) * per_page,
        size=per_page
    )

    ids = [int(hit['_id']) for hit in search['hits']['hits']]

    return ids, search['hits']['total']['value']

