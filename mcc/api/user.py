from ninja_extra import NinjaExtraAPI, api_controller, http_get, Router

router = Router()

@router.get('/users/')
def list_users(request):
    ...

@router.get('/users/{users_id}')
def users_details(request, news_id: int):
    ...
    
@router.get('/add')
def add(request, a: int, b: int):
    return {"result": a + b}

# 基于类的定义
@api_controller('/math', tags=['Math'], permissions=[])
class MathAPI:

    @http_get('/subtract',)
    def subtract(self, a: int, b: int):
        """Subtracts a from b"""
        return {"result": a - b}

    @http_get('/divide',)
    def divide(self, a: int, b: int):
        """Divides a by b"""
        return {"result": a / b}

    @http_get('/multiple',)
    def multiple(self, a: int, b: int):
        """Multiples a with b"""
        return {"result": a * b}