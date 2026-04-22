from ninja import Router, Schema
from django.shortcuts import get_object_or_404
from typing import List, Optional
from .models import Person

router = Router()

# --- SCHEMAS ---
class EstateSchema(Schema):
    """Schema basado en el modelo para devolver datos (Output)"""
    id: int
    name: str
    code: str

class MunicipalitySchema(Schema):
    """Schema basado en el modelo para devolver datos (Output)"""
    id: int
    name: str
    code: str
    estate: Optional[EstateSchema] = None

class ParishSchema(Schema):
    """Schema basado en el modelo para devolver datos (Output)"""
    id: int
    name: str
    code: str
    municipality: Optional[MunicipalitySchema] = None

class PersonSchema(Schema):
    """Schema basado en el modelo para devolver datos (Output)"""
    id: int
    name: str
    email: str
    age: int
    estate: Optional[EstateSchema] = None
    municipality: Optional[MunicipalitySchema] = None
    parish: Optional[ParishSchema] = None

class PersonCreateSchema(Schema):
    """Schema para recibir datos al crear o actualizar (Input)"""
    name: str
    email: str
    age: int
    estate: str
    municipality: str
    parish: str

# --- ENDPOINTS (CRUD) ---

# 1. Listar personas (GET)
@router.get("/", response=List[PersonSchema])
def list_people(request):
    return Person.objects.select_related("estate", "municipality", "parish")

# 2. Obtener una persona (GET por ID)
@router.get("/{person_id}", response=PersonSchema)
def get_person(request, person_id: int):
    person = get_object_or_404(Person, id=person_id)
    return person

# 3. Crear una persona (POST)
@router.post("/", response=PersonSchema)
def create_person(request, data: PersonCreateSchema):
    # .dict() convierte el esquema de Pydantic en un diccionario de Python
    person = Person.objects.create(**data.dict())
    return person

# 4. Actualizar una persona (PUT)
@router.put("/{person_id}", response=PersonSchema)
def update_person(request, person_id: int, data: PersonCreateSchema):
    person = get_object_or_404(Person, id=person_id)
    for attr, value in data.dict().items():
        setattr(person, attr, value)
    person.save()
    return person

# 5. Eliminar una persona
@router.delete("/{person_id}")
def delete_person(request, person_id: int):
    person = get_object_or_404(Person, id=person_id)
    person.delete()
    return {"success": True, "message": f"Person {person_id} deleted successfully"}

# 1. Listar estados (GET)
# @router.get("/estates", response=List[EstateSchema])
# def list_estate(request):
#     estate = Estate.objects.all()
#     print(estate)
#     return Estate.objects.all()

# 1. Listar municipios (GET)
# @router.get("/municipalities", response=List[MunicipalitySchema])
# def list_municipality(request):
#     return Municipality.objects.select_related("estate")

# 1. Listar parroquias (GET)
# @router.get("/parishes", response=List[ParishSchema])
# def list_parish(request):
#     return Parish.objects.select_related("municipality")