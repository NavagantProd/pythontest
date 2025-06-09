from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()
class ReportRequest(BaseModel):
    topic: str
    year: int
    region: str
@app.post("/GenReport")
async def GenReport(req: ReportRequest):
    # Simulated processing
    result = {
        "summary": f"Report on {req.topic} for {req.region} in {req.year}.",
        "status": "success"
    }
    return JSONResponse(content=result)
