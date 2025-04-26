#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 24 20:29:23 2025
@author: damonharris1_snhu
"""

from pymongo import MongoClient
from bson.objectid import ObjectId
from pymongo.errors import PyMongoError


class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self):
        # Connection Variables
        USER = 'aacuser'
        PASS = 'SNHU1234'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 32648
        DB = 'AAC'
        COL = 'animals'

        # Initialize Connection
        try:
            self.client = MongoClient(f'mongodb://{USER}:{PASS}@{HOST}:{PORT}')
            self.database = self.client[DB]
            self.collection = self.database[COL]
            print("Connected to MongoDB.")
        except PyMongoError as e:
            print("Failed to connect to MongoDB:", str(e))
            self.client = None

    def create(self, data):
        """Inserts a document into the animals collection."""
        if data:
            try:
                result = self.collection.insert_one(data)
                return result.acknowledged
            except PyMongoError as e:
                print("Insert failed:", str(e))
                return False
        else:
            raise Exception("Nothing to save, because data parameter is empty")

    def read(self, query):
        """Queries for documents from the animals collection."""
        if query:
            try:
                results = list(self.collection.find(query))
                return results
            except PyMongoError as e:
                print("Query failed:", str(e))
                return []
        else:
            raise Exception("Nothing to search, because query parameter is empty")

    def update(self, query, update_data, multiple=False):
        """
        Updates document(s) in the collection based on a lookup query and update data.
        """
        if query and update_data:
            try:
                if multiple:
                    result = self.collection.update_many(query, update_data)
                else:
                    result = self.collection.update_one(query, update_data)
                return result.modified_count
            except PyMongoError as e:
                print("Update failed:", str(e))
                return 0
        else:
            raise Exception("Missing query or update_data for update")

    def delete(self, query, multiple=False):
        """
        Deletes document(s) based on a query.
        """
        if query:
            try:
                if multiple:
                    result = self.collection.delete_many(query)
                else:
                    result = self.collection.delete_one(query)
                return result.deleted_count
            except PyMongoError as e:
                print("Delete failed:", str(e))
                return 0
        else:
            raise Exception("Missing query for delete")


# ===================
# Example usage
# ===================
if __name__ == "__main__":
    shelter = AnimalShelter()

    # Example insert
    animal = {"name": "Clawdeah", "type": "Cat", "age": 4}
    success = shelter.create(animal)
    print("Insert successful?", success)

    # Example read
    result = shelter.read({"type": "Cat"})
    print("Query results:", result)

    # Example update
    num_modified = shelter.update({"name": "Clawdeah"}, {"$set": {"age": 5}})
    print("Documents modified:", num_modified)

    # Example delete
    num_deleted = shelter.delete({"name": "Clawdeah"})
    print("Documents deleted:", num_deleted)
