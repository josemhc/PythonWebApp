from flask import Blueprint, request, jsonify
from products.models.product_model import Products
from db.db import db

product_controller = Blueprint('product_controller', __name__)

@product_controller.route('/api/products', methods=['GET'])
def get_products():
    print("listado de productos")
    products = Products.query.all()
    result = [{'id':product.id, 'name': product.name, 'owner': product.owner, 'section': product.section} for product in products]
    return jsonify(result)

# Get single product by id
@product_controller.route('/api/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    print("obteniendo usuario")
    product = Products.query.get_or_404(product_id)
    return jsonify({'id': product.id, 'name': product.name, 'owner': product.owner, 'section': product.section})

@product_controller.route('/api/products', methods=['POST'])
def create_product():
    print("creando usuario")
    data = request.json
    new_product = Products(name=data['name'], owner=data['owner'], section=data['section'])
    db.session.add(new_product)
    db.session.commit()
    return jsonify({'message': 'User created successfully'}), 201

# Update an existing product
@product_controller.route('/api/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    print("actualizando usuario")
    product = Products.query.get_or_404(product_id)
    data = request.json
    product.name = data['name']
    product.owner = data['owner']
    product.section = data['section']
    db.session.commit()
    return jsonify({'message': 'User updated successfully'})

# Delete an existing product
@product_controller.route('/api/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = Products.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    return jsonify({'message': 'User deleted successfully'})