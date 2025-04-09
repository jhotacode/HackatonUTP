from odoo import models, fields

class Producto(models.Model):
    _name = 'quindicolor.producto'
    _description = 'Producto de Quindicolor'

    name = fields.Char(string='Nombre del producto', required=True)
    descripcion = fields.Text(string='Descripción del producto')
    
    categoria = fields.Selection([
        ('pintura', 'Pintura'),
        ('ferreteria', 'Ferretería'),
        ('arquitectonica', 'Línea Arquitectónica'),
        ('automotriz', 'Línea Automotriz'),
        ('madera', 'Línea para Madera'),
        ('otros', 'Otros'),
    ], string='Categoría', required=True)

    subcategoria = fields.Char(string='Subcategoría (opcional)')

    codigo_interno = fields.Char(string='Código interno', required=False, copy=False, readonly=True, default=lambda self: self.env['ir.sequence'].next_by_code('quindicolor.producto'))
    
    unidad_medida = fields.Selection([
        ('lt', 'Litros'),
        ('ml', 'Mililitros'),
        ('gl', 'Galones'),
        ('kg', 'Kilogramos'),
        ('g', 'Gramos'),
        ('unidad', 'Unidad'),
        ('caja', 'Caja'),
        ('pqt', 'Paquete'),
    ], string='Unidad de medida', required=True)

    precio = fields.Float(string='Precio de venta', required=True)
    costo = fields.Float(string='Costo de adquisición', required=False)
    stock = fields.Integer(string='Cantidad en inventario', default=0)
    ubicacion_bodega = fields.Char(string='Ubicación en bodega')  # Ej: Estantería 3, Estante B

    marca = fields.Char(string='Marca')
    proveedor = fields.Char(string='Proveedor principal')
    es_activo = fields.Boolean(string='Disponible para la venta', default=True)

    def action_guardar_info(self):
        for record in self:
            # Lógica para guardar la información
            pass



