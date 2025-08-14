from fastapi import FastAPI, Path, Query, Body
import uuid
from sqlalchemy.orm import sessionmaker
from utilities.db_engine import engine
from utilities.db_base import Base
from utilities.person import Person


#BD
Base.metadata.create_all(engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#FASTAPI
app = FastAPI()

#REQUESTS
@app.get("/")
async def root():
    print('hi')
    return 1

@app.post('/submit')
async def create_person(data: dict):
    p = Person(
        id=str(uuid.uuid4()),  # Generate a new UUID for the person ID
        name=data.get('name'),
        surname=data.get('surname'),
        gender=data.get('gender'),
        age=data.get('age')
    )
    db = SessionLocal()
    db.add(p)
    db.commit()
    db.refresh(p)
    return p.to_dict()

@app.get('/api/people')
async def get_people():
    db = SessionLocal()
    try:
        people = db.query(Person).all()
        return [p.to_dict() for p in people]
    except Exception as e:
        return {'error': str(e)}
    finally:
        db.close()