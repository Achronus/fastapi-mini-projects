from app.api.car.schema import Car

from zentra_api.responses import SuccessResponse


class CarListResponse(SuccessResponse[list[Car]]):
    """A response for returning a list of cars."""

    pass


class CarResponse(SuccessResponse[Car]):
    """A response for returning a single car."""

    pass
