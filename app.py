from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse

app = FastAPI()

class ReportRequest(BaseModel):
    topic: str
    year: int
    region: str

@app.post("/GenReport")
async def GenReport(req: ReportRequest):
    result = {
        "summary": f"Report on {req.topic} for {req.region} in {req.year}.",
        "status": "success THIS WORK, AS INTENDWED"
    }
    return JSONResponse(content=result)
