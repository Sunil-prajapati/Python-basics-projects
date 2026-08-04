from sqlalchemy import Boolean, create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from fastapi import FastAPI, Depends, HTTPException

app = FastAPI()

DATABASE_URL = "sqlite:///./test.db"  # Example database URL, change as needed
engine = create_engine(DATABASE_URL,connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    completed = Column(Boolean, default=False, nullable=False)  # Use Boolean for boolean representation

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/todos")
def create_todo(title:str, db: Session = Depends(get_db)):
    todo = Todo(title=title,completed=False)
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return {"id": todo.id, "title": todo.title, "completed": todo.completed, "message": "Todo created successfully!"}

@app.get("/todos")
def read_todos(db: Session = Depends(get_db)):
    todos = db.query(Todo).all()
    return [{"id": todo.id, "title": todo.title, "completed": todo.completed, "message": "Todos retrieved successfully!"} for todo in todos]

@app.get("/todos/{todo_id}")
def read_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return {"id": todo.id, "title": todo.title, "completed": todo.completed, "message": "Todo retrieved successfully!"}

@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, title: str = None, completed: bool = None, db: Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    if title is not None:
        todo.title = title
    if completed is not None:
        todo.completed = completed
    db.commit()
    db.refresh(todo)
    return {"id": todo.id, "title": todo.title, "completed": todo.completed, "message": "Todo updated successfully!"}

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    db.delete(todo)
    db.commit()
    return {"message": "Todo deleted successfully!"}