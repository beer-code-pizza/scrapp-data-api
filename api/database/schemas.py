from pydantic import BaseModel


#############################################################################################
################################      Prezunic      #########################################
#############################################################################################

class PrezunicBase(BaseModel):
    id: int
    nome: str
    preco: float

class PrezunicRequest(PrezunicBase):
    ...

class PrezunicResponse(PrezunicBase):
    id: int

    class Config:
        orm_mode = True

#############################################################################################
##############################      Mercado Livre      ######################################
#############################################################################################

class MercadoLivreBase(BaseModel):
    id: int
    nome: str
    preco: float

class MercadoLivreRequest(MercadoLivreBase):
    ...

class MercadoLivreResponse(MercadoLivreBase):
    id: int

    class Config:
        orm_mode = True

#############################################################################################
##############################      Pao de Acucar      ######################################
#############################################################################################

class PaodeAcucarBase(BaseModel):
    id: int
    nome: str
    preco: float

class PaodeAcucarRequest(PaodeAcucarBase):
    ...

class PaodeAcucarResponse(PaodeAcucarBase):
    id: int

    class Config:
        orm_mode = True