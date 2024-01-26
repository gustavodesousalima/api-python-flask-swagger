class clientDb:
    # Lista de itens
    items = [
        {
            'id': 1,
            'nome': 'jozimar Back'
        },

        {
            'id': 2,
            'nome': 'Maria Antonieta',
            'endereco': 'Brasil'
        },
        {
            'id': 3,
            'nome': 'Rebecca Braz',
            'endereco': 'Brasil'
        }
    ]

    # Método para adicionar um item à lista
    @classmethod
    def adicionar(cls, item):
        cls.items.append(item)
        return True
    
    # Método para obter um item da lista
    @classmethod
    def obter(cls, id=None):
        if id:
            return next(filter(lambda x: x['id'] == id,cls.items),{})
        return cls.items
    
    # Método para remover um item da lista
    @classmethod
    def remover(cls, id):
        cls.items = list(filter(lambda x: x['id'] != id, cls.items),[])
        return {"mensagem": f"id {id} deletado com sucesso"}
    
    # Método para alterar um item da lista
    @classmethod
    def alterar(cls, id, novo_item:dict):
        item = next(filter(lambda x: x['id'] == id, cls.items),{})
        index = cls.items.index(item)

        if novo_item.get('nome'):
            item['nome'] = novo_item['nome']

        if novo_item.get('endereco'):
            item['endereco'] = novo_item.get('endereco')