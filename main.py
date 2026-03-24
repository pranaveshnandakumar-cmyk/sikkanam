from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class Trip(BaseModel):
    source: str
    destination: str
    days: int
    budget: int

@app.post("/plan-trip")
def plan_trip(trip: Trip):

    return {
        "route": [
            f"{trip.source} → Salem (Train)",
            f"Salem → {trip.destination} (Bus)"
        ],
        "travel_cost": 500,
        "hotel_budget_per_night": (trip.budget * 0.4) / trip.days,
        "recommended_hotels": [
            "Green Valley Stay",
            "Hill View Lodge"
        ],
        "tourist_places": [
            "Lake",
            "View Point"
        ]
    }
