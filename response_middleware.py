from fastapi import FastAPI, Request, Response
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse
import json

class ResponseWrapperMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        try:
            # Call the actual route handler
            response = await call_next(request)

            # If it's already a JSON response, we wrap it
            if response.headers.get("content-type") == "application/json":
                body = [section async for section in response.body_iterator]
                raw_data = b"".join(body).decode()

                # Rebuild response
                try:
                    data = json.loads(raw_data)
                    wrapped = {
                        "success": True,
                        "data": data,
                        "message": "OK"
                    }
                except json.JSONDecodeError:
                    # In case response is not valid JSON
                    wrapped = {
                        "success": False,
                        "data": None,
                        "message": "Invalid JSON response from server"
                    }

                return JSONResponse(content=wrapped, status_code=response.status_code)

            # Not JSON (e.g. HTML, plain text, etc.)
            return response

        except Exception as e:
            # Catch unhandled exceptions and wrap them too
            return JSONResponse(
                status_code=500,
                content={
                    "success": False,
                    "data": None,
                    "message": f"Internal server error: {str(e)}"
                }
            )
