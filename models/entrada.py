from . import db
from datetime import date
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, Date, ForeignKey

class Entrada(db.Model):
    __tablename__ = "entradas"
    
    entrada_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    entrada_producto_id: Mapped[int] = mapped_column(Integer, ForeignKey("productos.producto_id"), nullable=False)
    entrada_cantidad: Mapped[int] = mapped_column(Integer, nullable=False)
    entrada_factura: Mapped[str] = mapped_column(String(100), nullable=False)
    entrada_stand: Mapped[str] = mapped_column(String(50), nullable=False)
    entrada_ubicacion: Mapped[str] = mapped_column(String(100), nullable=False)
    entrada_fecha: Mapped[date] = mapped_column(Date, default=date.today)

    producto = relationship("Producto", backref="entradas")

    def to_dict(self):
        return {
            "id": self.entrada_id,
            "producto_id": self.entrada_producto_id,
            "producto_nombre": self.producto.nombre if self.producto else None,
            "cantidad": self.entrada_cantidad,
            "factura": self.entrada_factura,
            "stand": self.entrada_stand,
            "ubicacion": self.entrada_ubicacion,
            "fecha": self.entrada_fecha.isoformat() if self.entrada_fecha else None
        }
    