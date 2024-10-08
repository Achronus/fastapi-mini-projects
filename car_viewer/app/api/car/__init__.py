from typing import Annotated
from app.api.car.schema import Car
from fastapi import APIRouter, Body, HTTPException, Query, status, Request
from fastapi.responses import HTMLResponse

from app.data.cars import CARS_DATA
from app.templates import templates
from app.api.car.response import CarResponse

from zentra_api.responses import SuccessMsgResponse


router = APIRouter(prefix="/cars", tags=["Cars"])


@router.get("", response_class=HTMLResponse)
def get_cars(
    request: Request,
    limit: Annotated[
        str | None,
        Query(max_length=3, description="Maximum number of items to retrieve."),
    ] = "10",
):
    cars = []

    for id, car in list(CARS_DATA.items())[: int(limit)]:
        cars.append(Car(**car))

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "cars": cars,
        },
    )


@router.get("/{id}", response_model=CarResponse)
def get_car_by_id(id: int):
    if id in CARS_DATA:
        return CarResponse(code=status.HTTP_200_OK, data=Car(**CARS_DATA[id]))

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Car not found.",
    )


@router.post(
    "/cars", response_model=SuccessMsgResponse, status_code=status.HTTP_201_CREATED
)
def create_car(cars: list[Car], min_id: Annotated[int | None, Body()] = 0):
    if len(cars) < 1:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No cars to add.",
        )

    min_id = len(CARS_DATA.keys()) + min_id

    for car in cars:
        while CARS_DATA.get(min_id):
            min_id += 1

        CARS_DATA[min_id] = car
        min_id += 1

    return SuccessMsgResponse(
        code=status.HTTP_201_CREATED, message="Cars created successfully."
    )


@router.put("/{id}", response_model=CarResponse)
def update_car(id: int, car: Car):
    stored = CARS_DATA.get(id)

    if not stored:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Car not found."
        )

    stored = Car(**stored)
    new_car = car.model_dump(exclude_unset=True)
    new_car = stored.model_copy(update=new_car)
    CARS_DATA[id] = new_car.model_dump()

    return CarResponse(code=status.HTTP_200_OK, data=Car(**CARS_DATA[id]))


@router.delete("/{id}", response_model=SuccessMsgResponse)
def delete_car(id: int):
    if not CARS_DATA.get(id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Car not found."
        )

    if id in CARS_DATA:
        CARS_DATA.pop(id)

    return SuccessMsgResponse(
        code=status.HTTP_201_CREATED, message="Car deleted successfully."
    )
