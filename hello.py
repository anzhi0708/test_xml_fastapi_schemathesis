from dataclasses import dataclass

from fastapi import FastAPI, Request, Response, Body
from fastapi.openapi.utils import get_openapi
from pydantic import BaseModel
from fastapi_xml import add_openapi_extension, XmlRoute, XmlAppResponse, XmlBody

app = FastAPI(title="Hello")


@dataclass
class _AccessIdentifier:
    SenderIdentifier: str
    ReceiverIdentifier: str

@dataclass
class _root:
    AccessIdentifier: _AccessIdentifier

@dataclass
class wraproot:
    root: _root


@app.post("/xml", response_class=Response)
async def xml(req: _root = XmlBody()):
    return Response(content="<result>OK</result>", media_type='application/xml')


@app.post("/")
async def main(request: Request, model: wraproot):
    return '{"result": "OK"}'



