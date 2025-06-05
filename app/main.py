from fastapi import FastAPI, status, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from app.api.task_route import route as task_route
from app.api.user_route import router as user_router
from app.exceptions.exceptions import UserNotFoundException, TaskNotFoundException

app = FastAPI()


@app.exception_handler(UserNotFoundException)
async def user_not_found_exception_handler(request, exc: UserNotFoundException):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={
            "success": False,
            "message": exc.message,
        }
    )


@app.exception_handler(TaskNotFoundException)
async def task_not_found_exception_handler(request, exc: TaskNotFoundException):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={
            "success": False,
            "message": exc.message,
        }
    )


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc: RequestValidationError):
    print("Validation error occurred :", exc.errors())
    error_msgs = []
    for err in exc.errors():
        # Extrae el campo (último elemento de loc) y el mensaje
        field = err["loc"][-1]
        msg = err["msg"]
        error_msgs.append(f"{field} {msg}")
    return JSONResponse(
        status_code=422,
        content={"success": False, "message": "Data invalid", "errors": error_msgs},
    )


@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc: HTTPException):
    print("HTTP exception occurred :", exc.detail)
    return JSONResponse(
        status_code=exc.status_code,
        content={"success": False, "message": exc.detail},
    )


app.include_router(user_router)

app.include_router(task_route)
