from sqlalchemy.orm import Session
from api.database.models import Prezunic
# , MercadoLivre, PaodeAcucar

#############################################################################################
################################      Prezunic      #########################################
#############################################################################################

class PrezunicRepository:
    @staticmethod
    def find_all(db: Session) -> list[Prezunic]:
        return db.query(Prezunic).all()

    @staticmethod
    def save(db: Session, Prezunic: Prezunic) -> Prezunic:
        if Prezunic.id:
            db.merge(Prezunic)
        else:
            db.add(Prezunic)
        db.commit()
        return Prezunic

    @staticmethod
    def find_by_font(db: Session, id: str) -> Prezunic:
        return db.query(Prezunic).filter(Prezunic.id == id).first()

    @staticmethod
    def exists_by_id(db: Session, id: int) -> bool:
        return db.query(Prezunic).filter(Prezunic.id == id).first() is not None

    @staticmethod
    def delete_all(db: Session) -> None:
        itens = db.query(Prezunic).all()
        db.delete(itens)
        db.commit()
    
    @staticmethod
    def delete_by_id(db: Session, id: str) -> None:
        itens = db.query(Prezunic).filter(Prezunic.id == id).first()
        if Prezunic is not None:
            db.delete(itens)
            db.commit()

# #############################################################################################
# ##############################      Mercado Livre      ######################################
# #############################################################################################

# class MercadoLivreRepository:
#     @staticmethod
#     def find_all(db: Session) -> list[MercadoLivre]:
#         return db.query(MercadoLivre).all()

#     @staticmethod
#     def save(db: Session, MercadoLivre: MercadoLivre) -> MercadoLivre:
#         if MercadoLivre.id:
#             db.merge(MercadoLivre)
#         else:
#             db.add(MercadoLivre)
#         db.commit()
#         return MercadoLivre

#     @staticmethod
#     def find_by_font(db: Session, id: str) -> MercadoLivre:
#         return db.query(MercadoLivre).filter(MercadoLivre.id == id).first()

#     @staticmethod
#     def exists_by_id(db: Session, id: int) -> bool:
#         return db.query(MercadoLivre).filter(MercadoLivre.id == id).first() is not None

#     @staticmethod
#     def delete_all(db: Session) -> None:
#         itens = db.query(MercadoLivre).all()
#         db.delete(itens)
#         db.commit()
    
#     @staticmethod
#     def delete_by_id(db: Session, id: str) -> None:
#         itens = db.query(MercadoLivre).filter(MercadoLivre.id == id).first()
#         if MercadoLivre is not None:
#             db.delete(itens)
#             db.commit()

# #############################################################################################
# ##############################      Pao de Acucar      ######################################
# #############################################################################################

# class PaodeAcucarRepository:
#     @staticmethod
#     def find_all(db: Session) -> list[PaodeAcucar]:
#         return db.query(PaodeAcucar).all()

#     @staticmethod
#     def save(db: Session, PaodeAcucar: PaodeAcucar) -> PaodeAcucar:
#         if PaodeAcucar.id:
#             db.merge(PaodeAcucar)
#         else:
#             db.add(PaodeAcucar)
#         db.commit()
#         return PaodeAcucar

#     @staticmethod
#     def find_by_font(db: Session, id: str) -> PaodeAcucar:
#         return db.query(PaodeAcucar).filter(PaodeAcucar.id == id).first()

#     @staticmethod
#     def exists_by_id(db: Session, id: int) -> bool:
#         return db.query(PaodeAcucar).filter(PaodeAcucar.id == id).first() is not None

#     @staticmethod
#     def delete_all(db: Session) -> None:
#         itens = db.query(PaodeAcucar).all()
#         db.delete(itens)
#         db.commit()
    
#     @staticmethod
#     def delete_by_id(db: Session, id: str) -> None:
#         itens = db.query(PaodeAcucar).filter(PaodeAcucar.id == id).first()
#         if PaodeAcucar is not None:
#             db.delete(itens)
#             db.commit()