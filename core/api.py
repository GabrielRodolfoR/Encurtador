from ninja import NinjaAPI
from shortner.api import shortner_router

api = NinjaAPI()
api.add_router("", shortner_router)