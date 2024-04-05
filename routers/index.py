from fastapi import FastAPI

from .registrationRoute import api as registration_sub_api
from .ownerRoute import api as owner_sub_api
from .userRoute import api as user_sub_api
from .adminRoute import api as admin_sub_api
from .problemRoute import api as problem_sub_api

#--------------Exception Handlers--------------------#
from exceptions.RegistrationException import add_user_registration_handler
from exceptions.AdminException import add_admin_exception_handler
from exceptions.OwnerException import add_owner_exception_handler

add_admin_exception_handler(admin_sub_api)
add_owner_exception_handler(owner_sub_api)
add_user_registration_handler(registration_sub_api)

#--------------MiddleWares--------------------#

from middlewares.tokenProcessingMiddleWare import TokenProcessingMiddleWare
from middlewares.adminMiddleWare import AdminMiddleWare
from middlewares.ownerMiddleWare import OwnerMiddleWare
from middlewares.JSONBodyReaderMiddleware import JSONParserMiddleWare

owner_sub_api.add_middleware(JSONParserMiddleWare)
owner_sub_api.add_middleware(OwnerMiddleWare)
owner_sub_api.add_middleware(TokenProcessingMiddleWare)

user_sub_api.add_middleware(TokenProcessingMiddleWare)

admin_sub_api.add_middleware(JSONParserMiddleWare)
admin_sub_api.add_middleware(AdminMiddleWare)
admin_sub_api.add_middleware(TokenProcessingMiddleWare)


#----------Adding subapis---------------#

subApp = FastAPI()
subApp.mount("/registration", registration_sub_api)
subApp.mount("/owner", owner_sub_api)
subApp.mount("/user", user_sub_api)
subApp.mount("/admin", admin_sub_api)
subApp.mount("/problem",problem_sub_api)

