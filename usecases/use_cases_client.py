from entities.model import Client
from datasource.db_session import local_session

def insert(client:Client)->bool: # type: ignore
    with local_session() as orm:
        if client:
            orm.add(client)
            orm.commit()
            return True

def select_all()->list[Client]:
    with local_session() as orm:
        all=orm.query(Client).all()
        return all

def update(client:Client)->bool:
    with local_session() as orm:
        result=orm.query(Client).filter(Client.id==client.id).update({
            Client.name: client.name,
            Client.address: client.address,
            Client.email: client.email
        })
        orm.commit()
        return result>0
    
def delete(id:int)->bool:
    with local_session() as orm:
        result=orm.query(Client).filter(Client.id==id).delete()
        orm.commit()
        return result>0