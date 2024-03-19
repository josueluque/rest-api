from fastapi import Response, Request, FastAPI
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from starlette import status
# from starlette.requests import Request
# from starlette.responses import JSONResponse


class ErrorHandler(BaseHTTPMiddleware):
    def __init__(self, app: FastAPI) -> None:
        super().__init__(app)

    async def dispatch(self, request: Request, call_next) -> Response | JSONResponse:
        try:
            return await call_next(request)
        except Exception as e:
            return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content={'Error': str(e)})
        

# class ErrorHandler():
#     async def __call__(self, request: Request, call_next) -> Response | JSONResponse:
#         try:
#             response = await call_next(request)
#             return response
#         except Exception as e:
#             return JSONResponse({"Error": str(e)}, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)