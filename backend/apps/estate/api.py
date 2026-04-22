from ninja import Router, Schema
from typing import List
from .models import Estate

router = Router()

# --- SCHEMAS ---
class EstateSchema(Schema):
    """Schema basado en el modelo para devolver datos (Output)"""
    id: int
    name: str
    code: str

# --- ENDPOINTS (CRUD) ---

# 1. Listar estados (GET)
@router.get("/", response=List[EstateSchema])
def list_estate(request):
    return Estate.objects.all()

# 1. Listar municipios (GET)
# @router.get("/municipalities", response=List[MunicipalitySchema])
# def list_municipality(request):
#     return Municipality.objects.select_related("estate")

# 1. Listar parroquias (GET)
# @router.get("/parishes", response=List[ParishSchema])
# def list_parish(request):
#     return Parish.objects.select_related("municipality")