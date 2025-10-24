"""
FastAPI REST API - Starter Code
================================

Este arquivo contém a estrutura básica para começar sua API de tarefas.
Complete as partes marcadas com TODO para implementar a funcionalidade completa.

Para executar:
1. Instale as dependências: pip install fastapi uvicorn
2. Execute o servidor: uvicorn main:app --reload
3. Acesse a documentação: http://localhost:8000/docs
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

# Inicializar a aplicação FastAPI
app = FastAPI(
    title="To-Do List API",
    description="Uma API REST simples para gerenciar tarefas",
    version="1.0.0"
)

# TODO: Definir o modelo Pydantic para Task
class Task(BaseModel):
    id: int
    title: str = Field(..., min_length=3, description="Título da tarefa")
    description: Optional[str] = Field(None, description="Descrição detalhada")
    completed: bool = Field(default=False, description="Status de conclusão")
    created_at: datetime = Field(default_factory=datetime.now)
    
    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "title": "Estudar FastAPI",
                "description": "Completar a tarefa de APIs REST",
                "completed": False,
                "created_at": "2025-10-24T10:00:00"
            }
        }


# Modelo para criação de tarefas (sem id e created_at)
class TaskCreate(BaseModel):
    title: str = Field(..., min_length=3)
    description: Optional[str] = None
    completed: bool = False


# Banco de dados em memória (lista de tarefas)
tasks_db: List[Task] = []
next_id = 1


# TODO: Implementar endpoint GET / - Mensagem de boas-vindas
@app.get("/")
async def root():
    """Endpoint raiz - retorna mensagem de boas-vindas"""
    return {
        "message": "Bem-vindo à To-Do List API!",
        "docs": "/docs",
        "endpoints": {
            "GET /tasks": "Listar todas as tarefas",
            "GET /tasks/{id}": "Obter uma tarefa específica",
            "POST /tasks": "Criar nova tarefa",
            "PUT /tasks/{id}": "Atualizar tarefa",
            "DELETE /tasks/{id}": "Deletar tarefa"
        }
    }


# TODO: Implementar endpoint GET /tasks - Listar todas as tarefas
@app.get("/tasks", response_model=List[Task])
async def get_tasks():
    """Retorna lista de todas as tarefas"""
    pass  # Substitua com sua implementação


# TODO: Implementar endpoint GET /tasks/{id} - Obter tarefa por ID
@app.get("/tasks/{task_id}", response_model=Task)
async def get_task(task_id: int):
    """Retorna uma tarefa específica pelo ID"""
    pass  # Substitua com sua implementação
    # Dica: Use HTTPException(status_code=404) se a tarefa não for encontrada


# TODO: Implementar endpoint POST /tasks - Criar nova tarefa
@app.post("/tasks", response_model=Task, status_code=201)
async def create_task(task: TaskCreate):
    """Cria uma nova tarefa"""
    global next_id
    pass  # Substitua com sua implementação
    # Dica: Incremente next_id após criar cada tarefa


# TODO: Implementar endpoint PUT /tasks/{id} - Atualizar tarefa
@app.put("/tasks/{task_id}", response_model=Task)
async def update_task(task_id: int, task_update: TaskCreate):
    """Atualiza uma tarefa existente"""
    pass  # Substitua com sua implementação


# TODO: Implementar endpoint DELETE /tasks/{id} - Deletar tarefa
@app.delete("/tasks/{task_id}", status_code=204)
async def delete_task(task_id: int):
    """Deleta uma tarefa"""
    pass  # Substitua com sua implementação


# Função auxiliar (opcional, mas recomendada)
def find_task_by_id(task_id: int) -> Optional[Task]:
    """Encontra uma tarefa pelo ID"""
    for task in tasks_db:
        if task.id == task_id:
            return task
    return None


# Para testar localmente, execute:
# uvicorn main:app --reload
# Acesse: http://localhost:8000/docs
