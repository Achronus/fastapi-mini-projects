from typing import Annotated
from app.api.car.schema import Car
from fastapi import APIRouter, Body, HTTPException, Query, status

from app.data.cars import CARS_DATA
from app.api.car.response import CarListResponse, CarResponse

from zentra_api.responses import SuccessMsgResponse


router = APIRouter(prefix="/cars", tags=["Cars"])


@router.get("", response_model=CarListResponse)
def get_cars(
    limit: Annotated[
        str | None,
        Query(max_length=3, description="Maximum number of items to retrieve."),
    ] = "10",
):
    response = []

    for id, car in list(CARS_DATA.items())[: int(limit)]:
        response.append(Car(**car))

    return CarListResponse(code=status.HTTP_200_OK, data=response)


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


@router.patch("/{id}", response_model=SuccessMsgResponse)
def update_car(id: int, car: Car):
    pass
