from flask_restful import Resource, reqparse
from models.item import ItemModel

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    # parser.add_argument('store_id',
    #                     type=int,
    #                     required=True,
    #                     help="Every item needs a store_id."
    #                     )

#    @jwt_required()
    def get(self, id):
        item = ItemModel.find_by_id(id)
        if item:
            return item.json()
        return {'message': 'Item not found'}, 404

    def delete(self, id):
        item = ItemModel.find_by_id(id)
        if item:
            item.delete_from_db()
            return {'message': 'Item deleted.'}
        return {'message': 'Item not found.'}, 404

    def patch(self, id):
        data = Item.parser.parse_args()

        item = ItemModel.find_by_id(id)

        if item:
            item.name = data['name']
            item.save_to_db()
            return item.json()
        else:
            return {'message': 'Item not found'}, 404


class ItemList(Resource):
    def get(self):
        return {'items': list(map(lambda x: x.json(), ItemModel.query.all()))}

    def post(self):

        data = Item.parser.parse_args()

        item = ItemModel(**data)

        try:
            item.save_to_db()
        except Exception as e:
            print(e)
            return {"message": "An error occurred inserting the item."}, 500

        return item.json(), 201
