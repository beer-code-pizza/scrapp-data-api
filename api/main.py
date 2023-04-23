from sqlalchemy.orm import Session
from api.database.database import engine, Base, get_db
from api.database.models import Prezunic,MercadoLivre,PaodeAcucar
from fastapi import FastAPI, Query,  Depends, HTTPException, status, Response
from api.database.repositories import PrezunicRepository,MercadoLivreRepository,PaodeAcucarRepository
from api.database.schemas import PrezunicRequest, PrezunicResponse, MercadoLivreRequest, MercadoLivreResponse, PaodeAcucarRequest, PaodeAcucarResponse

Base.metadata.create_all(bind=engine)

app = FastAPI()

#############################################################################################
#################################      Prezunic      ########################################
#############################################################################################

@app.get("/health", response_model=list[PrezunicResponse])
def health():   
    return "ok"

@app.get("/api/prezunic/list_itens", response_model=list[PrezunicResponse])
async def find_all(page: int = Query(1, gt=0), page_size: int = Query(10, gt = 0, le=100), db: Session = Depends(get_db)):
    start_index = (page-1)*page_size
    end_index = start_index + page_size
    itens = PrezunicRepository.find_all(db)
    return [PrezunicResponse.from_orm(item) for item in itens][start_index:end_index]

@app.post("/api/prezunic/add_itens", response_model=PrezunicResponse, status_code=status.HTTP_201_CREATED)
def create(request: PrezunicRequest, db: Session = Depends(get_db)):
    item = list(PrezunicRepository).save(db, Prezunic(**request.dict()))
    return PrezunicResponse.from_orm(item)

@app.delete("/api/prezunic/delete_item/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_by_id(id: int, db: Session = Depends(get_db)):
    if not PrezunicRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Item não encontrado"
        )
    PrezunicRepository.delete_by_id(db, id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

#############################################################################################
##############################      Mercado Livre      ##########################   ############
#############################################################################################

@app.get("/api/mercadolivre/list_itens", response_model=list[MercadoLivreResponse])
def find_all(page: int = Query(1, gt=0), page_size: int = Query(10, gt = 0, le=100),db: Session = Depends(get_db)):
    start_index = (page-1)*page_size
    end_index = start_index + page_size
    itens = MercadoLivreRepository.find_all(db)
    return [MercadoLivreResponse.from_orm(item) for item in itens][start_index:end_index]

@app.post("/api/mercadolivre/add_itens", response_model=MercadoLivreResponse, status_code=status.HTTP_201_CREATED)
def create(request: MercadoLivreRequest, db: Session = Depends(get_db)):
    item = MercadoLivreRepository.save(db, MercadoLivre(**request.dict()))
    return MercadoLivreResponse.from_orm(item)

@app.delete("/api/mercadolivre/delete_item/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_by_id(id: int, db: Session = Depends(get_db)):
    if not MercadoLivreRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Item não encontrado"
        )
    MercadoLivreRepository.delete_by_id(db, id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

#############################################################################################
##############################      Pao de Acucar      ######################################
#############################################################################################

@app.get("/api/paodeacucar/list_itens", response_model=list[PaodeAcucarResponse])
def find_all(page: int = Query(1, gt=0), page_size: int = Query(10, gt = 0, le=100),db: Session = Depends(get_db)):
    start_index = (page-1)*page_size
    end_index = start_index + page_size
    itens = PaodeAcucarRepository.find_all(db)
    return [PaodeAcucarResponse.from_orm(item) for item in itens][start_index:end_index]

@app.post("/api/paodeacucar/add_itens", response_model=MercadoLivreResponse, status_code=status.HTTP_201_CREATED)
def create(request: PaodeAcucarRequest, db: Session = Depends(get_db)):
    item = PaodeAcucarRepository.save(db, PaodeAcucar(**request.dict()))
    return PaodeAcucarResponse.from_orm(item)

@app.delete("/api/paodeacucar/delete_item/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_by_id(id: int, db: Session = Depends(get_db)):
    if not PaodeAcucarRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Item não encontrado"
        )
    PaodeAcucarRepository.delete_by_id(db, id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)