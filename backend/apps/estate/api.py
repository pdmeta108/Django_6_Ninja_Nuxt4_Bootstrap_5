from ninja import Router, Schema
from typing import List, Optional
from django.shortcuts import get_object_or_404
from .models import Estate, Municipality, Parish

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

# --- ENDPOINTS (CRUD) ---

# 1. Listar estados (GET)
@router.get("/", response=List[EstateSchema])
def list_estate(request):
    return Estate.objects.all()

# 2. Listar municipios (GET)
@router.get("/municipalities", response=List[MunicipalitySchema])
def list_municipality(request):
    return Municipality.objects.select_related("estate")

# 3. Listar municipios que pertenecen al estado (GET)
@router.get("/municipalities/{estate_id}", response=List[MunicipalitySchema])
def get_municipalities_by_estate(request, estate_id):
    # Access the estate object or its ID
    current_estate_code = get_object_or_404(Estate, pk=estate_id).code

    return Municipality.objects.filter(estate_id=current_estate_code)

# 2. Listar parroquias (GET)
@router.get("/parishes", response=List[ParishSchema])
def list_parish(request):
    return Parish.objects.select_related("municipality")

# 3. Listar parroquias que pertenecen al municipio (GET)
@router.get("/parishes/{municipality_id}", response=List[ParishSchema])
def get_parishes_by_municipality(request, municipality_id):
    # Access the municipality object or its ID
    current_municipality_code = get_object_or_404(Municipality, pk=municipality_id).code

    return Parish.objects.filter(municipality_id=current_municipality_code)